from random import randint
import tkinter as tk

# Original Rating
Rating = 400

# Maximum gain or loss
K = 50

players = []

class player:
    def __init__(self, name):
        self.name = name
        self.rating = Rating
        players.append(self)

num = 0
def rate():
    global num
    player_num = len(players)
    if num == player_num:
        num = 0
    global a, b
    a = players[num]
    new_players = players.copy()
    new_players.pop(num)
    b = new_players[randint(0, player_num - 2)]

    global ExpScoreA, ExpScoreB
    ExpScoreA = (1 / (1 + (10 ** ((b.rating - a.rating) / 400))))
    ExpScoreB = 1 - ExpScoreA
    textA.set(a.name)
    textB.set(b.name)

def A():
    SA = 1
    SB = 0

    a.rating += K * (SA - ExpScoreA)
    b.rating += K * (SB - ExpScoreB)

    text3.set(f"{a.name}'s rating is {round(a.rating)}, and {b.name}'s is {round(b.rating)}")

    global num
    num += 1
    text4.set("")
    rate()
def B():
    SA = 0
    SB = 1

    a.rating += K * (SA - ExpScoreA)
    b.rating += K * (SB - ExpScoreB)

    text3.set(f"{a.name}'s rating is {round(a.rating)}, and {b.name}'s is {round(b.rating)}")

    global num
    num += 1
    text4.set("")
    rate()

def show_rating():
    players.sort(key=lambda x: x.rating, reverse=True)
    l = []
    for x in players:
        l.append(f"{x.name}'s rating is {round(x.rating)}")
    text4.set('\n'.join(l))

count = 1

def add_player():
    p_name = entry1.get()
    k = player(p_name)
    global count
    count += 1
    text1.set(f"Name of player {count}")
    entry1.delete(0, "end")

window = tk.Tk()
window.geometry("550x500")
window.title("Rating system")
text1 = tk.StringVar()
text1.set(f"Name of player {count}")
p_nameLabel = tk.Label(window, textvariable=text1)
p_nameLabel.grid(column=0, row=1)

entry1 = tk.Entry()
entry1.grid(column=1, row=1)

button = tk.Button(text="Add player", fg="blue", command=add_player)
button.grid(column=1, row=2)

Label = tk.Label(window, text="")
Label.grid(column=1, row=3)

button = tk.Button(text="Rate!", fg="blue", command=rate)
button.grid(column=1, row=4)

Label = tk.Label(window, text="")
Label.grid(column=1, row=5)

textA = tk.StringVar()
textA.set("")
buttonA = tk.Button(textvariable=textA, fg="blue", command=A, height=3, width=6)
buttonA.grid(column=0, row=6)
buttonA.config(font=("Ariel", 25))

textB = tk.StringVar()
textB.set("")
buttonB = tk.Button(textvariable=textB, fg="blue", command=B, height=3, width=6)
buttonB.grid(column=2, row=6)
buttonB.config(font=("Ariel", 25))

Label = tk.Label(window, text="")
Label.grid(column=1, row=7)

text3 = tk.StringVar()
text3.set("")
ratLabel = tk.Label(window, textvariable=text3)
ratLabel.grid(column=1, row=8)

Label = tk.Label(window, text="")
Label.grid(column=1, row=9)

text4 = tk.StringVar()
text4.set("")
Label = tk.Label(window, textvariable=text4)
Label.grid(column=1, row=11)

button = tk.Button(text="Show all ratings", fg="blue", command=show_rating)
button.grid(column=1, row=10)


window.mainloop()
