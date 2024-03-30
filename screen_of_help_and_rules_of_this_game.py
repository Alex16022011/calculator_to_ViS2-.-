from tkinter import*

window = Tk()
window.geometry('500x500+100+100')
to_delete_all_to_go_first_screen = []


def delete_all_to_go_to_first_screen():
    global window
    global to_delete_all_to_go_first_screen
    if len(to_delete_all_to_go_first_screen) > 0:
        for i in to_delete_all_to_go_first_screen:
            i.destroy()
        to_delete_all_to_go_first_screen = []
    return window


def screen_with_rules():
    btn_to_go_rules_of_game.destroy()
#     for i in range(15):
#         exec(f'''lbl{i} = Label(text='{i}. ', font='Arial 15')
# lbl{i}.grid(row={i}, column=0)
# to_delete_all_to_go_first_screen.append(lbl{i})''')
    lbl0 = Label(text='0. Чтобы начать игру нажмите кнопку "Морской бой"', font='Arial 15')
    lbl0.grid(row=0, column=0)
    to_delete_all_to_go_first_screen.append(lbl0)
    lbl1 = Label(text='1. ', font='Arial 15')
    lbl1.grid(row=1, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl1)
    lbl2 = Label(text='2. ', font='Arial 15')
    lbl2.grid(row=2, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl2)
    lbl3 = Label(text='3. ', font='Arial 15')
    lbl3.grid(row=3, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl3)
    lbl4 = Label(text='4. ', font='Arial 15')
    lbl4.grid(row=4, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl4)
    lbl5 = Label(text='5. ', font='Arial 15')
    lbl5.grid(row=5, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl5)
    lbl6 = Label(text='6. ', font='Arial 15')
    lbl6.grid(row=6, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl6)
    lbl7 = Label(text='7. ', font='Arial 15')
    lbl7.grid(row=7, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl7)
    lbl8 = Label(text='8. ', font='Arial 15')
    lbl8.grid(row=8, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl8)
    lbl9 = Label(text='9. ', font='Arial 15')
    lbl9.grid(row=9, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl9)
    lbl10 = Label(text='10. ', font='Arial 15')
    lbl10.grid(row=10, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl10)
    lbl11 = Label(text='11. ', font='Arial 15')
    lbl11.grid(row=11, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl11)
    lbl12 = Label(text='12. ', font='Arial 15')
    lbl12.grid(row=12, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl12)
    lbl13 = Label(text='13. ', font='Arial 15')
    lbl13.grid(row=13, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl13)
    lbl14 = Label(text='14. ', font='Arial 15')
    lbl14.grid(row=14, column=0, sticky='w')
    to_delete_all_to_go_first_screen.append(lbl14)


btn_to_go_rules_of_game = Button(text='Правила\nпользования\nигрой', font='Arial 20', command=screen_with_rules)
btn_to_go_rules_of_game.grid(row=0, column=0)

window.mainloop()