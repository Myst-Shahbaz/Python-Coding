# -------------------------------
# 🧮 BMI Calculator in Python
# -------------------------------

# Function to calculate BMI based on weight (kg) and height (m)
def calculate_BMI(weight, height):
    # Validate that weight is greater than zero
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    
    # Validate that height is greater than zero
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    
    # Calculate BMI using the standard formula
    bmi = weight / (height ** 2)
    
    # Return the BMI value
    return bmi


# Main function — runs the BMI calculator program
def main():
    print("Welcome to the BMI Calculator!")
    try:
        # Get user's name
        name = input("Please enter your name: ")
        print(f"Hello, {name}! Let's calculate your BMI.")
        
        # Get weight input from the user
        weight = float(input("Enter your weight in kilograms (kg): "))
        
        # Get height input from the user
        height = float(input("Enter your height in meters (m): "))
        
        # Call the calculate_BMI function and store the result
        bmi = calculate_BMI(weight, height)
        
        # Display the BMI result rounded to 2 decimal places
        print(f"\nYour BMI is: {bmi:.2f}")
        
        # Determine and display the BMI category
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        elif 30 <= bmi < 34.9:
            print("You are obese.")
        elif 35 <= bmi < 39.9:
            print("You are severely obese.")
        else:
            print("You are morbidly obese.")
    
    # Handle invalid or non-numeric input gracefully
    except ValueError as e:
        print(f"Error: {e}")


# Ensures the program runs only when executed directly (not imported)
if __name__ == "__main__":
    main()
