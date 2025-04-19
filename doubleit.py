# 🎯 Number Doubler - Fancy but Simple

print("🔢 Welcome to the Number Doubler!")
print("💬 Enter a number and watch it grow... 💥\n")

# Start by getting a number from the user
curr_value = float(input("👉 Enter a number: "))

# Start doubling and printing values
while curr_value < 100:
    previous_value = curr_value
    curr_value = curr_value * 2
    print(f" Doubling {int(previous_value)} gives {int(curr_value)}")

print("\n\n🎉Done! The final number is 100 or greater than 100.")
print(" Thanks for using the Number Doubler Program!")
