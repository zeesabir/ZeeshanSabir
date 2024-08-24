def convert_to_cm(height, unit):
    if unit == 'inches':
        return height * 2.54
    elif unit == 'ft':
        return height * 30.48
    elif unit == 'cm':
        return height
    else:
        return None

def recommend_weight(height_cm):
    # Pre-stored information for weight recommendations based on height in cm
    if height_cm < 150:
        return 45, 55
    elif height_cm < 160:
        return 50, 60
    elif height_cm < 170:
        return 55, 65
    elif height_cm < 180:
        return 60, 70
    elif height_cm < 190:
        return 65, 75
    else:
        return 70, 80

def main():
    print("Welcome to the Weight Recommendation Program!")
    
    age = input("Please enter your age: ")

    # Get user height and unit
    height = input("Please enter your height: ")
    unit = input("Is this in Inches, Ft, or Cm? ").strip().lower()

    try:
        height = float(height)
        height_cm = convert_to_cm(height, unit)
        
        if height_cm is not None:
            weight_min, weight_max = recommend_weight(height_cm)
            print(f"For your height of {height_cm:.2f} cm, your recommended weight should be between {weight_min} kg and {weight_max} kg.")
        else:
            print("Invalid unit. Please enter 'Inches', 'Ft', or 'Cm'.")
    
    except ValueError:
        print("Please enter a valid number for your height.")

if __name__ == "__main__":
    main()
