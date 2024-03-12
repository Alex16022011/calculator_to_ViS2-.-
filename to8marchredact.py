for i in range(10):
    for j in range(10):
        print(f"button{i}{j} = Button(text=matrix[{i}][{j}], font=\"Arial 14\", width=4, bd=5, bg=\"grey\", activebackground='green')")
        print(f"button{i}{j}.grid(row=({i} + 2), column=({j} + 1), padx=1, pady=1)")
        print(f"to_delete_all_to_go_first_screen.append(button{i}{j})")