from time import *
import random
from tkinter import *

w = Tk()
w.geometry("600x400")
w.configure(bg='lightblue')


def errors(ori, user):
    if len(ori) == 0:
        return 0

    correct_characters = sum(1 for char1, char2 in zip(ori, user) if char1 == char2)
    accuracy = (correct_characters / len(ori)) * 100
    return accuracy


def generate():
    text = [
        "The quick brown fox jumps over the lazy dog.",
        "Tomorrow is a new day, full of endless possibilities.",
        "The serene ocean waves lapped against the sandy shore.",
        "The aroma of freshly baked bread filled the air.",
        "She danced in the moonlight, her silhouette a graceful shadow.",
        "The ancient castle stood tall against the test of time.",
        "Laughter is the best medicine for a weary heart.",
        "The city never sleeps, its lights shimmering like stars.",
        "The majestic mountains were covered in a blanket of snow.",
        "Music has the power to touch the soul in profound ways."]
    return random.choice(text)


def typing():
    nw = Toplevel(w)
    nw.configure(bg="light blue")
    nw.geometry("600x400")
    label1 = Label(nw, text="Type the following sentence", font=("Comic Sans MS", 28), background="light blue")
    label1.pack()
    text = generate()
    label2 = Label(nw, text=text, font=("Arial", 18), background="light blue")
    label2.place(x=40, y=100)
    start_time = time()
    user_input = Entry(nw, width=80, font=18)
    user_input.place(x=0, y=140)

    def calculate_speed():
        end_time = time()
        time_taken = end_time - start_time
        words = text.split()
        char_typed = len(" ".join(words[:len(user_input.get().split())]))
        wpm = len(user_input.get().split()) / (time_taken / 60)
        accuracy = errors(text, user_input.get())

        result_label = Label(nw, text=f"Your typing speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%",
                            font=("Arial", 14), background='light blue')
        result_label.place(x=160, y=230)

        retry_button = Button(nw, text="Retry", font=("Arial", 12), width=10, height=2, command=retry)
        exit_button = Button(nw, text="Exit", font=("Arial", 12), width=10, height=2, command=nw.destroy)

        retry_button.place(x=100, y=300)
        exit_button.place(x=350, y=300)

    def retry():
        nw.destroy()
        typing()

    submit_button = Button(nw, text="Submit", font=("Arial", 12), width=10, height=2, command=calculate_speed)
    submit_button.place(x=260, y=180)


text_label = Label(w, text="Welcome to simple Typing speed tester!", font=("Comic Sans MS", 22), background='lightblue')
text_label1 = Label(w, text="Are you Ready?", font=("Comic Sans MS", 26), background='lightblue')
text_label.pack()
text_label1.place(x=180, y=80)
yesb = Button(w, text="Yes", font=18, width=10, height=2, command=typing)
nob = Button(w, text="No", font=18, width=10, height=2)
yesb.place(x=120, y=180)
nob.place(x=360, y=180)

w.mainloop()
