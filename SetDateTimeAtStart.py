from tkinter import *
import os.path

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

pth = r'\C$\ПУТЬ'
sladh = r'\\'
avtor = '©by Tolchelnikov'
file_name = '\настройки'
error_write = 'не поменял - '
error_none = 'нет файла - '
success_On = 'Успешно включил - '
success_Off = 'Успешно выключил - '
stepDown = 20
stepRight = 350
kass_list = ['1', '2', '3']
root = Tk()
root.title('SetDateTimeAtStart')
canvas = Canvas(root, width=700, height=700)
canvas.pack()
canvas.create_text(550, 680, text=avtor, fill='black', font=('Helvetica', 16))


def setDateTimeAtStart_ON():
    canvas.delete("all")
    canvas.create_text(550, 680, text=avtor, fill='black', font=('Helvetica', 16))
    i = 0
    first_x = 100
    first_z = 120

    while i < len(kass_list):

        canvas.clipboard_clear()
        if os.path.isfile(sladh + kass_list[i] + pth + file_name):

            config = configparser.ConfigParser()
            try:
                config.read(sladh + kass_list[i] + pth + file_name)
                config.set("Reliability", "setdatetimeatstart", "1")
                with open(sladh + kass_list[i] + pth + file_name, 'w') as configfile:  # save
                    config.write(configfile)
                canvas.create_text(first_z, first_x, text=success_On + kass_list[i], fill='green',
                                   font=('Helvetica', 12))
            except:
                canvas.create_text(first_z, first_x, text=error_write + kass_list[i], fill='red',
                                   font=('Helvetica', 12))
        else:
            canvas.create_text(first_z, first_x, text=error_none + kass_list[i], fill='red', font=('Helvetica', 12))
        print(sladh + kass_list[i] + pth + file_name)
        i = i + 1
        first_x = first_x + stepDown
        if first_x >= 680:
            first_z = first_z + stepRight
            first_x = 100


def setDateTimeAtStart_OFF():
    canvas.delete("all")
    canvas.create_text(550, 680, text=avtor, fill='black', font=('Helvetica', 16))
    i = 0
    first_x = 100
    first_z = 120

    while i < len(kass_list):

        canvas.clipboard_clear()
        if os.path.isfile(sladh + kass_list[i] + pth + file_name):

            config = configparser.ConfigParser()
            try:
                config.read(sladh + kass_list[i] + pth + file_name)
                config.set("Reliability", "setdatetimeatstart", "0")
                with open(sladh + kass_list[i] + pth + file_name, 'w') as configfile:  # save
                    config.write(configfile)
                canvas.create_text(first_z, first_x, text=success_Off + kass_list[i], fill='green',
                                   font=('Helvetica', 12))
            except:
                canvas.create_text(first_z, first_x, text=error_write + kass_list[i], fill='red',
                                   font=('Helvetica', 12))
        else:
            canvas.create_text(first_z, first_x, text=error_none + kass_list[i], fill='red', font=('Helvetica', 12))

        i = i + 1
        first_x = first_x + stepDown
        if first_x >= 680:
            first_z = first_z + stepRight
            first_x = 100


but_On = Button(root, text='Выключить', width=10, height=2, command=lambda: setDateTimeAtStart_ON())
but_Off = Button(root, text='Выключить', width=10, height=2, command=lambda: setDateTimeAtStart_OFF())
but_Off['bg'] = 'red'
but_On['bg'] = 'green'
but_On.place(x=10, y=50)
but_Off.place(x=100, y=50)
root.mainloop()
