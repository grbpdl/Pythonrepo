'''modules are anything that gives funtionality to our program
modules can be downloaded by typing pip install module_name(pip install playsound in this case) which will download the module from internet
modules should first be imported(import playsound in this case) after download for using
for ex:we will download a module named playsound which will play sound'''
print("playing your music.. ")
from playsound import playsound
playsound('C:\\Users\\User\\OneDrive\\Documents\\python ode\\play.mp3')#syntax and format given with module
import os
print(os.listdir())