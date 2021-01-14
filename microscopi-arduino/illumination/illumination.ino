#include <Wire.h>
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"

//=============== Definitions =================//

// Initialise matrix
Adafruit_8x8matrix matrix = Adafruit_8x8matrix();

// Initialise command
String command = "";

// Declare illumination source states
enum SourceStates {MATRIX};

// Declare matrix shapes
enum matrixStates {
  MATRIX_ALL,
  MATRIX_NONE,
  MATRIX_BF,
  MATRIX_DF,
  MATRIX_TOP,
  MATRIX_BOTTOM,
  MATRIX_RIGHT,
  MATRIX_LEFT
};

// Set matrix variables
uint8_t matrixAddr = 0x70;
enum matrixStates matrixState;
float matrixPixelSize = 3.81;
float matrixRadius = matrixPixelSize * 3;
int matrixOblique = 4;
long matrixClock = 400000L;

// Set initial source
enum SourceStates source;

//=============== Functions ===================//

// Initialise source
void initSource(){
  if (source == MATRIX){
    Serial.println("Init matrix");

    // Start matrix i2c communication
    matrix.begin(matrixAddr);

    // Set initial matrix state
    matrixSetClock(matrixClock);
    matrixSetBrightness(0);
    matrixDraw(MATRIX_ALL);
    matrixOn();
  } 
  else {
    Serial.println("Invalid source");
  }

};

// Turn matrix on
void matrixOn() {
  matrixDraw(matrixState);
  matrix.writeDisplay();
}

// Turn matrix off
void matrixOff() {
  matrix.clear();
  matrix.writeDisplay();
}

// General matrix draw method
void matrixDraw(enum matrixStates state){
  matrix.clear();

  float xpos;
  float ypos;
  float r;
      
  switch (state){
    matrixState = state;

    case MATRIX_ALL:
      matrix.fillRect(0, 0, 8, 8, LED_ON);
      break;
    
    case MATRIX_NONE:
      break;
    
    case MATRIX_BF:
      for (int i=0; i<8; i++){
        for (int j=0; j<8; j++) {
          xpos = -15.24+i*matrixPixelSize+matrixPixelSize/2;
          ypos = -15.24+j*matrixPixelSize+matrixPixelSize/2;
          r = sqrt(sq(xpos)+sq(ypos));
          if (r <= matrixRadius) {
            matrix.drawPixel(i, j, LED_ON);  
          }
          
        }
      }
      break;

    case MATRIX_DF:
      for (int i=0; i<8; i++){
        for (int j=0; j<8; j++) {
          xpos = -15.24+i*matrixPixelSize+matrixPixelSize/2;
          ypos = -15.24+j*matrixPixelSize+matrixPixelSize/2;
          r = sqrt(sq(xpos)+sq(ypos));
          if (r > matrixRadius) {
            matrix.drawPixel(i, j, LED_ON);  
          }
          
        }
      }
      break;

    case MATRIX_TOP:
      matrix.fillRect(0, 0, 8, matrixOblique, LED_ON);
      break;

    case MATRIX_BOTTOM:
      matrix.fillRect(0, 8-matrixOblique, 8, matrixOblique, LED_ON);
      break;

    case MATRIX_LEFT:
      matrix.fillRect(0, 0, matrixOblique, 8, LED_ON);
      break;

    case MATRIX_RIGHT:
      matrix.fillRect(8-matrixOblique, 0, matrixOblique, 8, LED_ON);
      break;
  }
  
  matrix.writeDisplay();
}

// Set matrix clock speed
void matrixSetClock(long clockspeed){
  // Turn off oscillator
  Wire.beginTransmission(matrixAddr);
  Wire.write(0x20);
  Wire.endTransmission();

  // Set clock speed
  Wire.setClock(clockspeed);

  // Restart oscillator
  Wire.beginTransmission(matrixAddr);
  Wire.write(0x21);
  Wire.endTransmission();

  // Set variable
  matrixClock = clockspeed;
}

// Set the brightness of the matrix from 0-15
void matrixSetBrightness(uint8_t brightness) {
  brightness = constrain(brightness,0,15);
  matrix.setBrightness(brightness);
  matrix.writeDisplay();
}

// Set radius for bright/dark-field
void matrixSetRadius(float r){
  matrixRadius = r;
}

// Set oblique illumination width
void matrixSetOblique(int w){
  matrixOblique = w;
}

// Process commands from serial
void process_command(String command){
  Serial.println("process command");
  if (command.startsWith("set source")) {
    String source_command = command.substring(11);
  
    if (source_command == "matrix") {
      source = MATRIX;
    } 

    initSource();
    return;
  }
  
  switch(source){
    case MATRIX:
      if (command == "on") {
        matrixOn();
      } else if (command == "off") {
        matrixOff();
      } else if (command == "all") {
        matrixDraw(MATRIX_ALL);  
      } else if (command == "bright") {
        matrixDraw(MATRIX_BF);
      } else if (command == "none") {
        matrixDraw(MATRIX_NONE);
      } else if (command == "dark") {
        matrixDraw(MATRIX_DF);
      } else if (command =="left") {
        matrixDraw(MATRIX_LEFT);
      } else if (command =="right") {
        matrixDraw(MATRIX_RIGHT);
      } else if (command =="top") {
        matrixDraw(MATRIX_TOP);
      } else if (command =="bottom") {
        matrixDraw(MATRIX_BOTTOM);
      } else if (command.startsWith("set brightness")){
        int val = command.substring(15).toFloat();
        matrixSetBrightness(val);
      } else if (command.startsWith("set radius")){
        float val = command.substring(11).toFloat();
        matrixSetRadius(val);
      } else if (command.startsWith("set oblique")){
        int val = command.substring(12).toInt();
        matrixSetOblique(val);
      } else if (command.startsWith("set clock")){
        int val = command.substring(10).toInt();
        matrixSetClock((long) val*1000);
      }
      break;
  }
}

//================ Main =======================//

// Setup function, called on program start
void setup() {
  Serial.begin(9600);

  // Wait for Serial to be active
  while (!Serial){;}
  
  // Debug log
  Serial.println("Begin illumination control");
  
  // Initialise source
  source = MATRIX;
  initSource();
  
}

// Main loop
void loop() {
  if (Serial.available() > 0) {
    char inputChar = (char)Serial.read();

    // Process command if it terminates in \n
    if (inputChar == '\n'){
      
      // Set command to lower case
      command.toLowerCase();

      // echo command for debugging
      Serial.println(command);
      
      // choose action based on command
      process_command(command);
      command = "";
    } 
    // otherwise add char to command
    else {
      command += inputChar;
    }
  }
}
