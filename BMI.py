# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)  # Round to 2 decimal places

# Function to classify BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main function to prompt user input and display results
def bmi_calculator():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Determine BMI category
        category = bmi_category(bmi)
        
        # Display the result
        print(f"\nYour BMI is {bmi}, which falls under the category: {category}")
    
    except ValueError:
        print("Please enter valid numbers for weight and height.")

# Run the BMI calculator
if _name_ == "_main_":
    bmi_calculator()