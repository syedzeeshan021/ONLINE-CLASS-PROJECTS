# Write a simple joke bot. The bot starts by asking the user what they want. 
# However, your program will only respond to one response: Joke.
# If the user enters Joke then we will print out a single joke. Each time the joke is always the same:

print("Joke Bot")
user_input = input("What do you want?")

if user_input.strip().lower() == "joke":
    print("Why did the chicken cross the road?")
    print("To get to the other side.")
    print("Knock knock.")
    print("Who's there?")
else:
    print("I only tell jokes. Try typing: Joke")






