import psutil
import time
import tkinter as tk
from tkinter import messagebox

print('How often should the pop-up appear?')
t = int(input('Hours: '))*60*60 + int(input('Minutes: '))*60 + int(input('Seconds: '))
while(1):
	cpup = psutil.cpu_percent()
	ramp = psutil.virtual_memory()[2]
	rama = psutil.virtual_memory()[1]
	ramused = psutil.virtual_memory()[3]
	root = tk.Tk()
	root.withdraw()
	messagebox.showinfo('Stats', 'CPU %: ' + str(cpup) + '\nRam %: ' + str(ramp) + '\nRam Available: ' + str(rama) + '\nRam Used: ' + str(ramused))
	time.sleep(t)