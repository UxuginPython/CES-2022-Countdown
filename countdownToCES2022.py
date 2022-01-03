try:
    from tkinter import *
except ImportError:
    from Tkinter import *
    from warnings import warn
    warn('You are using Python 2. It is recommended that you update to Python 3.')
window=Tk()
window.title('Countdown to CES')
label=Label(window, text='Loading...', font=('Arial', 72, ''))
label.pack()
import datetime
now=datetime.datetime.now
CESTime=datetime.datetime(2022, 1, 4, 8, 0, 0, 0) #Year, Month, Day, Hour, Minute, Second, Millisecond
while True:
    label.config(text=CESTime-datetime.datetime.now())
    window.update()
    window.update_idletasks()
