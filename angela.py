""" 
# import random

# random_number = random.randint(1,10)
# print(random_number)

# random_float = random.random()
# print(random_float)
""" 

# HEADS OR TAILS EXERCISE
"""
import random

number=random.randint(0,1)
h_or_t= input("Heads or Tails?")

if number== 0:
  winner

  
if(h_or_t == ):
  print("you are the winner")
elif(h_or_t != number):
  print("sorry you lost")

  
random_side = random.randint(0,1)

if random_side ==1:
  print("Heads")
else:
  print("tails")

"""
# WHO WILL PAY THE BILL
"""
import random

names_string = input("enter the names of the people\n")
names = names_string.split(",")
print(names)

x=random.randint(0,len(names)-1)
print(f"{names[x]} will pay the bill")

"""

# WHERE DO YOU WANT TO PUT THE TREASURE
""" 

🚨 Don't change the code below 👇
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")


column = position[0]-1
row = position[1]-1

map([column][row]) = "X"

print(f"{row1}\n{row2}\n{row3}")
""" 

# ROCK PAPER SCISSORS
""" 
import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choose_action = input("choose an action: rock, paper or scissors?: \n")

computer_moves= ["rock", "paper", "scissors"]
random_computer_move = random.choice(computer_moves)

print(random_computer_move)

if choose_action == random_computer_move :
  
  print(f"You both chose {choose_action}. Draw!")

elif choose_action== "rock":
  if random_computer_move == "scissors":
    print("You win!")
  else:
    print("Computer wins!")
  
elif choose_action== "paper":
  if random_computer_move == "rock":
    print("You win!")
  else:
    print("Computer wins!")

elif choose_action== "scissors":
  if random_computer_move == "rock":
    print("You win!")
  else:
    print("Computer wins!")
"""

# --- FOR LOOP--------
""" 
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
  print(fruit)
  print(fruit + " pie")

print(fruits)
""" 
# STUDENT HEIGHTS
""" 
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

  print(student_heights)


sum1= 0
length = len(student_heights)
for i in range (length):
    sum1= sum1 + student_heights[i]

average = sum1/length
print(f"Average height: {average}")

---

total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)

""" 

# HIGHEST SCORE WITHOUT USING MAX

""" 
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


length = len(student_scores)

highest_score=0
for score in student_scores:
  if score > highest_score:
    highest_score= score
    
print(highest_score)

""" 

#PASSWORD GENERATOR

""" 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=""
for letter in range(nr_letters):
  password += random.choice(letters)
for symbol in range(nr_symbols):
  password += random.choice(symbols)
for number in range(nr_numbers):
  password += random.choice(numbers)

password_array= list(password)
random.shuffle(password_array)

str_password=""
for i in range(len(password_array)):
  str_password += password_array[i]
print(str_password)

""" 
""" 
def over_the_hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
while not at_goal():
   if wall_in_front():
      over_the_hurdle()
   else:
      move()
    
""" 

















