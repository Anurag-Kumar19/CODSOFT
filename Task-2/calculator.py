from tkinter import *
root = Tk()
root.geometry("450x550")
root.title("Calculator")
root.resizable(True, True)

def press(value):
    first = display.cget("text")
    if first == "0" and value not in "+-×÷":
        display.config(text = str(value))
    else:
        display.config(text = first + str(value))

def clear():
    display.config( text = "0")

def backspace():
    current = display.cget("text")
    if len(current) > 1:
        display.config(text=current[:-1])
    else:
        display.config(text="0")


def equal_to():
    try:
        expression = display.cget("text").replace("×", "*").replace("÷", "/")
        result = str(eval(expression))
        display.config(text=result)
    except:
        display.config(text="Error")
        

display = Label(root, text="0", anchor="e", bg="#1E1E1E",fg="#FFFFFF", font=("Arial", 28), padx=10, relief="sunken", bd=3)
display.pack(fill=X, pady=5)

button_frame=Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["C", "0","⌫", "="],
    ["","+","",""]
]

for r in range(len(buttons)):
    for c in range(len(buttons[r])):
        char = buttons[r][c]
        if char == "C":
            cmd = clear
        elif char == "=":
            cmd = equal_to
        elif char == "⌫":
            cmd = backspace
        else:
            cmd = lambda ch=char: press(ch)

        btn = Button(button_frame, text=char, width=5, height=2, font=("Arial", 18), bg="#F0F0F0",fg="black", relief="raised", bd=2, command=cmd )
        btn.grid(row=r, column=c, padx=5, pady=5)
root.mainloop()
