import random
from tkinter import *

root = Tk()
root.title("Rock-paper-scissors")
root.geometry("600x550")
root.resizable(True, True)
root['bg'] = "#ffccdc"

img1 = PhotoImage(file="rock.png")
smaller_img = img1.subsample(3, 3)
img2 = PhotoImage(file="paper.png")
smaller_img2 = img2.subsample(3, 3)
img3 = PhotoImage(file="scissors.png")
smaller_img3 = img3.subsample(3, 3)
images = [smaller_img, smaller_img2, smaller_img3]
choices = ["rock", "paper", "scissors"]

user_score = 0
comp_score = 0

def check_winner(player, computer):
    global user_score, comp_score
    if player == computer:
        return "It's a Draw!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        user_score += 1
        return "You Win!"
    else:
        comp_score += 1
        return "You Lose!"

def play(player_choice):
    
    if player_choice == "rock":
        display1.config(image=smaller_img)
        display1.image = smaller_img
    elif player_choice == "paper":
        display1.config(image=smaller_img2)
        display1.image = smaller_img2
    else:
        display1.config(image=smaller_img3)
        display1.image = smaller_img3
    
    
    idk = random.randint(0, 2)
    comp_img = images[idk]
    comp_choice = choices[idk]
    display2.config(image=comp_img)
    display2.image = comp_img
    
    
    result = check_winner(player_choice, comp_choice)
    result_label.config(text=result)
    score_label.config(text=f"Your Score: {user_score}   Computer Score: {comp_score}")

btn_frame = Frame(root, bg="#F6C4CF")
btn_frame.pack(side="top", pady=40)
rock_btn = Button(btn_frame, text="Rock", width=12, height=2, bg="#f3ab9b", fg="black", relief="raised", command=lambda: play("rock"))
paper_btn = Button(btn_frame, text="Paper", width=12, height=2, bg="#f9e79f", fg="black", relief="raised", command=lambda: play("paper"))
scissor_btn = Button(btn_frame, text="Scissor", width=12, height=2, bg="#a9cce3", fg="black", relief="raised", command=lambda: play("scissors"))
rock_btn.pack(side="left", padx=20)
paper_btn.pack(side="left", padx=20)
scissor_btn.pack(side="left", padx=20)


score_label = Label(root, text="Your Score: 0   Computer Score: 0", font=("Arial", 16), bg="#ffccdc", fg="black")
score_label.pack(pady=10)

display1_frame = Frame(root, width=200, height=200, bg="#bae6af", bd=3, relief="sunken")
display1_frame.pack_propagate(False)
display1_frame.pack(side="left", padx=20, pady=20)
display1 = Label(display1_frame, bg="#bae6af")
display1.pack()

display2_frame = Frame(root, width=200, height=200, bg="#bae6af", bd=3, relief="sunken")
display2_frame.pack_propagate(False)
display2_frame.pack(side="right", padx=20, pady=20)
display2 = Label(display2_frame, bg="#bae6af")
display2.pack()


result_label = Label(root, text="", font=("Arial", 18), bg="#ffccdc", fg="black", wraplength=500, justify="center")
result_label.pack(side="bottom", pady=30)

root.mainloop()

