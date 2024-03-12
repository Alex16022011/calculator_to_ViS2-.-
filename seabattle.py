from tkinter import *

from random import *

from tkinter import ttk

from math import *

to_delete_from_first_screen = []
to_delete_from_screen_ViS_when_you_tap_the_button = []
to_delete_from_screen_ViS_when_you_tap_the_answer = []
to_delete_all_to_go_first_screen = []

def delete_from_fist_screen():
    global window
    global to_delete_from_first_screen
    if len(to_delete_from_first_screen) > 0:
        for i in to_delete_from_first_screen:
            i.destroy()
        to_delete_from_first_screen = []
    return window


def delete_from_screen_ViS_when_you_tap_the_button():
    global window
    global to_delete_from_screen_ViS_when_you_tap_the_button
    if len(to_delete_from_screen_ViS_when_you_tap_the_button) > 0:
        for i in to_delete_from_screen_ViS_when_you_tap_the_button:
            i.destroy()
        to_delete_from_screen_ViS_when_you_tap_the_button = []
    return window


def delete_from_screen_ViS_when_you_tap_answer():
    global window
    global to_delete_from_screen_ViS_when_you_tap_the_answer
    if len(to_delete_from_screen_ViS_when_you_tap_the_answer) > 0:
        for i in to_delete_from_screen_ViS_when_you_tap_the_answer:
            i.destroy()
        to_delete_from_screen_ViS_when_you_tap_the_answer = []
    return window


def delete_all_to_go_to_first_screen():
    global window
    global to_delete_all_to_go_first_screen
    if len(to_delete_all_to_go_first_screen) > 0:
        for i in to_delete_all_to_go_first_screen:
            i.destroy()
        to_delete_all_to_go_first_screen = []
    return window

c = 0

window = Tk()


def need_button_2():
    global window
    global to_delete_from_first_screen
    buton7 = Button(window, text='Морской бой', font='Arial 18', command=sea_battle)
    buton7.place(x=280, y=200)
    to_delete_from_first_screen.append(buton7)
    return window


def sea_battle():

    def matrix():
        matrix = [[' ' for j in range(8)] for i in range(8)]
        matrix2 = [[' ' for j in range(8)] for i in range(8)]
        # counter = 4
        # while counter != 0:
        #     f = randint(0, 7)
        #     d = randint(0, 7)
        #     if matrix2[f][d] != 'q' and matrix2[f][d] != '*':
        #         matrix2[f][d] = '*'
        #         if 0 < d < 7:
        #             matrix2[f][d + 1] = 'q'
        #             matrix2[f][d - 1] = 'q'
        #         if 0 < f < 7:
        #             matrix2[f + 1][d] = 'q'
        #             matrix2[f - 1][d] = 'q'
        #         counter -= 1

        counter2 = 3
        while counter2 != 0:
            f = randint(0, 7)
            d = randint(0, 7)
            f2 = randint(0, 7)
            d2 = randint(0, 7)
            if matrix2[f][d] != 'q' and matrix2[f][d] != '*' and (abs(f2 - f) == 1 and abs(d2 - d) == 0) or (abs(f2 - f) == 0 and abs(d2 - d) == 1):
                matrix2[f][d] = 't'
                matrix2[f2][d2] = 't1'
                if 0 < d < 7:
                    matrix2[f][d + 1] = 'q'
                    matrix2[f][d - 1] = 'q'
                if 0 < f < 7:
                    matrix2[f + 1][d] = 'q'
                    matrix2[f - 1][d] = 'q'
                if 1 < d2 < 6:
                    matrix2[f2][d2 + 2] = 'q'
                    matrix2[f2][d2 - 2] = 'q'
                if 1 < f2 < 6:
                    matrix2[f2 + 2][d2] = 'q'
                    matrix2[f2 - 2][d2] = 'q'
                counter2 -= 1
        return matrix2

    delete_from_fist_screen()
    matrix = matrix()
    print(*matrix, sep='\n')
    lbln = Label(text='Морской Бой', font='Arial 40', bg='#CC99FF')
    lbln.grid(row=0, column=1, columnspan=8)
    for i in range(8):
        for j in range(8):
            Button(text=matrix[i][j], font='Arial 19', width=4, bd=5, bg='grey', activebackground='green').grid(row=(i + 1), column=(j + 1), padx=1, pady=1)
    return window


def first_screen():
    global window
    window.title('Калькулятор ВиС')
    window.geometry('630x600+300+170')
    window.configure(bg='#CC99FF')
    photo = PhotoImage(file='new.png')
    window.iconphoto(False, photo)
    window.resizable(False, False)
    window = need_button_2()
    return window


window = first_screen()
window.mainloop()
