#Greeting
print("Hello! Welcome to our Elite 101 Chatbot.")
#Collect user info
user_name = input("What is your name? ")
user_age = input("How old are you? ")
#Greet using info
print("Hello and welcome " + user_name + "! " + "I see you are " + user_age + " years old.")
print("How can I help you today?")

#Design menu of options and establish variables
conversation = True
menu = [ "1. Option 1", "2. Option 2", "3. Option 3", "4. Option 4", "5. Exit Conversation"]

#Define options
def option_1():
  print("You chose Option 1.")
def option_2():
  print("You chose Option 2.")
def option_3():
  print("You chose Option 3.")
def option_4():
  print("You chose Option 4.")
def exit_convo():
  print("You chose to exit the conversation. Goodbye!")
  
#Create while loop to run menu print menu and let user make a choice repeatedly until done
while conversation:
  print("\nHere are your options to choose from: ")
  print(menu[0] + "\n" + menu[1] + "\n" + menu[2] + "\n" + menu[3] + "\n" + menu[4])
  user_choice = input("Enter the number correlating to your choice: ")
  if user_choice == "1":
    option_1()
  elif user_choice == "2":
    option_2()
  elif user_choice == "3":
    option_3()
  elif user_choice == "4":
    option_4()
  elif user_choice == "5":
    exit_convo()
    conversation = False
  else:
    print("Invalid. Please answer with a number. Try again: ")