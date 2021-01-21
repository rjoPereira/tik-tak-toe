# author: Ricardo Pereira
from time import sleep
from tkinter import *

positions = [
    [(1, 1), (188, 1), (378, 1)],
    [(1, 191), (190, 191), (378, 191)],
    [(1, 378), (190, 378), (378, 379)]
]
buttons = [
    [],
    [],
    []
]
turn = 0


def play(button_obj):
    global turn

    if turn == 0 and button_obj.cget("image") == "":
        button_obj.config(image=x_file)
        button_obj.place(relx=0.02)
        turn = 1
        if has_won():
            reset()
        elif is_full():
            reset()
    elif turn == 1 and button_obj.cget("image") == "":
        button_obj.config(image=o_file)
        button_obj.place(relx=0.02)
        turn = 0
        if has_won():
            reset()
        elif is_full():
            reset()


def reset():
    global buttons

    window.update_idletasks()
    sleep(2)

    for i in range(0, 3):
        for j in range(0, 3):
            b = Button()
            b.config(command=lambda button=b: play(button),
                     padx=80, pady=71, borderwidth=0,
                     bg="white",
                     highlightthickness=0)
            buttons[i][j] = b
            buttons[i][j].place(x=positions[i][j][0], y=positions[i][j][1])


def change_image(i1, j1, i2, j2, i3, j3, img):
    buttons[i1][j1].config(image=img)
    buttons[i2][j2].config(image=img)
    buttons[i3][j3].config(image=img)


def is_full():
    for i in range(0, 3):
        for j in range(0, 3):
            if buttons[i][j].cget("image") == "":
                return False

    return True


def has_won():
    if buttons[0][0].cget("image") == buttons[0][1].cget("image") == buttons[0][2].cget("image") == str(x_file):
        change_image(0, 0, 0, 1, 0, 2, x_win_file)
        return True
    if buttons[0][0].cget("image") == buttons[0][1].cget("image") == buttons[0][2].cget("image") == str(o_file):
        change_image(0, 0, 0, 1, 0, 2, o_win_file)
        return True
    if buttons[1][0].cget("image") == buttons[1][1].cget("image") == buttons[1][2].cget("image") == str(x_file):
        change_image(1, 0, 1, 1, 1, 2, x_win_file)
        return True
    if buttons[1][0].cget("image") == buttons[1][1].cget("image") == buttons[1][2].cget("image") == str(o_file):
        change_image(1, 0, 1, 1, 1, 2, o_win_file)
        return True
    if buttons[2][0].cget("image") == buttons[2][1].cget("image") == buttons[2][2].cget("image") == str(x_file):
        change_image(2, 0, 2, 1, 2, 2, x_win_file)
        return True
    if buttons[2][0].cget("image") == buttons[2][1].cget("image") == buttons[2][2].cget("image") == str(o_file):
        change_image(2, 0, 2, 1, 2, 2, o_win_file)
        return True
    if buttons[0][0].cget("image") == buttons[1][0].cget("image") == buttons[2][0].cget("image") == str(x_file):
        change_image(0, 0, 1, 0, 2, 0, x_win_file)
        return True
    if buttons[0][0].cget("image") == buttons[1][0].cget("image") == buttons[2][0].cget("image") == str(o_file):
        change_image(0, 0, 1, 0, 2, 0, o_win_file)
        return True
    if buttons[0][1].cget("image") == buttons[1][1].cget("image") == buttons[2][1].cget("image") == str(x_file):
        change_image(0, 1, 1, 1, 2, 1, x_win_file)
        return True
    if buttons[0][1].cget("image") == buttons[1][1].cget("image") == buttons[2][1].cget("image") == str(o_file):
        change_image(0, 1, 1, 1, 2, 1, o_win_file)
        return True
    if buttons[0][2].cget("image") == buttons[1][2].cget("image") == buttons[2][2].cget("image") == str(x_file):
        change_image(0, 2, 1, 2, 2, 2, x_win_file)
        return True
    if buttons[0][2].cget("image") == buttons[1][2].cget("image") == buttons[2][2].cget("image") == str(o_file):
        change_image(0, 2, 1, 2, 2, 2, o_win_file)
        return True
    if buttons[0][0].cget("image") == buttons[1][1].cget("image") == buttons[2][2].cget("image") == str(x_file):
        change_image(0, 0, 1, 1, 2, 2, x_win_file)
        return True
    if buttons[0][0].cget("image") == buttons[1][1].cget("image") == buttons[2][2].cget("image") == str(o_file):
        change_image(0, 0, 1, 1, 2, 2, o_win_file)
        return True
    if buttons[0][2].cget("image") == buttons[1][1].cget("image") == buttons[2][0].cget("image") == str(x_file):
        change_image(0, 2, 1, 1, 2, 0, x_win_file)
        return True
    if buttons[0][2].cget("image") == buttons[1][1].cget("image") == buttons[2][0].cget("image") == str(o_file):
        change_image(0, 2, 1, 1, 2, 0, o_win_file)
        return True


window = Tk()
window.title("Jogo do Galo")
window.minsize(width=552, height=541)
window.resizable(False, False)

x_file = PhotoImage(file="X.png")
x_win_file = PhotoImage(file="X_win.png")
o_file = PhotoImage(file="circle.png")
o_win_file = PhotoImage(file="circle_win.png")
image_file = PhotoImage(file="Tic_Tac_Toe.png")

canvas = Canvas(width=552, height=542, highlightthickness=0, bg="white")
canvas.pack()
image = canvas.create_image(276, 271, image=image_file)

for i in range(0, 3):
    for j in range(0, 3):
        button_obj = Button()
        button_obj.config(command=lambda button=button_obj: play(button),
                          padx=80, pady=71, borderwidth=0,
                          bg="white",
                          highlightthickness=0)
        buttons[i].append(button_obj)
        buttons[i][j].place(x=positions[i][j][0], y=positions[i][j][1])

mainloop()
