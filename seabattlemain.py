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

def make_matrix(height, width):
    matrix = [[' ' for j in range(width)] for i in range(height)]
    for i in range(height):
        matrix[i][0] = '0'
        matrix[i][-1] = '0'
    for j in range(width):
        matrix[0][j] = '0'
        matrix[-1][j] = '0'
    return matrix


def first_chance(matrix, r, c):
    if str(c) in '3456':
        matrix[c] = '1'
        counter = 3
        while counter != 0:
            if matrix[matrix.index('1') - 1] == ' ' and matrix[''.join(matrix).rfind('1') + 1] == ' ':
                to = choice([matrix.index('1') - 1, ''.join(matrix).rfind('1') + 1])
                if matrix[to] != '0':
                    matrix[to] = '1'
                    counter -= 1

    else:
        matrix[c] = '1'
        if c < 3:
            counter = 3
            list1 = []
            while matrix.index('1') - 1 > 0 and matrix[matrix.index('1') - 1] == ' ' and counter != 0:
                to = choice([matrix.index('1') - 1, ''.join(matrix).rindex('1') + 1])
                print(to)
                if abs(to) not in list1:
                    matrix[abs(to)] = '1'
                    counter -= 1
                list1.append(abs(to))
            if counter != 0:
                for i in range(counter):
                    matrix[''.join(matrix).rfind('1') + 1] = '1'
        elif c > 6:
            counter = 3
            list1 = []
            while ''.join(matrix).rindex('1') + 1 < 10 and matrix[''.join(matrix).rindex('1') + 1] == ' ' and counter != 0:
                to = choice([matrix.index('1') - 1, ''.join(matrix).rindex('1') + 1])
                print(to)
                if abs(to) not in list1:
                    matrix[abs(to)] = '1'
                    counter -= 1
                list1.append(abs(to))
            if counter != 0:
                for i in range(counter):
                    matrix[matrix.index('1') - 1] = '1'
    return matrix

def second_chance(matrix, r, c):
    matrix[r][c] = '1'
    list1 = []
    for i in range(12):
        list1.append(matrix[i][c])
    c2 = list1.index('1')
    list1 = first_chance(list1, r, c2)
    for i in range(12):
        matrix[i][c] = list1[i]
    return matrix

def need_button_2():
    global window
    global to_delete_from_first_screen
    buton7 = Button(window, text='Морской бой', font='Arial 18', command=sea_battle)
    buton7.place(x=280, y=200)
    to_delete_from_first_screen.append(buton7)
    return window


def sea_battle():
    global window
    w = 650
    h = 620
    window.geometry(f'{w}x{h}+300+170')

    def on_main_screen():
        global window
        delete_all_to_go_to_first_screen()
        need_button_2()

    btn10 = Button(window, text='На главную страницу', font='Arial 18', bg='blue', fg='white', activebackground='red',
                   activeforeground='white', command=on_main_screen)
    btn10.grid(row=14, column=1, columnspan=10)
    to_delete_all_to_go_first_screen.append(btn10)

    def matrix():
        matrix = make_matrix(12, 12)

        def largest_ship(matrix):
            chance = randint(1, 2)
            if chance == 1:
                r = randint(1, 10)
                c = randint(1, 10)
                matrix[r][c] = '1'
                matrix[r] = first_chance(matrix[r], r, c)
            else:
                r = randint(1, 10)
                c = randint(1, 10)
                print(r, c)
                matrix = second_chance(matrix, r, c)
            return matrix
        matrix = largest_ship(matrix)
        return matrix

    delete_from_fist_screen()
    matrix = matrix()
    print(*matrix, sep = '\n')
    lbln = Label(text='Морской Бой', font='Arial 40', bg='#CC99FF')
    lbln.grid(row=0, column=1, columnspan=10)
    to_delete_all_to_go_first_screen.append(lbln)

    lbl11 = Label(text='1', font='Arial 14', bg='#CC99FF')
    lbl12 = Label(text='2', font='Arial 14', bg='#CC99FF')
    lbl13 = Label(text='3', font='Arial 14', bg='#CC99FF')
    lbl14 = Label(text='4', font='Arial 14', bg='#CC99FF')
    lbl15 = Label(text='5', font='Arial 14', bg='#CC99FF')
    lbl16 = Label(text='6', font='Arial 14', bg='#CC99FF')
    lbl17 = Label(text='7', font='Arial 14', bg='#CC99FF')
    lbl18 = Label(text='8', font='Arial 14', bg='#CC99FF')
    lbl19 = Label(text='9', font='Arial 14', bg='#CC99FF')
    lbl20 = Label(text='10', font='Arial 14', bg='#CC99FF')
    lbl11.grid(row=3, column=0)
    lbl12.grid(row=4, column=0)
    lbl13.grid(row=5, column=0)
    lbl14.grid(row=6, column=0)
    lbl15.grid(row=7, column=0)
    lbl16.grid(row=8, column=0)
    lbl17.grid(row=9, column=0)
    lbl18.grid(row=10, column=0)
    lbl19.grid(row=11, column=0)
    lbl20.grid(row=12, column=0)
    to_delete_all_to_go_first_screen.append(lbl11)
    to_delete_all_to_go_first_screen.append(lbl12)
    to_delete_all_to_go_first_screen.append(lbl13)
    to_delete_all_to_go_first_screen.append(lbl14)
    to_delete_all_to_go_first_screen.append(lbl15)
    to_delete_all_to_go_first_screen.append(lbl16)
    to_delete_all_to_go_first_screen.append(lbl17)
    to_delete_all_to_go_first_screen.append(lbl18)
    to_delete_all_to_go_first_screen.append(lbl19)
    to_delete_all_to_go_first_screen.append(lbl20)

    list5 = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
    lbl1 = Label(text=list5[0], font='Arial 18', bg='#CC99FF')
    lbl2 = Label(text=list5[1], font='Arial 18', bg='#CC99FF')
    lbl3 = Label(text=list5[2], font='Arial 18', bg='#CC99FF')
    lbl4 = Label(text=list5[3], font='Arial 18', bg='#CC99FF')
    lbl5 = Label(text=list5[4], font='Arial 18', bg='#CC99FF')
    lbl6 = Label(text=list5[5], font='Arial 18', bg='#CC99FF')
    lbl7 = Label(text=list5[6], font='Arial 18', bg='#CC99FF')
    lbl8 = Label(text=list5[7], font='Arial 18', bg='#CC99FF')
    lbl9 = Label(text=list5[8], font='Arial 18', bg='#CC99FF')
    lbl10 = Label(text=list5[9], font='Arial 18', bg='#CC99FF')
    lbl1.grid(row=1, column=2)
    lbl2.grid(row=1, column=3)
    lbl3.grid(row=1, column=4)
    lbl4.grid(row=1, column=5)
    lbl5.grid(row=1, column=6)
    lbl6.grid(row=1, column=7)
    lbl7.grid(row=1, column=8)
    lbl8.grid(row=1, column=9)
    lbl9.grid(row=1, column=10)
    lbl10.grid(row=1, column=11)
    to_delete_all_to_go_first_screen.append(lbl1)
    to_delete_all_to_go_first_screen.append(lbl2)
    to_delete_all_to_go_first_screen.append(lbl3)
    to_delete_all_to_go_first_screen.append(lbl4)
    to_delete_all_to_go_first_screen.append(lbl5)
    to_delete_all_to_go_first_screen.append(lbl6)
    to_delete_all_to_go_first_screen.append(lbl7)
    to_delete_all_to_go_first_screen.append(lbl8)
    to_delete_all_to_go_first_screen.append(lbl9)
    to_delete_all_to_go_first_screen.append(lbl10)
    button00 = Button(text=matrix[0][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button00.grid(row=(0 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button00)
    button01 = Button(text=matrix[0][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button01.grid(row=(0 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button01)
    button02 = Button(text=matrix[0][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button02.grid(row=(0 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button02)
    button03 = Button(text=matrix[0][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button03.grid(row=(0 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button03)
    button04 = Button(text=matrix[0][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button04.grid(row=(0 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button04)
    button05 = Button(text=matrix[0][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button05.grid(row=(0 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button05)
    button06 = Button(text=matrix[0][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button06.grid(row=(0 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button06)
    button07 = Button(text=matrix[0][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button07.grid(row=(0 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button07)
    button08 = Button(text=matrix[0][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button08.grid(row=(0 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button08)
    button09 = Button(text=matrix[0][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button09.grid(row=(0 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button09)
    button010 = Button(text=matrix[0][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button010.grid(row=(0 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button010)
    button011 = Button(text=matrix[0][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button011.grid(row=(0 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button011)
    button10 = Button(text=matrix[1][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button10.grid(row=(1 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button10)
    button11 = Button(text=matrix[1][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button11.grid(row=(1 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button11)
    button12 = Button(text=matrix[1][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button12.grid(row=(1 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button12)
    button13 = Button(text=matrix[1][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button13.grid(row=(1 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button13)
    button14 = Button(text=matrix[1][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button14.grid(row=(1 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button14)
    button15 = Button(text=matrix[1][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button15.grid(row=(1 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button15)
    button16 = Button(text=matrix[1][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button16.grid(row=(1 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button16)
    button17 = Button(text=matrix[1][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button17.grid(row=(1 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button17)
    button18 = Button(text=matrix[1][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button18.grid(row=(1 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button18)
    button19 = Button(text=matrix[1][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button19.grid(row=(1 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button19)
    button110 = Button(text=matrix[1][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button110.grid(row=(1 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button110)
    button111 = Button(text=matrix[1][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button111.grid(row=(1 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button111)
    button20 = Button(text=matrix[2][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button20.grid(row=(2 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button20)
    button21 = Button(text=matrix[2][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button21.grid(row=(2 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button21)
    button22 = Button(text=matrix[2][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button22.grid(row=(2 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button22)
    button23 = Button(text=matrix[2][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button23.grid(row=(2 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button23)
    button24 = Button(text=matrix[2][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button24.grid(row=(2 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button24)
    button25 = Button(text=matrix[2][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button25.grid(row=(2 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button25)
    button26 = Button(text=matrix[2][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button26.grid(row=(2 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button26)
    button27 = Button(text=matrix[2][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button27.grid(row=(2 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button27)
    button28 = Button(text=matrix[2][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button28.grid(row=(2 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button28)
    button29 = Button(text=matrix[2][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button29.grid(row=(2 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button29)
    button210 = Button(text=matrix[2][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button210.grid(row=(2 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button210)
    button211 = Button(text=matrix[2][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button211.grid(row=(2 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button211)
    button30 = Button(text=matrix[3][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button30.grid(row=(3 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button30)
    button31 = Button(text=matrix[3][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button31.grid(row=(3 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button31)
    button32 = Button(text=matrix[3][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button32.grid(row=(3 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button32)
    button33 = Button(text=matrix[3][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button33.grid(row=(3 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button33)
    button34 = Button(text=matrix[3][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button34.grid(row=(3 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button34)
    button35 = Button(text=matrix[3][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button35.grid(row=(3 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button35)
    button36 = Button(text=matrix[3][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button36.grid(row=(3 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button36)
    button37 = Button(text=matrix[3][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button37.grid(row=(3 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button37)
    button38 = Button(text=matrix[3][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button38.grid(row=(3 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button38)
    button39 = Button(text=matrix[3][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button39.grid(row=(3 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button39)
    button310 = Button(text=matrix[3][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button310.grid(row=(3 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button310)
    button311 = Button(text=matrix[3][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button311.grid(row=(3 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button311)
    button40 = Button(text=matrix[4][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button40.grid(row=(4 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button40)
    button41 = Button(text=matrix[4][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button41.grid(row=(4 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button41)
    button42 = Button(text=matrix[4][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button42.grid(row=(4 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button42)
    button43 = Button(text=matrix[4][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button43.grid(row=(4 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button43)
    button44 = Button(text=matrix[4][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button44.grid(row=(4 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button44)
    button45 = Button(text=matrix[4][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button45.grid(row=(4 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button45)
    button46 = Button(text=matrix[4][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button46.grid(row=(4 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button46)
    button47 = Button(text=matrix[4][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button47.grid(row=(4 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button47)
    button48 = Button(text=matrix[4][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button48.grid(row=(4 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button48)
    button49 = Button(text=matrix[4][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button49.grid(row=(4 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button49)
    button410 = Button(text=matrix[4][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button410.grid(row=(4 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button410)
    button411 = Button(text=matrix[4][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button411.grid(row=(4 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button411)
    button50 = Button(text=matrix[5][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button50.grid(row=(5 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button50)
    button51 = Button(text=matrix[5][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button51.grid(row=(5 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button51)
    button52 = Button(text=matrix[5][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button52.grid(row=(5 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button52)
    button53 = Button(text=matrix[5][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button53.grid(row=(5 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button53)
    button54 = Button(text=matrix[5][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button54.grid(row=(5 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button54)
    button55 = Button(text=matrix[5][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button55.grid(row=(5 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button55)
    button56 = Button(text=matrix[5][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button56.grid(row=(5 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button56)
    button57 = Button(text=matrix[5][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button57.grid(row=(5 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button57)
    button58 = Button(text=matrix[5][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button58.grid(row=(5 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button58)
    button59 = Button(text=matrix[5][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button59.grid(row=(5 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button59)
    button510 = Button(text=matrix[5][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button510.grid(row=(5 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button510)
    button511 = Button(text=matrix[5][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button511.grid(row=(5 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button511)
    button60 = Button(text=matrix[6][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button60.grid(row=(6 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button60)
    button61 = Button(text=matrix[6][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button61.grid(row=(6 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button61)
    button62 = Button(text=matrix[6][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button62.grid(row=(6 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button62)
    button63 = Button(text=matrix[6][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button63.grid(row=(6 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button63)
    button64 = Button(text=matrix[6][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button64.grid(row=(6 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button64)
    button65 = Button(text=matrix[6][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button65.grid(row=(6 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button65)
    button66 = Button(text=matrix[6][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button66.grid(row=(6 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button66)
    button67 = Button(text=matrix[6][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button67.grid(row=(6 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button67)
    button68 = Button(text=matrix[6][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button68.grid(row=(6 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button68)
    button69 = Button(text=matrix[6][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button69.grid(row=(6 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button69)
    button610 = Button(text=matrix[6][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button610.grid(row=(6 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button610)
    button611 = Button(text=matrix[6][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button611.grid(row=(6 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button611)
    button70 = Button(text=matrix[7][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button70.grid(row=(7 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button70)
    button71 = Button(text=matrix[7][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button71.grid(row=(7 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button71)
    button72 = Button(text=matrix[7][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button72.grid(row=(7 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button72)
    button73 = Button(text=matrix[7][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button73.grid(row=(7 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button73)
    button74 = Button(text=matrix[7][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button74.grid(row=(7 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button74)
    button75 = Button(text=matrix[7][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button75.grid(row=(7 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button75)
    button76 = Button(text=matrix[7][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button76.grid(row=(7 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button76)
    button77 = Button(text=matrix[7][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button77.grid(row=(7 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button77)
    button78 = Button(text=matrix[7][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button78.grid(row=(7 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button78)
    button79 = Button(text=matrix[7][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button79.grid(row=(7 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button79)
    button710 = Button(text=matrix[7][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button710.grid(row=(7 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button710)
    button711 = Button(text=matrix[7][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button711.grid(row=(7 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button711)
    button80 = Button(text=matrix[8][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button80.grid(row=(8 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button80)
    button81 = Button(text=matrix[8][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button81.grid(row=(8 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button81)
    button82 = Button(text=matrix[8][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button82.grid(row=(8 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button82)
    button83 = Button(text=matrix[8][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button83.grid(row=(8 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button83)
    button84 = Button(text=matrix[8][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button84.grid(row=(8 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button84)
    button85 = Button(text=matrix[8][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button85.grid(row=(8 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button85)
    button86 = Button(text=matrix[8][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button86.grid(row=(8 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button86)
    button87 = Button(text=matrix[8][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button87.grid(row=(8 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button87)
    button88 = Button(text=matrix[8][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button88.grid(row=(8 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button88)
    button89 = Button(text=matrix[8][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button89.grid(row=(8 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button89)
    button810 = Button(text=matrix[8][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button810.grid(row=(8 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button810)
    button811 = Button(text=matrix[8][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button811.grid(row=(8 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button811)
    button90 = Button(text=matrix[9][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button90.grid(row=(9 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button90)
    button91 = Button(text=matrix[9][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button91.grid(row=(9 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button91)
    button92 = Button(text=matrix[9][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button92.grid(row=(9 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button92)
    button93 = Button(text=matrix[9][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button93.grid(row=(9 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button93)
    button94 = Button(text=matrix[9][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button94.grid(row=(9 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button94)
    button95 = Button(text=matrix[9][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button95.grid(row=(9 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button95)
    button96 = Button(text=matrix[9][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button96.grid(row=(9 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button96)
    button97 = Button(text=matrix[9][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button97.grid(row=(9 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button97)
    button98 = Button(text=matrix[9][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button98.grid(row=(9 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button98)
    button99 = Button(text=matrix[9][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button99.grid(row=(9 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button99)
    button910 = Button(text=matrix[9][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button910.grid(row=(9 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button910)
    button911 = Button(text=matrix[9][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button911.grid(row=(9 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button911)
    button100 = Button(text=matrix[10][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button100.grid(row=(10 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button100)
    button101 = Button(text=matrix[10][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button101.grid(row=(10 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button101)
    button102 = Button(text=matrix[10][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button102.grid(row=(10 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button102)
    button103 = Button(text=matrix[10][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button103.grid(row=(10 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button103)
    button104 = Button(text=matrix[10][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button104.grid(row=(10 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button104)
    button105 = Button(text=matrix[10][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button105.grid(row=(10 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button105)
    button106 = Button(text=matrix[10][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button106.grid(row=(10 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button106)
    button107 = Button(text=matrix[10][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button107.grid(row=(10 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button107)
    button108 = Button(text=matrix[10][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button108.grid(row=(10 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button108)
    button109 = Button(text=matrix[10][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button109.grid(row=(10 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button109)
    button1010 = Button(text=matrix[10][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button1010.grid(row=(10 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button1010)
    button1011 = Button(text=matrix[10][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button1011.grid(row=(10 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button1011)
    button110 = Button(text=matrix[11][0], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button110.grid(row=(11 + 2), column=(0 + 1))
    to_delete_all_to_go_first_screen.append(button110)
    button111 = Button(text=matrix[11][1], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button111.grid(row=(11 + 2), column=(1 + 1))
    to_delete_all_to_go_first_screen.append(button111)
    button112 = Button(text=matrix[11][2], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button112.grid(row=(11 + 2), column=(2 + 1))
    to_delete_all_to_go_first_screen.append(button112)
    button113 = Button(text=matrix[11][3], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button113.grid(row=(11 + 2), column=(3 + 1))
    to_delete_all_to_go_first_screen.append(button113)
    button114 = Button(text=matrix[11][4], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button114.grid(row=(11 + 2), column=(4 + 1))
    to_delete_all_to_go_first_screen.append(button114)
    button115 = Button(text=matrix[11][5], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button115.grid(row=(11 + 2), column=(5 + 1))
    to_delete_all_to_go_first_screen.append(button115)
    button116 = Button(text=matrix[11][6], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button116.grid(row=(11 + 2), column=(6 + 1))
    to_delete_all_to_go_first_screen.append(button116)
    button117 = Button(text=matrix[11][7], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button117.grid(row=(11 + 2), column=(7 + 1))
    to_delete_all_to_go_first_screen.append(button117)
    button118 = Button(text=matrix[11][8], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button118.grid(row=(11 + 2), column=(8 + 1))
    to_delete_all_to_go_first_screen.append(button118)
    button119 = Button(text=matrix[11][9], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button119.grid(row=(11 + 2), column=(9 + 1))
    to_delete_all_to_go_first_screen.append(button119)
    button1110 = Button(text=matrix[11][10], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button1110.grid(row=(11 + 2), column=(10 + 1))
    to_delete_all_to_go_first_screen.append(button1110)
    button1111 = Button(text=matrix[11][11], font="Arial 11", width=3, bd=5, bg="grey", activebackground='green')
    button1111.grid(row=(11 + 2), column=(11 + 1))
    to_delete_all_to_go_first_screen.append(button1111)

    return window


def first_screen():
    global window
    window.title('Калькулятор ВиС')
    window.geometry('610x600+300+170')
    window.configure(bg='#CC99FF')
    photo = PhotoImage(file='new.png')
    window.iconphoto(False, photo)
    window.resizable(False, False)
    window = need_button_2()
    return window


window = first_screen()
window.mainloop()
