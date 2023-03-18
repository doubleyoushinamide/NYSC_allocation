import random as rand

states = ["Nassarawa", "Jigawa", "Abuja", "Gombe", "Sokoto", "Kano",
          "Lagos", "Osun", "Ekiti", "Oyo", "Kwara",
          "Kogi", "Plateau", "Markurdi", "Imo", "Abia", "Anambra", "Enugu",
          "Cross-Rivers", "Delta", "Rivers", "Akwa-Ibom", "Edo"]
All_states = set(states)

# Get user inputs
def get_user_inputs():
    user_inputs = set()
    for i in range(3):
        user_input = input(f"Enter state{i+1}: ").title()
        user_inputs.add(user_input)
    return user_inputs

# Select and print the result
def syt_choice():
    new_list = list(All_states - get_user_inputs())
    display = rand.choice(new_list)
    print(f"""----------------------------------------------------------
    Congratulations!!! You have been posted to {display} State 
    for your NYSC service. Good Luck!!!!
    ------------------------------------------------------""")
    return display

syt_choice()
