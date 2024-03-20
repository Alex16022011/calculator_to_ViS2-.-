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


list_to_insert = ['0']


def first_chance(matrix, r, c, lenght, to_insert):
    if str(c) in '3456':
        counter = lenght - 1
        while counter != 0:
            if matrix[matrix.index(to_insert) - 1] == ' ' and matrix[''.join(matrix).rfind(to_insert) + 1] == ' ':
                to = choice([matrix.index(to_insert) - 1, ''.join(matrix).rfind(to_insert) + 1])
                if matrix[to] not in list_to_insert:
                    matrix[to] = to_insert
                    counter -= 1

    else:
        if c < 3:
            counter = lenght - 1
            list1 = []
            while matrix.index(to_insert) - 1 > 0 and matrix[matrix.index(to_insert) - 1] == ' ' and counter != 0:
                to = choice([matrix.index(to_insert) - 1, ''.join(matrix).rindex(to_insert) + 1])
                print(to)
                if abs(to) not in list1:
                    matrix[abs(to)] = to_insert
                    counter -= 1
                list1.append(abs(to))
            if counter != 0:
                for i in range(counter):
                    matrix[''.join(matrix).rfind(to_insert) + 1] = to_insert
        elif c > 6:
            counter = lenght - 1
            list1 = []
            while ''.join(matrix).rindex(to_insert) + 1 < 10 and matrix[''.join(matrix).rindex(to_insert) + 1] == ' ' and counter != 0:
                to = choice([matrix.index(to_insert) - 1, ''.join(matrix).rindex(to_insert) + 1])
                print(to)
                if abs(to) not in list1:
                    matrix[abs(to)] = to_insert
                    counter -= 1
                list1.append(abs(to))
            if counter != 0:
                for i in range(counter):
                    matrix[matrix.index(to_insert) - 1] = to_insert
    return matrix


def second_chance(matrix, r, c, lenght, to_insert):
    list1 = []
    for i in range(12):
        list1.append(matrix[i][c])
    c2 = list1.index(to_insert)
    list1 = first_chance(list1, r, c2, lenght, to_insert)
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


def limitation1(matrix, r, c, first_or_second, to_insert):
    if first_or_second == 'first':
        a = matrix[r].index(to_insert) - 1
        b = ''.join(matrix[r]).rfind(to_insert) + 1
        matrix[r][a] = '0'
        matrix[r][b] = '0'
        for i in range(a, b + 1):
            matrix[r - 1][i] = '0'
            matrix[r + 1][i] = '0'
    elif first_or_second == 'second':
        a = matrix[c].index(to_insert) - 1
        b = ''.join(matrix[c]).rfind(to_insert) + 1
        matrix[c][a] = '0'
        matrix[c][b] = '0'
        for i in range(a, b + 1):
            matrix[c - 1][i] = '0'
            matrix[c + 1][i] = '0'
    return matrix


def limitation2(matrix, r, c, to_insert):
    matrix2 = []
    for i in range(12):
        listnd = []
        for j in range(12):
            listnd.append(matrix[j][i])
        listnd = listnd[::-1]
        matrix2.append(listnd)
    print(matrix2)
    first_or_second = 'second'
    matrix2 = limitation1(matrix2, r, c, first_or_second, to_insert)
    matrix3 = []
    for i in range(12):
        listnd2 = []
        for j in range(12):
            listnd2.append(matrix2[j][i])
        matrix3.append(listnd2)
    matrix = matrix3
    matrix = matrix[::-1]
    return matrix


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

        def fourth_ship(matrix, to_insert):
            chance = randint(1, 2)
            r = randint(1, 10)
            c = randint(1, 10)
            lenght = 4
            print(f'r = {r}, c = {c}, chance = {chance}')
            matrix[r][c] = to_insert
            if chance == 1:
                matrix[r] = first_chance(matrix[r], r, c, lenght, to_insert)
                first_or_second = 'first'
                matrix = limitation1(matrix, r, c, first_or_second, to_insert)
            else:
                matrix = second_chance(matrix, r, c, lenght, to_insert)
                matrix = limitation2(matrix, r, c, to_insert)
            return matrix

        def third_ship(matrix, to_insert):
            r = randint(1, 10)
            c = randint(1, 10)
            lenght = 3
            while matrix[r][c] != ' ':
                r = randint(1, 10)
                c = randint(1, 10)
            matrix[r][c] = to_insert
            # if matrix[r][c + 1] == ' ' and matrix[r][c + 2] == ' ' and matrix[r][c - 1] == ' ' and matrix[r][c - 2] == ' ' and matrix[r + 1][c] == ' ' and matrix[r + 2][c] == ' ' and matrix[r - 1][c] == ' ' and matrix[r - 2][c] == ' ':
            chance = randint(1, 2)
            if chance == 1:
                matrix[r] = first_chance(matrix[r], r, c, lenght, to_insert)
                first_or_second = 'first'
                matrix = limitation1(matrix, r, c, first_or_second, to_insert)
            elif chance == 2:
                matrix = second_chance(matrix, r, c, lenght, to_insert)
                matrix = limitation2(matrix, r, c, to_insert)
            return matrix

        def second_ship(matrix, to_insert):
            r = randint(1, 10)
            c = randint(1, 10)
            lenght = 2
            while matrix[r][c] != ' ':
                r = randint(1, 10)
                c = randint(1, 10)
            matrix[r][c] = to_insert
            # if matrix[r][c + 1] == ' ' and matrix[r][c + 2] == ' ' and matrix[r][c - 1] == ' ' and matrix[r][c - 2] == ' ' and matrix[r + 1][c] == ' ' and matrix[r + 2][c] == ' ' and matrix[r - 1][c] == ' ' and matrix[r - 2][c] == ' ':
            chance = randint(1, 2)
            if chance == 1:
                matrix[r] = first_chance(matrix[r], r, c, lenght, to_insert)
                first_or_second = 'first'
                matrix = limitation1(matrix, r, c, first_or_second, to_insert)
            elif chance == 2:
                matrix = second_chance(matrix, r, c, lenght, to_insert)
                matrix = limitation2(matrix, r, c, to_insert)
            # else:
            #     if ...:
            #         pass
            #     elif ...:
            #         pass
            return matrix


        def first_ship(matrix, to_insert):
            r = randint(1, 10)
            c = randint(1, 10)
            lenght = 1
            while matrix[r][c] != ' ':
                r = randint(1, 10)
                c = randint(1, 10)
            matrix[r][c] = to_insert
            # if matrix[r][c + 1] == ' ' and matrix[r][c + 2] == ' ' and matrix[r][c - 1] == ' ' and matrix[r][c - 2] == ' ' and matrix[r + 1][c] == ' ' and matrix[r + 2][c] == ' ' and matrix[r - 1][c] == ' ' and matrix[r - 2][c] == ' ':
            chance = randint(1, 2)
            if chance == 1:
                matrix[r] = first_chance(matrix[r], r, c, lenght, to_insert)
                first_or_second = 'first'
                matrix = limitation1(matrix, r, c, first_or_second, to_insert)
            elif chance == 2:
                matrix = second_chance(matrix, r, c, lenght, to_insert)
                matrix = limitation2(matrix, r, c, to_insert)
            # else:
            #     if ...:
            #         pass
            #     elif ...:
            #         pass
            return matrix

        matrix = fourth_ship(matrix, '1')
        list_to_insert.append('1')

        matrix = third_ship(matrix, '2')
        list_to_insert.append('2')
        matrix = third_ship(matrix, '3')
        list_to_insert.append('3')

        matrix = second_ship(matrix, '4')
        list_to_insert.append('4')
        matrix = second_ship(matrix, '5')
        list_to_insert.append('5')
        matrix = second_ship(matrix, '6')
        list_to_insert.append('6')

        matrix = first_ship(matrix, '7')
        list_to_insert.append('7')
        matrix = first_ship(matrix, '8')
        list_to_insert.append('8')
        matrix = first_ship(matrix, '9')
        list_to_insert.append('9')
        matrix = first_ship(matrix, '10')
        list_to_insert.append('10')

        return matrix

    delete_from_fist_screen()
    matrix = matrix()
    print(*matrix, sep = '\n')
    lbln = Label(text='Морской Бой', font='Arial 40', bg='#CC99FF')
    lbln.grid(row=0, column=1, columnspan=10)
    to_delete_all_to_go_first_screen.append(lbln)

    for i in range(12):
        for j in range(12):
            exec(f'''button{i}{j} = Button(text=matrix[{i}][{j}], font=\"Arial 11\", width=3, bd=5, bg=\"grey\", activebackground='green')
button{i}{j}.grid(row=({i + 2}), column=({j + 1}), padx=1, pady=1)
to_delete_all_to_go_first_screen.append(button{i}{j})''')
    for i in range(1, 3):
        for j in range(1, 11):
            exec(f'''lbl{i}{j} = Label(text='{j}', font='Arial 14', bg='#CC99FF')
lbl{i}{j}.grid(row={j + 2}, column=0)
to_delete_all_to_go_first_screen.append(lbl{i}{j})''')

    list5 = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
    for i in range(1, 11):
        exec(f'''lbl{i} = Label(text=list5[{i - 1}], font='Arial 18', bg='#CC99FF')
lbl{i}.grid(row=1, column={i + 1})
to_delete_all_to_go_first_screen.append(lbl{i})''')

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