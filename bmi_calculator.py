# Function to calculate BMI
def calculate_bmi(weight_kg, height_m):
    """
    Calculates the Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: The calculated BMI.
    """
    if height_m <= 0:
        raise ValueError("Height cannot be zero or negative.")
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Function to classify BMI into categories
def classify_bmi(bmi):
    """
    Classifies the BMI into different categories.

    Args:
        bmi (float): The calculated BMI.

    Returns:
        str: The BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main function to run the BMI calculator
def main():
    """
    Prompts the user for weight and height, calculates BMI,
    classifies it, and displays the result.
    """
    print("Welcome to the BMI Calculator!")

    while True:
        try:
            # Get weight input from the user
            weight_str = input("Enter your weight in kilograms (e.g., 70.5): ")
            weight_kg = float(weight_str)
            if weight_kg <= 0:
                print("Weight must be a positive number. Please try again.")
                continue

            # Get height input from the user
            height_str = input("Enter your height in meters (e.g., 1.75): ")
            height_m = float(height_str)
            if height_m <= 0:
                print("Height must be a positive number. Please try again.")
                continue

            break # Exit loop if inputs are valid

        except ValueError:
            print("Invalid input. Please enter numerical values for weight and height.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Calculate BMI
    try:
        bmi = calculate_bmi(weight_kg, height_m)
        # Classify BMI
        category = classify_bmi(bmi)

        # Display the results
        print(f"\nYour BMI is: {bmi:.2f}") # Format BMI to two decimal places
        print(f"Based on your BMI, you are categorized as: {category}")
    except ValueError as e:
        print(f"Error calculating BMI: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during calculation: {e}")


if __name__ == "__main__":
    main()