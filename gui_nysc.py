import random as rand
import tkinter as tk

states = ["Nassarawa", "Jigawa", "Abuja", "Gombe", "Sokoto", "Kano",
          "Lagos", "Osun", "Ekiti", "Oyo", "Kwara",
          "Kogi", "Plateau", "Benue", "Imo", "Abia", "Anambra", "Enugu",
          "Cross-Rivers", "Delta", "Rivers", "Akwa-Ibom", "Edo"]
All_states = set(states)

# Define GUI popup function
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("NYSC Posting Result")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    button = tk.Button(popup, text="OK", command=popup.destroy)
    button.pack()
    popup.mainloop()

# Get user inputs from GUI
def get_user_inputs():
    user_inputs = set()
    for input_box in input_boxes:
        user_input = input_box.get().title()
        user_inputs.add(user_input)
    return user_inputs

# Select and print the result using GUI popup function
def syt_choice():
    new_list = list(All_states - get_user_inputs())
    if len(new_list) == 0:
        msg = "Error: No states remaining to choose from!"
    else:
        display = rand.choice(new_list)
        msg = f"Congratulations!!! You have been posted to {display} State for your NYSC service. Good Luck!!!!"
    popupmsg(msg)

root = tk.Tk()
root.title("NYSC Posting")

# Create input boxes and labels
input_boxes = []
for i in range(3):
    label = tk.Label(root, text=f"Enter state{i+1}: ")
    label.grid(row=i, column=0, sticky="W")
    input_box = tk.Entry(root)
    input_box.grid(row=i, column=1, padx=5, pady=5)
    input_boxes.append(input_box)

# Create button and result label
button = tk.Button(root, text="Generate", command=syt_choice)
button.grid(row=3, column=1, pady=10)
result_label = tk.Label(root)
result_label.grid(row=4, columnspan=2)

root.mainloop()
