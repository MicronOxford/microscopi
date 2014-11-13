microscoPi
==========

Initial software for the 'microscoPI', Raspberry Pi based microscope platform

Feature suggestions from Ilan 12/11/2014

 1) settings.py should be a bit clearer and configurable in terms of easy
window it's size - roi of the camera displayed within the window and
initial position on the screen.

2) woukd be good to expose a bit more functionality. Such as video capture
from time lapse. H264 compressed.

3) good to add a skeletal visualization of jpgs and video module and
importing into bumpy arrays and displaying the numbers on the screen. Eg a
small box ROI of the image with another window showing the array of numbers
in the screen. Also raw capture and camera models. Ian can help with this
too.

4) woukd be good to add back more of the ps3 commands.

5). Running python within python (when pressing I for interactive)  Did not
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
