from tkinter import *
import os.path

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

path = 'C:\goodus\TFP3530.ini'
name = 'cashier-'
avtor = '©by Tolchelnikov'
error_write = 'не поменял'
error_none = 'файла с настройками нет'
success = 'Успешно поменял'
step = 20

root = Tk()
root.title('SetDateTimeAtStart')
canvas = Canvas(root, width=600, height=600)
canvas.pack()
canvas.create_text(500, 580, text=avtor, fill='black', font=('Helvetica', 16))


def setDateTimeAtStart_ON():
    canvas.delete("all")
    canvas.clipboard_clear()
    if (os.path.exists(path)):
        first_x = 200
        config = configparser.ConfigParser()
        try:
            config.read(path)
            config.set("Reliability", "setdatetimeatstart", "1")
            with open(path, 'w') as configfile:  # save
                config.write(configfile)
            canvas.create_text(90, first_x, text=success, fill='green', font=('Helvetica', 12))
        except:
            canvas.create_text(90, first_x, text=error_write, fill='red', font=('Helvetica', 12))
    else:
        canvas.create_text(90, 200, text=error_none, fill='red', font=('Helvetica', 12))


def setDateTimeAtStart_OFF():
    canvas.delete("all")
    if (os.path.exists(path)):
        first_x = 200
        config = configparser.ConfigParser()
        try:
            config.read(path)
            config.set("Reliability", "setdatetimeatstart", "0")
            with open(path, 'w') as configfile:  # save
                config.write(configfile)
            canvas.create_text(90, first_x, text=success, fill='green', font=('Helvetica', 12))
        except:
            canvas.create_text(90, first_x, text=error_write, fill='red', font=('Helvetica', 12))
    else:
        canvas.create_text(90, 200, text=error_none, fill='red', font=('Helvetica', 12))


but_On = Button(root, text='Выключить', width=10, height=2, command=lambda: setDateTimeAtStart_ON())
but_Off = Button(root, text='Выключить', width=10, height=2, command=lambda: setDateTimeAtStart_OFF())
but_Off['bg'] = 'red'
but_On['bg'] = 'green'
but_On.place(x=10, y=50)
but_Off.place(x=100, y=50)
root.mainloop()
