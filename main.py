# from turtle import Screen, Turtle
from tkinter import FALSE
import turtle
import pandas

# openning the csv file
data = pandas.read_csv("50_states.csv")
data_dict = data
screen = turtle.Screen()
# tur = Turtle()
screen.title("U.S State Game")


screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# To get the x and y coordinate of each state
# def get_mouse_click_coor(x, y):
#     print(f"x:{x}, y:{y}")
# turtle.onscreenclick(get_mouse_click_coor)
tr = turtle.Turtle()
guessed_state = []
missing_state = []
while len(guessed_state) < 50:
    player_answer = screen.textinput(title=f"{len(guessed_state)}/50  State Guessed",prompt="Type the name of a state you can identify on the map").title()
    if player_answer in data.state.to_list():
        data2 = data[data.state == player_answer]
        guessed_state.append(player_answer)
        tr.penup()
        tr.goto(x= float(data2.x) , y=float(data2.y))
        tr.write(player_answer, align="center", font=("arial",7,"normal"))
    elif player_answer == "Exit":
        for state in data.state.to_list():
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn")
        break
    else:
        print("Wrong")

# Generate a state to learn csv
# state_to_learn = []
# for state in guessed_state:
#     for i in data.state:
#         if i == state:
#             pass
#         else:
#             state_to_learn.append(i)
# print(state_to_learn)


# turtle.mainloop()
# screen.exitonclick()