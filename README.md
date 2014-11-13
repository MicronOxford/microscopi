microscoPi
==========

Initial software for the 'microscoPI', Raspberry Pi based microscope platform


Basic instruction on how to run this software
----------------------------------------------

LOGGING INTO YOUR RASPBERRY PI, RUNNING THE PICAMERA FROM A PYTHON PROGRAM AND
EDITING THE SETTINGS AND PROGRAM. 

1. Once your Raspberry Pi has completed the boot process, a login prompt will
appear. The default login for Raspbian is username pi with the password
raspberry. Note you will not see any writing appear when you type the password.
This is a security feature in Linux.
2. After you have successfully logged in, you will see the command line prompt
pi@raspberrypi~$
3. To load the graphical user interface (GUI), type startx and press Enter on your
keyboard.
4. Once the GUI is running - double click on the terminal program to run it.
5. In the terminal window  at the prompt (unix command line prompt) type: cd
microscoPi (to change to the microscoPi director).
To run the microscoPi program (written in python using the picamera and pygame
libraries for capturing images in a GUI).  at the prompt type:   python
microscoPi.py
6. Once the program runs type p to get a preview window. Press again to remove the
window (toggle). Press c to capture an individual image as image.jpg. type t to
start time lapse with a default interval of 5 seconds. 
7. Try altering some settings in the settings.py file. And ps3.py contains
the settings for controlling the RSPI from a PS3 controller. 
8. To edit the files uses the editor nano, that understands python syntax.  e.g.
type nano settings.py



Feature suggestions from Ilan 12/11/2014
----------------------------------------
 1. settings.py should be a bit clearer and configurable in terms of easy
window it's size - roi of the camera displayed within the window and
initial position on the screen.

2. woukd be good to expose a bit more functionality. Such as video capture
from time lapse. H264 compressed.

3. good to add a skeletal visualization of jpgs and video module and
importing into bumpy arrays and displaying the numbers on the screen. Eg a
small box ROI of the image with another window showing the array of numbers
in the screen. Also raw capture and camera models. Ian can help with this
too.

4. woukd be good to add back more of the ps3 commands.

5. Running python within python (when pressing I for interactive)  Did not
work until I added the import code instruction that was missing. But it was
not much use as you could not return to the program from the python shell.
Ie quit() exited both the parent micriscoPI program and the spawned command
line python.

What do you think is easily feasible out of this and what GUI could be easy
to make more interactive with the ps3. Eg to change camera modes for
capture and contract etc. And then display the modes in a control window
showing settings. Is pygame good for this?

Would be good to write a guide to how to develop the program for
students. Eg some suggested new functionalities for them to try adding
in order of difficulty.
