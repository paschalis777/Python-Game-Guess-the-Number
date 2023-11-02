import tkinter as tk
import random

attempts_limit = 10
attempts = 0
hidden_number = random.randint(1, 100)

def check_number(event=None):
    global attempts
    user_guess = int(entry.get())
    attempts += 1
    remaining_attempts = attempts_limit - attempts
    attempts_label.config(text="Απομένουν προσπάθειες: " + str(remaining_attempts), font=("Helvetica", 14), background="gray")

    if user_guess == hidden_number:
        result_label.config(text="Σωστά! Προσπάθειες: " + str(attempts), font=("Helvetica", 16), background="gray")
        new_game_button.config(state=tk.NORMAL)
        check_button.config(state=tk.DISABLED)
        if attempts == 1:
            show_trophy()
    elif user_guess < hidden_number:
        result_label.config(text="Δοκιμάστε ένα μεγαλύτερο νούμερο.", font=("Helvetica", 14), background="gray")
    else:
        result_label.config(text="Δοκιμάστε ένα μικρότερο νούμερο.", font=("Helvetica", 14), background="gray")

    if attempts >= attempts_limit:
        result_label.config(text="Χάσατε! Ο σωστός αριθμός ήταν " + str(hidden_number), font=("Helvetica", 14), background="gray")
        new_game_button.config(state=tk.NORMAL)
        check_button.config(state=tk.DISABLED)

def start_new_game():
    global hidden_number, attempts
    hidden_number = random.randint(1, 100)
    entry.delete(0, tk.END)
    result_label.config(text="", background="gray")
    new_game_button.config(state=tk.DISABLED)
    check_button.config(state=tk.NORMAL)
    attempts = 0
    attempts_label.config(text="Απομένουν προσπάθειες: " + str(attempts_limit), font=("Helvetica", 14), background="gray")
    hide_trophy()

def show_trophy():
    trophy_window = tk.Toplevel(window)
    trophy_window.title("Συγχαρητήρια!")

    trophy_label = tk.Label(trophy_window, text="Συγχαρητήρια! Κερδίσατε το παιχνίδι!", font=("Helvetica", 16))
    trophy_label.pack()

    # Φορτώστε την εικόνα
    trophy_image = tk.PhotoImage(file="pasch.gif")  # Αντικαταστήστε "giphy.gif" με το όνομα της εικόνας του τροπαίου
    trophy_image_label = tk.Label(trophy_window, image=trophy_image)
    trophy_image_label.pack()

    trophy_window.mainloop()

window = tk.Tk()
window.title("Παιχνίδι 'Βρες τον αριθμό'")

def hide_trophy():
    for widget in trophy_window.winfo_children():
        widget.destroy()
    trophy_window.withdraw()

window = tk.Tk()
window.title("Παιχνίδι 'Βρες τον αριθμό'")
window.configure(background="gray")

label = tk.Label(window, text="Βρείτε τον αριθμό μεταξύ 1 και 100.", font=("Helvetica", 16), background="gray")
label.pack()

entry = tk.Entry(window, font=("Helvetica", 14))
entry.pack()
entry.bind("<Return>", check_number)  # Προσθέστε αυτήν τη γραμμή για να δεσμεύσετε το Enter με τη συνάρτηση check_number

check_button = tk.Button(window, text="Έλεγχος", command=check_number, font=("Helvetica", 14), height=2, width=15)
check_button.pack()

clear_button = tk.Button(window, text="Clear", command=lambda: entry.delete(0, tk.END), font=("Helvetica", 14), height=2, width=15)
clear_button.pack()

new_game_button = tk.Button(window, text="New Game", command=start_new_game, font=("Helvetica", 14), height=2, width=15)
new_game_button.pack()
new_game_button.config(state=tk.DISABLED)

result_label = tk.Label(window, text="", background="gray", font=("Helvetica", 16))
result_label.pack()

attempts_label = tk.Label(window, text="Απομένουν προσπάθειες: " + str(attempts_limit), font=("Helvetica", 14), background="gray")
attempts_label.pack()

trophy_window = tk.Toplevel(window)
trophy_window.withdraw()

window.mainloop()
