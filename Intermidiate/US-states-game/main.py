import turtle
import pandas
screen = turtle.Screen()
screen.title("US States")

screen.addshape("./blank_states_img.gif")
turtle.shape("./blank_states_img.gif")
data = pandas.read_csv("./50_states.csv")
all_states_data = data["state"].to_list()
guessed_states = []
states_to_learn = []

while len(guessed_states) <= 50:
    guess = screen.textinput(title= f"{len(guessed_states)}/50 correct, Any more Guess?", prompt= "Guess one of the remaining State of US")
    guess = guess.title()
    if guess == "Exit":
        for state in all_states_data:
            if state not in guessed_states:
                states_to_learn.append(state)
        pandas.DataFrame(states_to_learn).to_csv("States_to_learn.csv")

        break
    if guess in all_states_data:
        guessed_states.append(guess)
        place_holder = turtle.Turtle()
        place_holder.hideturtle()
        place_holder.penup()
        state_data = data[data["state"] == guess]
        place_holder.goto(int(state_data.x), int(state_data.y))
        place_holder.write(arg= f"{guess}")




