from tkinter import *

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
    buton5 = Button(window, text='Калькулятор для ВиС', font='Arial 18', command=calculator_to_ViS)
    buton5.place(x=20, y=200)
    to_delete_from_first_screen.append(buton5)
    buton6 = Button(window, text='Калькулятор', font='Arial 18', command=calculator)
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
            if c == 1:
                need3 = factorial(n) / (factorial(n - k) * factorial(k))
                output1 = ''
                myset1 = set()
                myset2 = set()
                for f in range(1, n + 1):
                    output1 += str(f)
                    output1 += '*'
                    myset1.add(f)
                output1 = output1[:-1]
                output3 = ''
                for w in range(1, n - k + 1):
                    output3 += str(w)
                    output3 += '*'
                    myset2.add(w)
                for y in range(1, k + 1):
                    output3 += str(y)
                    output3 += '*'
                    myset2.add(y)
                myset3 = myset1.copy()
                myset1 -= myset2
                myset2 -= myset3
                a = ''
                b = ''
                for i in myset1:
                    a += str(i)
                    a += '*'
                a = a[:-1]
                for j in myset2:
                    b += str(j)
                    b += '*'
                b = b[:-1]
                output3 = output3[:-1]
                output2 = ''
                output2 += '-' * (len(output1) + len(output3) // 2)
                output2 += ' = '
                output1 += ' ' * 3
                output3 += ' ' * (len(output2) - len(output3))
                output1 += a
                output2 += '--' * (len(a) + len(b) // 2)
                output2 += ' = '
                output2 += str(need3)
                if len(b) > 1:
                    output3 += b
                else:
                    output3 += ' ' * (len(a) // 2)
                    output3 += '1'
                    output3 += ' ' * (len(a) // 2)
                output1 += ' ' * (len(output2) - len(output1))
                output3 += ' ' * (len(output2) - len(output3))
                to_output2.append(output1)
                to_output2.append(output2)
                to_output2.append(output3)
                window = answer(to_output2)
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
        else:
            n = name.get()
            if c == 3:
                cqw = ''
                n = int(n)
                for u in range(1, n + 1):
                    cqw += str(u)
                    cqw += '*'
                cqw = cqw[:-1]
                cqw += ' = '
                cqw += str(factorial(int(n)))
                to_output2.append(cqw)
                window = answer(to_output2)
            if c == 4:
                qw = n.split()
                c3 = []
                counter1 = 2

                co = 0
                for d in range(len(qw)):
                    r = qw.count(qw[d])
                    if r >= counter1:
                        c3.append(qw[d])
                        counter1 = r
                    else:
                        co += 1
                t = []
                for y in range(len(c3)):
                    rt = c3.count(c3[y])
                    if rt >= counter1 and c3[y] not in t:
                        t.append(c3[y])
                        counter1 = rt
                if co == len(qw):
                    to_output2.append('Моды нет')
                else:
                    f = 'Мода списка' + ' ' + ' '.join(qw) + ' = ' + ' '.join(t)
                    to_output2.append(f)
                window = answer(to_output2)
            if c == 5:
                n = n.split()
                counter = []
                numbers = []
                for i in n:
                    if i not in numbers:
                        numbers.append(i)
                numbers.sort()
                for i in numbers:
                    c5 = n.count(i)
                    counter.append(c5)
                print('Число:             Сколько раз встречается:')
                for i in range(len(counter)):
                    print(numbers[i].ljust(10), '='.ljust(10), counter[i])
            if c == 6:
                n = n.split()
                m = sort_list(n)
                print('Упорядоченный ряд: ', *n, ' = ', *m)
            if c == 7:
                qw = n.split()
                b = qw[:]
                dek = sort_list(b)
                b = dek.copy()
                if len(b) % 2 == 0:
                    b = dek[:]
                    for i in dek:
                        dek[dek.index(i)] = str(i)
                    while len(b) != 2:
                        del b[0]
                        del b[-1]
                    c8 = int(b[0]) + int(b[1])
                    t = str(b[0]) + ' + ' + str(b[1])
                    n = ' '.join(qw)
                    m = ' '.join(dek)
                    a = 'Медиана списка  = ' + n + ' = ' + m + ' = '
                    first = second = third = ''
                    second += a
                    first += ' ' * (len(second) + 1)
                    third += ' ' * (len(second) + 1)
                    second += '-' * len(m)
                    first += t
                    third += ' ' * ((len(second) - len(third)) // 2 - 1)
                    third += '2'
                    second += ' = '
                    first += ' ' * (len(second) - len(first))
                    third += ' ' * (len(second) - len(third))
                    second += '-' * len(str(c8))
                    first += str(c8)
                    third += '2'
                    second += ' = '
                    second += str(c8 / 2)
                    first += ' ' * (len(second) - len(first))
                    third += ' ' * (len(second) - len(third))
                    to_output2.append(first)
                    to_output2.append(second)
                    to_output2.append(third)
                elif len(b) % 2 == 1 and len(b) > 2:
                    while len(b) != 1:
                        del b[0]
                        del b[-1]
                    q8 = sorted(qw)
                    to3 = 'Медиана списка = '
                    for i in qw:
                        to3 += str(i)
                        to3 += ' '

                    to3 += '= '
                    for i in q8:
                        to3 += str(i)
                        to3 += ' '

                    to3 += '= '
                    to3 += str(b[0])
                    to_output2.append(to3)
                elif len(b) == 1:
                    to4 = 'Медиана списка  = ' + str(b[0])
                    to_output2.append(to4)
                else:
                    to_output2.append('Медианы нет! Введите еще одно число!')
                window = answer(to_output2)
            if c == 8:
                n = n.split()
                n = sort_list(n)
                numbers2 = n
                first = second = third = ''
                second += 'Среднее арифметическое ряда = '
                first = third = '  ' * 26
                w = '--' * max(len(str(sum(numbers2))), len(str(len(numbers2))))
                second += str(w)
                first += ' '
                third += ' ' * (len(w) // 2)
                first += str(sum(numbers2))
                third += str(len(numbers2))
                second += ' = '
                second += str(sum(numbers2) / len(numbers2))
                second += ' '
                first += ' ' * (len(second) - len(first))
                third += ' ' * (len(second) - len(third))
                to_output2.append(first)
                to_output2.append(second)
                to_output2.append(third)
                window = answer(to_output2)
            if c == 9:
                n = n.split()
                numbers = sort_list(n)
                if len(numbers) > 1:
                    c2 = max(numbers)
                    v = min(numbers)
                    to = 'Размах: ' + str(c2 - v)
                    to_output2.append(to)
                else:
                    to_output2.append('Вы ввели одно число!')
                window = answer(to_output2)
        delete_from_screen_ViS_when_you_tap_answer()

    def new_button():
        global window
        global name2
        global to_delete_all_to_go_first_screen
        global to_delete_from_screen_ViS_when_you_tap_the_answer
        buton = Button(window, text='delete \nlast \ndigit', command=delete_text, height=5, width=10, font=(10))
        buton2 = Button(window, text='delete \nall', command=delete_all_text, height=3, width=5, font=(10))
        buton.place(x=380, y=360)
        to_delete_all_to_go_first_screen.append(buton)
        to_delete_all_to_go_first_screen.append(buton2)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(buton)
        to_delete_from_screen_ViS_when_you_tap_the_answer.append(buton2)
        buton2.place(x=100, y=370)
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
        print(c)
        work_with_list()
        return window

    def counter_of_digits():
        global c
        c = 5
        print(c)
        work_with_list()
        return window

    def sort_list():
        global c
        c = 6
        print(c)
        work_with_list()
        return window

    def MED():
        global c
        c = 7
        print(c)
        work_with_list()
        return window

    def average_arithmetic():
        global c
        c = 8
        print(c)
        work_with_list()
        return window

    def SCOPE():
        global c
        c = 9
        print(c)
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

def calculator():
    global window

    window = delete_from_fist_screen()

    def on_main_screen():
        global window
        delete_all_to_go_to_first_screen()
        need_button_2()

    calc = Entry(window, justify=RIGHT, font='Arial 35', disabledforeground='black')
    calc.insert(0, '0')
    calc['state'] = DISABLED
    calc.grid(row=0, column=0, stick='we', columnspan=4, padx=25, pady=5)
    to_delete_all_to_go_first_screen.append(calc)

    def add_digit(digit):
        value = calc.get()
        if value[0] == '0' and len(value) == 1:
            value = value[1:]
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, value + str(digit))
        calc['state'] = DISABLED

    def calculate():
        value = calc.get()
        if value[-1] in '+-/*':
            value = value + value[:-1]
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, eval(value))
        calc['state'] = DISABLED

    def add_operation(operation):
        value = calc.get()
        if value[-1] in '+-/*':
            value = value[:-1]
        elif '+' in value or '-' in value or '*' in value or '/' in value:
            calculate()
            value = calc.get()
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, value + operation)
        calc['state'] = DISABLED

    def make_digit_button(digit):
        return Button(window, text=digit, font='Arial 35',  bd=5, width=4, command=lambda: add_digit(digit))

    def make_operation_button(operation):
        return Button(window, text=operation, font='Arial 35', bd=5, width=4, command=lambda: add_operation(operation))

    def make_calc_button(operation):
        return Button(window, text=operation,  font='Arial 35', bd=5, width=4, command=calculate)

    def delete_all_text():
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, '0')
        calc['state'] = DISABLED

    def delete_last_digit():
        value = calc.get()
        value = value[:-1]
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, value)
        if len(value) == 0:
            calc.insert(0, '0')
        calc['state'] = DISABLED

    def press_key(event):
        if event.char.isdigit():
            add_digit(event.char)
        elif event.char in '+-*/':
            add_operation(event.char)
        elif event.char == '\r':
            calculate()
        elif event.char == '\x08':
            delete_last_digit()
        else:
            pass

    window.bind('<Key>', press_key)

    btn1 = make_digit_button(1)
    btn2 = make_digit_button(2)
    btn3 = make_digit_button(3)
    btn4 = make_digit_button(4)
    btn5 = make_digit_button(5)
    btn6 = make_digit_button(6)
    btn7 = make_digit_button(7)
    btn8 = make_digit_button(8)
    btn9 = make_digit_button(9)
    btn0 = make_digit_button(0)

    btn1.grid(row=1, column=0, stick='wens', padx=5, pady=5)
    btn2.grid(row=1, column=1, stick='wens', padx=5, pady=5)
    btn3.grid(row=1, column=2, stick='wens', padx=5, pady=5)
    btn4.grid(row=2, column=0, stick='wens', padx=5, pady=5)
    btn5.grid(row=2, column=1, stick='wens', padx=5, pady=5)
    btn6.grid(row=2, column=2, stick='wens', padx=5, pady=5)
    btn7.grid(row=3, column=0, stick='wens', padx=5, pady=5)
    btn8.grid(row=3, column=1, stick='wens', padx=5, pady=5)
    btn9.grid(row=3, column=2, stick='wens', padx=5, pady=5)
    btn0.grid(row=4, column=0, stick='wens', padx=5, pady=5)

    to_delete_all_to_go_first_screen.append(btn1)
    to_delete_all_to_go_first_screen.append(btn2)
    to_delete_all_to_go_first_screen.append(btn3)
    to_delete_all_to_go_first_screen.append(btn4)
    to_delete_all_to_go_first_screen.append(btn5)
    to_delete_all_to_go_first_screen.append(btn6)
    to_delete_all_to_go_first_screen.append(btn7)
    to_delete_all_to_go_first_screen.append(btn8)
    to_delete_all_to_go_first_screen.append(btn9)
    to_delete_all_to_go_first_screen.append(btn0)

    btn10 = make_operation_button('+')
    btn11 = make_operation_button('-')
    btn12 = make_operation_button('/')
    btn13 = make_operation_button('*')

    btn10.grid(row=1, column=3, stick='wens', padx=5, pady=5)
    btn11.grid(row=2, column=3, stick='wens', padx=5, pady=5)
    btn12.grid(row=3, column=3, stick='wens', padx=5, pady=5)
    btn13.grid(row=4, column=3, stick='wens', padx=5, pady=5)

    to_delete_all_to_go_first_screen.append(btn10)
    to_delete_all_to_go_first_screen.append(btn11)
    to_delete_all_to_go_first_screen.append(btn12)
    to_delete_all_to_go_first_screen.append(btn13)

    btn14 = (make_calc_button('='))
    btn14.grid(row=4, column=2, stick='wens', padx=5, pady=5)
    to_delete_all_to_go_first_screen.append(btn14)

    window.grid_columnconfigure(0, minsize=60)
    window.grid_columnconfigure(1, minsize=60)
    window.grid_columnconfigure(2, minsize=60)
    window.grid_columnconfigure(3, minsize=60)

    window.grid_rowconfigure(1, minsize=60)
    window.grid_rowconfigure(2, minsize=60)
    window.grid_rowconfigure(3, minsize=60)
    window.grid_rowconfigure(4, minsize=60)

    ac = Button(window, text='C', font='Arial 35', width=4, bd=5, command=delete_all_text)
    ac.grid(row=4, column=1, stick='wens', padx=5, pady=5)
    to_delete_all_to_go_first_screen.append(ac)

    on_main_page = Button(window, text='На главную страницу', font='Arial 25', bg='blue', fg='white', activebackground='red',
                   activeforeground='white', command=on_main_screen)
    on_main_page.grid(column=0, row=5, columnspan=4)
    to_delete_all_to_go_first_screen.append(on_main_page)
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
