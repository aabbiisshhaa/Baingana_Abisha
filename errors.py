# Write a program to handle errors, the program should:
# 1. Ask for 2 numbers using input and then divide them
# 2. Use an infinite loop to keep asking for numbers until a valid input is provided


# List to store calculation history
history = []

while True:
    try:
        # Ask user to input two numbers
        m = float(input("Enter the first number: "))
        n = float(input("Enter the second number: "))

        # Attempt the division
        ans = m / n

    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    except ZeroDivisionError:
        print("Cannot divide by zero! Please enter a different second number.")
        continue

    else:
        # If no exceptions occur, print result and store it in history list
        print(f"Result: {m} ÷ {n} = {ans}")
        
        history.append(f"{m} ÷ {n} = {ans}")
    

    # Ask if the user wants to perform another calculation after a successful division
    prompt = input("Do you wish to perform another calculation? (yes/no): ").strip().lower()
    if prompt != 'yes':
        break
        
# Display all successful calculations at the end
print("\n Calculation History:")
if history:
        for record in history:
            print(record)
            
else:
    print("No successful calculations recorded.")
                
