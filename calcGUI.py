import tkinter as tk
from tkinter import font as tkFont
import calculator as clc


root = tk.Tk()
# Set up the window
# root.resizable(width=False, height=False)

window_width = 800
window_height = 400
dark_mode = False
default_colour = "#F0F0F0"
dark_colour = "#333333"
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
empty_response = ""


def user_solve():
    eq = clc_eq.get()
    ans = clc.solve(eq)
    if ans[0] == "I":
        clc_result["text"] = empty_response
        clc_error["text"] = ans
    else:
        clc_result["text"] = wrap(ans, 20)
        clc_error["text"] = empty_response


def wrap(string, max_width):
    para = ""
    temp = ""
    count = 0
    for i in range(len(string)):
        temp += string[i]
        count += 1
        if count == max_width or i == len(string)-1:
            para += temp + "\n"
            temp = ""
            count = 0
    return para


# center of screen
cx = int(screen_width/2 - window_width/2)
cy = int(screen_height/3 - window_height/3)

# configure the GUI itself
root.title("Calculator")
root.geometry(f'{window_width}x{window_height}+{cx}+{cy}')
root.config(bg=default_colour)


clc_eq = tk.Entry(master=root, width=30) # user equation

# All user buttons
clc_calc = tk.Button(
    master=root,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=user_solve,
    width=8,
    height=1,
    bg="green"
)

# Labels
clc_title = tk.Label(
    master=root,
    text="Group 19 Calculator",
    bg=default_colour,
    font=("Segoe UI", 30)
    )

clc_subtitle = tk.Label(
    master=root,
    text="To start, please enter an equation in the box below.",
    bg=default_colour)


clc_result = tk.Label(master=root, text=empty_response,font=("Segoe UI", 11), bg=default_colour)
clc_error = tk.Label(master=root, text="", bg=default_colour, fg="dark red")

###################### POSITIONING ALL WIDGETS ######################
clc_title.place(relx=0.5, rely=.1, anchor='center')
clc_subtitle.place(relx=0.5, rely=.2, anchor='center')
clc_eq.place(relx=.2, rely=.35, anchor='center')
clc_calc.place(relx=.5, rely=.35, anchor='center')
clc_result.place(relx=.8, rely=.375, anchor='center')
clc_error.place(relx=.5, rely=.45, anchor='center')


clc_eq.focus_set()  # focus the equation entry on load

# Run the application
root.mainloop()
