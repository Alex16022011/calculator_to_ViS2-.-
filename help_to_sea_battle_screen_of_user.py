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


def make_matrix2(height, width):
    matrix = [[' ' for j in range(width)] for i in range(height)]
    return matrix


def need_button_2():
    global window
    global to_delete_from_first_screen
    buton7 = Button(window, text='Морской бой', font='Arial 18', command=sea_battle)
    buton7.place(x=280, y=200)
    to_delete_from_first_screen.append(buton7)
    return window


list_to_append_stroka = []


def config_color(i, j, stroka):
    global to_do
    global list_to_append_stroka
    if matrix_user[i][j] in ' 1':
        to_do = 1
        if str(stroka) not in list_to_append_stroka:
            to_do = 0
            list_to_append_stroka.append(str(stroka))
        else:
            to_do = 1
        if to_do == 0:
            exec(f'button{i}{j}.config(bg="red")')
            matrix_user[i][j] = '1'
            matrix_user[i - 1][j - 1] = '0'
            matrix_user[i + 1][j - 1] = '0'
            matrix_user[i - 1][j + 1] = '0'
            matrix_user[i + 1][j + 1] = '0'
            to_do = 1
        else:
            exec(f'button{i}{j}.config(bg="grey")')
            matrix_user[i][j] = ' '
            matrix_user[i - 1][j - 1] = ' '
            matrix_user[i + 1][j - 1] = ' '
            matrix_user[i - 1][j + 1] = ' '
            matrix_user[i + 1][j + 1] = ' '
            to_do = 0
            del list_to_append_stroka[list_to_append_stroka.index(stroka)]
        print()
        print(*matrix_user, sep='\n')
        return matrix_user


to_do = 0


def fourth_ship():
    fourth = 0


def third_ship():
    third = 0


def second_ship():
    second = 0


def first_ship():
    first = 0


def sea_battle():
    global window
    global matrix_user
    w = 610
    h = 620
    window.geometry(f'{w}x{h}+300+70')
    matrix_user = make_matrix2(12, 12)

    def on_main_screen():
        global window
        delete_all_to_go_to_first_screen()
        need_button_2()

    btn1000 = Button(window, text='На главную страницу', font='Arial 18', bg='blue', fg='white', activebackground='red',
                   activeforeground='white', command=on_main_screen)
    btn1000.grid(row=18, column=1, columnspan=10)
    to_delete_all_to_go_first_screen.append(btn1000)
    delete_from_fist_screen()
    print(*matrix_user, sep = '\n')
    lbln = Label(text='Морской Бой', font='Arial 40', bg='#CC99FF')
    lbln.grid(row=0, column=1, columnspan=10)
    to_delete_all_to_go_first_screen.append(lbln)


    btn_clear_all = Button(text='Очистить поле', font='Arial 20')
    btn_clear_all.grid(row=12, column=3, columnspan=6)

    for i in range(1, 11):
        for j in range(1, 11):
            exec(f'''global button{i}{j}
button{i}{j} = Button(text=matrix_user[{i}][{j}], font=\"Arial 11\", width=3, bd=5, bg=\"grey\", activebackground='green', command= lambda: config_color({i}, {j}, 'btn{i}{j}'))
button{i}{j}.grid(row=({i + 1}), column=({j}), padx=1, pady=1)
to_delete_all_to_go_first_screen.append(button{i}{j})''')

    for i in range(1, 3):
        for j in range(1, 11):
            exec(f'''lbl{i}{j} = Label(text='{j}', font='Arial 14', bg='#CC99FF')
lbl{i}{j}.grid(row={j + 1}, column=0)
to_delete_all_to_go_first_screen.append(lbl{i}{j})''')

    list5 = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
    for i in range(1, 11):
        exec(f'''lbl{i} = Label(text=list5[{i - 1}], font='Arial 18', bg='#CC99FF')
lbl{i}.grid(row=1, column={i})
to_delete_all_to_go_first_screen.append(lbl{i})''')

    # btn_ship4 = Button(text='Четырехпалубный', font='Arial 18')
    # btn_ship3 = Button(text='Трехпалубный', font='Arial 18')
    # btn_ship2 = Button(text='Двухпалубный', font='Arial 18')
    # btn_ship1 = Button(text='Однопалубный', font='Arial 18')
    #
    # btn_ship4.grid(row=14, column=5, columnspan=5)
    # btn_ship3.grid(row=15, column=5, columnspan=5)
    # btn_ship2.grid(row=16, column=5, columnspan=5)
    # btn_ship1.grid(row=17, column=5, columnspan=5)
    #
    # to_delete_all_to_go_first_screen.append(btn_ship1)
    # to_delete_all_to_go_first_screen.append(btn_ship2)
    # to_delete_all_to_go_first_screen.append(btn_ship3)
    # to_delete_all_to_go_first_screen.append(btn_ship4)
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