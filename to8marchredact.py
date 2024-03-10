from tkinter import *

from tkinter import ttk

from math import *

# — минус

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
    buton5 = Button(window, text='Калькулятор для ВиС', font='Arial 18', command=calculator_to_ViS)
    buton5.place(x=20, y=200)
    to_delete_from_first_screen.append(buton5)
    buton6 = Button(window, text='Калькулятор', font='Arial 18')
    buton6.place(x=300, y=200)
    to_delete_from_first_screen.append(buton6)
    buton7 = Button(window, text='Сапер', font='Arial 18')
    buton7.place(x=480, y=200)
    to_delete_from_first_screen.append(buton7)
    return window


def calculator_to_ViS():
    window = delete_from_fist_screen()

    def delete_text():
        name.delete(len(name.get()) - 1)

    def delete_all_text():
        name.delete(0, END)

    def output_of_this_program():
        global to_output

        def answer(to_output2):
            global window
            global to_delete_all_to_go_first_screen
            global to_delete_from_screen_ViS_when_you_tap_the_button
            languages_var = StringVar(value=to_output2)
            listbox = Listbox(listvariable=languages_var, font='Arial 15')
            listbox.pack(side=LEFT, fill=BOTH, expand=1, pady=250, padx=30)

            scrollbar = ttk.Scrollbar(window, orient="horizontal")
            scrollbar = Scrollbar(window, orient='horizontal', command=listbox.xview)
            scrollbar.place(x=5, y=575, width=590, height=20)
            scrollbar2 = Scrollbar(window, orient='vertical', command=listbox.yview)
            scrollbar2.place(x=585, y=5, width=20, height=560)

            listbox["xscrollcommand"] = scrollbar.set
            listbox["yscrollcommand"] = scrollbar2.set

            to_delete_all_to_go_first_screen.append(listbox)
            to_delete_all_to_go_first_screen.append(scrollbar)
            to_delete_all_to_go_first_screen.append(scrollbar2)

            to_delete_from_screen_ViS_when_you_tap_the_button.append(listbox)
            to_delete_from_screen_ViS_when_you_tap_the_button.append(scrollbar)
            to_delete_from_screen_ViS_when_you_tap_the_button.append(scrollbar2)

            to_output2 = []
            return window

        def sort_list(a):
            ye = []
            for q in a:
                if '.' in str(a):
                    ye.append(float(q))
                else:
                    ye.append(int(q))
            ye.sort()
            return ye

        to_output2 = []
        if len(to_output) == 2:
            k = int(name.get())
            n = int(name1.get())
            if c == 2:
                first = ''
                second = ''
                third = ''
                c1 = ''
                myset1 = set()
                myset2 = set()
                for j in range(1, n + 1):
                    c1 += str(j)
                    myset1.add(j)
                    c1 += '*'
                c1 = c1[:-1]
                q = 3
                q += len(c1)
                d = ''
                for z in range(1, n - k + 1):
                    d += str(z)
                    myset2.add(z)
                    d += '*'
                d = d[:-1]
                myset3 = myset1.copy()
                myset1 -= myset2
                myset2 -= myset3
                first += c1
                first += '   '
                second += '-' * (len(c1) + (len(d) // 2))
                second += ' = '
                third += d
                third += ' ' * (len(c1) - len(d) + 3)
                a = ''
                for i in myset1:
                    a += str(i)
                    a += '*'
                a = a[:-1]
                first += a
                first += '   '
                second += '-' * len(a)
                second += ' = '
                if len(myset2) == 0:
                    third += ' ' * (len(a) // 2)
                    third += '1'
                    third += ' ' * (len(a) // 2)
                elif len(myset2) > 0:
                    q = ''
                    for i in myset2:
                        q += str(i)
                        q += '*'
                    q = q[:-1]
                    third += q
                m = factorial(n) // factorial(n - k)
                second += str(m)
                to_output2.append(first)
                to_output2.append(second)
                to_output2.append(third)
                window = answer(to_output2)
        delete_from_screen_ViS_when_you_tap_answer()

    def new_button():
        global window
        global name2
        global to_delete_all_to_go_first_screen
        global to_delete_from_screen_ViS_when_you_tap_the_answer
        buton3 = Button(window, text='Решение', height=3, width=10, bg='blue', fg='white',
                        command=output_of_this_program)
        buton3.place(x=230, y=360)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(buton3)
        to_delete_all_to_go_first_screen.append(buton3)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(buton3)
        return window

    def P():
        global window
        global name
        global to_delete_all_to_go_first_screen
        global to_output
        global c
        global to_delete_from_screen_ViS_when_you_tap_the_button
        global to_delete_from_screen_ViS_when_you_tap_the_answer
        c = 3
        delete_from_screen_ViS_when_you_tap_the_button()
        to_output = []
        name = Entry(window, font='Helvetica 15')
        name.place(x=50, y=300, width=500, height=50)
        to_output.append(name)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(name)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(name)
        to_delete_all_to_go_first_screen.append(name)
        lbl3 = Label(window, text='P', font="Helvetica 20", bg='#CC99FF')
        lbl3.place(x=20, y=310)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(lbl3)
        to_delete_all_to_go_first_screen.append(lbl3)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(lbl3)
        lbl4 = Label(window, text='!', font="Helvetica 20", bg='#CC99FF')
        lbl4.place(x=560, y=310)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(lbl4)
        to_delete_all_to_go_first_screen.append(lbl4)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(lbl4)
        window = new_button()
        return window

    def A():
        global window
        global name
        global name1
        global to_delete_all_to_go_first_screen
        global to_delete_from_screen_ViS_when_you_tap_the_button
        global to_delete_from_screen_ViS_when_you_tap_the_answer
        global to_output
        global c
        c = 2
        delete_from_screen_ViS_when_you_tap_the_button()
        to_output = []
        name = Entry(window, font="Helvetica 15")
        to_delete_all_to_go_first_screen.append(name)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(name)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(name)
        name.place(x=80, y=240, width=500, height=50)
        to_output.append(name)
        name1 = Entry(window, font="Helvetica 15")
        to_delete_all_to_go_first_screen.append(name1)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(name1)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(name1)
        name1.place(x=80, y=300, width=500, height=50)
        to_output.append(name1)
        lbl5 = Label(window, text='A', font="Helvetica 50", bg='#CC99FF')
        lbl5.place(x=20, y=265)
        to_delete_all_to_go_first_screen.append(lbl5)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(lbl5)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(lbl5)
        window = new_button()
        return window

    def C():
        global window
        global name
        global name1
        global to_delete_all_to_go_first_screen
        global to_delete_from_screen_ViS_when_you_tap_the_button
        global to_delete_from_screen_ViS_when_you_tap_the_answer
        global to_output
        global c
        c = 1
        delete_from_screen_ViS_when_you_tap_the_button()
        to_output = []
        name = Entry(window, font="Helvetica 15")
        to_delete_all_to_go_first_screen.append(name)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(name)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(name)
        name.place(x=80, y=240, width=500, height=50)
        to_output.append(name)
        name1 = Entry(window, font="Helvetica 15")
        to_delete_all_to_go_first_screen.append(name1)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(name1)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(name1)
        name1.place(x=80, y=300, width=500, height=50)
        to_output.append(name1)
        lbl6 = Label(window, text='C', font="Helvetica 50", bg='#CC99FF')
        lbl6.place(x=20, y=265)
        to_delete_all_to_go_first_screen.append(lbl6)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(lbl6)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(lbl6)
        window = new_button()
        return window

    def work_with_list():
        global window
        global name
        global name2
        global lbl2
        global to_delete_all_to_go_first_screen
        global to_delete_from_screen_ViS_when_you_tap_the_button
        global to_delete_from_screen_ViS_when_you_tap_the_answer
        global to_output
        delete_from_screen_ViS_when_you_tap_the_button()
        to_output = []
        name = Entry(window, font="Helvetica 15")
        to_delete_all_to_go_first_screen.append(name)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(name)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(name)
        to_output.append(name)
        name.place(x=20, y=300, width=550, height=50)
        lbl2 = Label(window, text='Введите список чисел:', font=(30))
        to_delete_all_to_go_first_screen.append(lbl2)
        to_delete_from_screen_ViS_when_you_tap_the_button.append(lbl2)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(lbl2)
        lbl2.place(x=190, y=260)
        window = new_button()
        return window

    def MODA():
        global c
        c = 4
        work_with_list()
        return window

    def counter_of_digits():
        global c
        c = 5
        work_with_list()
        return window

    def sort_list():
        global c
        c = 6
        work_with_list()
        return window

    def MED():
        global c
        c = 7
        work_with_list()
        return window

    def average_arithmetic():
        global c
        c = 8
        work_with_list()
        return window

    def SCOPE():
        global c
        c = 9
        work_with_list()
        return window

    def on_main_screen():
        global window
        delete_all_to_go_to_first_screen()
        need_button_2()

    def new_screen():
        global window
        global to_delete_all_to_go_first_screen
        global to_delete_from_screen_ViS_when_you_tap_the_answer
        btn = Button(window, text='С \nиз \nn по k', font=1, height=3, width=8, activebackground='green',
                     activeforeground='white', borderwidth=10,
                     bg='grey', command=C)
        btn.place(x=10, y=50)
        to_delete_all_to_go_first_screen.append(btn)

        btn2 = Button(window, text='A \nиз \nn по k', font=1, height=3, width=8, activebackground='green',
                      activeforeground='white', borderwidth=10,
                      bg='grey', command=A)
        btn2.place(x=115, y=50)
        to_delete_all_to_go_first_screen.append(btn2)

        btn3 = Button(window, text='Факториал \nчисла', font=1, height=3, width=8, activebackground='green',
                      activeforeground='white', borderwidth=10,
                      bg='grey', command=P)
        btn3.place(x=220, y=50)
        to_delete_all_to_go_first_screen.append(btn3)

        btn4 = Button(window, text='Мода \nстатистического \nряда', font=1, height=3, width=13,
                      activebackground='green', activeforeground='white',
                      borderwidth=10, bg='grey', command=MODA)
        btn4.place(x=325, y=50)
        to_delete_all_to_go_first_screen.append(btn4)

        btn5 = Button(window, text='Количество \nчисел', font=1, height=3, width=9, activebackground='green',
                      activeforeground='white',
                      borderwidth=10, bg='grey', command=counter_of_digits)
        btn5.place(x=475, y=50)
        to_delete_all_to_go_first_screen.append(btn5)

        btn6 = Button(window, text='Отсортировать \nсписок', font=1, height=3, width=12, activebackground='green',
                      activeforeground='white',
                      borderwidth=10, bg='grey', command=sort_list)
        btn6.place(x=20, y=140)
        to_delete_all_to_go_first_screen.append(btn6)

        btn7 = Button(window, text='Медиана \nряда', font=1, height=3, width=12, activebackground='green',
                      activeforeground='white', borderwidth=10,
                      bg='grey', command=MED)
        btn7.place(x=160, y=140)
        to_delete_all_to_go_first_screen.append(btn7)

        btn8 = Button(window, text='Среднее \nарифметическое', font=1, height=3, width=14, activebackground='green',
                      activeforeground='white',
                      borderwidth=10, bg='grey', command=average_arithmetic)
        btn8.place(x=300, y=140)
        to_delete_all_to_go_first_screen.append(btn8)

        btn9 = Button(window, text='Размах \nсписка', font=1, height=3, width=9, activebackground='green',
                      activeforeground='white', borderwidth=10,
                      bg='grey', command=SCOPE)
        btn9.place(x=460, y=140)
        to_delete_all_to_go_first_screen.append(btn9)

        btn10 = Button(window, text='На главную страницу', font='Arial 18', bg='blue', fg='white', activebackground='red',
                       activeforeground='white', command=on_main_screen)
        btn10.place(x=180, y=530)
        to_delete_all_to_go_first_screen.append(btn10)

        return window

    window = new_screen()
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
