# 🤖 Advance Joke Bot with Emojis

def tell_joke():
    print("\n🤣 What do you call a fake noodle?")
    print("👉 An *Impasta*! 🍝\n")
    print("🐄 What do you call a cow with no legs?")
    print("👉 *Ground beef!* 🥩\n")

print("===================================")
print("🎉 Welcome to the Advance Joke Bot! 🤖")
print("Type 'joke' to hear a joke or 'exit' to leave.")
print("===================================\n")

while True:
    user_input = input("👉 What do you want? ").strip().lower()

    if user_input == "joke":
        tell_joke()
        another_joke = input("😂 Want another joke? (yes/no): ").strip().lower()
        if another_joke != "yes":
            print("\n👋 Okay, goodbye! Stay laughing! 😄")
            break
    elif user_input == "exit":
        print("\n👋 Goodbye! Come back for more laughs! 😂")
        break
    else:
        print("❌ I only tell jokes. Try typing: 'joke' or 'exit'\n")

