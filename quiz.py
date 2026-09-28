import tkinter as tk
from tkinter import messagebox

# ---------------- QUIZ QUESTIONS ----------------

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which language is used for Python programming?",
        "options": ["HTML", "Python", "CSS", "SQL"],
        "answer": "Python"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Computer Processing Unit"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "How many bits are in one byte?",
        "options": ["4", "8", "16", "32"],
        "answer": "8"
    },
    {
        "question": "Which company developed Windows?",
        "options": ["Apple", "Google", "Microsoft", "IBM"],
        "answer": "Microsoft"
    },
    {
        "question": "What is the full form of RAM?",
        "options": [
            "Random Access Memory",
            "Read Access Memory",
            "Rapid Access Machine",
            "Run Access Memory"
        ],
        "answer": "Random Access Memory"
    },
    {
        "question": "Which device is used to measure temperature?",
        "options": ["Barometer", "Thermometer", "Ammeter", "Voltmeter"],
        "answer": "Thermometer"
    }
]

# ---------------- VARIABLES ----------------

current_question = 0
score = 0

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("🎯 Quiz Master")
root.geometry("700x600")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

# ---------------- FUNCTIONS ----------------

def load_question():
    question_data = questions[current_question]

    question_number.config(
        text=f"Question {current_question + 1} of {len(questions)}"
    )

    question_label.config(
        text=question_data["question"]
    )

    for i in range(4):
        option_buttons[i].config(
            text=question_data["options"][i],
            state="normal"
        )

    score_label.config(text=f"Score: {score}")


def check_answer(selected_answer):
    global current_question, score

    correct_answer = questions[current_question]["answer"]

    if selected_answer == correct_answer:
        score += 1
        messagebox.showinfo("Correct! 🎉", "Excellent! Your answer is correct.")
    else:
        messagebox.showerror(
            "Wrong Answer ❌",
            f"Correct answer: {correct_answer}"
        )

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        show_result()


def show_result():
    question_number.config(text="Quiz Completed 🎉")
    question_label.config(
        text=f"Your Final Score is {score}/{len(questions)}"
    )

    for button in option_buttons:
        button.config(state="disabled")

    score_label.config(text=f"Final Score: {score}")

    restart_button.pack(pady=20)


def restart_quiz():
    global current_question, score

    current_question = 0
    score = 0

    restart_button.pack_forget()

    load_question()


# ---------------- TITLE ----------------

title_label = tk.Label(
    root,
    text="🎯 QUIZ MASTER",
    font=("Arial", 28, "bold"),
    bg="#1e1e2f",
    fg="#00e5ff"
)
title_label.pack(pady=20)

# ---------------- SCORE ----------------

score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
)
score_label.pack()

# ---------------- QUESTION NUMBER ----------------

question_number = tk.Label(
    root,
    text="Question 1",
    font=("Arial", 15, "bold"),
    bg="#1e1e2f",
    fg="#ffd166"
)
question_number.pack(pady=15)

# ---------------- QUESTION ----------------

question_label = tk.Label(
    root,
    text="Question",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="white",
    wraplength=600
)
question_label.pack(pady=20)

# ---------------- OPTIONS ----------------

option_buttons = []

for i in range(4):
    button = tk.Button(
        root,
        text="Option",
        font=("Arial", 14, "bold"),
        width=45,
        height=2,
        bg="#34344a",
        fg="white",
        activebackground="#00e5ff",
        activeforeground="black",
        relief="flat",
        cursor="hand2",
        command=lambda i=i: check_answer(
            questions[current_question]["options"][i]
        )
    )

    button.pack(pady=7)

    option_buttons.append(button)

# ---------------- RESTART BUTTON ----------------

restart_button = tk.Button(
    root,
    text="🔄 PLAY AGAIN",
    font=("Arial", 14, "bold"),
    bg="#06d6a0",
    fg="white",
    width=20,
    height=2,
    relief="flat",
    cursor="hand2",
    command=restart_quiz
)

# ---------------- START GAME ----------------

load_question()

root.mainloop()

root.mainloop()
