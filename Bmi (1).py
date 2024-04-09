try:
    weight = int(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    if weight <= 0 or height <= 0:
        raise ValueError("Numbers have to be positive")
    
    x = weight / (height * height)
    
    if x < 18:
        print("Your BMI is", x, "and you are skinny")
    elif 18 <= x < 25:
        print("Your BMI is", x, "and you are normal")
    elif 25 <= x < 30:
        print("Your BMI is", x, "and you are fat")
    else:
        print("Your BMI is", x, "and you are super fat LMAO")

except ValueError as e:
    print(f"Error: {e}.Enter a number for the height and weight")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
