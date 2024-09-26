import pandas as pd
from datetime import datetime

# Function to select Zodiac sign
def get_zodiac_sign(day, month):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"

# Function to calculate Zodiac sign
def get_user_info():
    name = input("Enter your name: ")
    dob = input("Enter your birthdate (DD-MM-YYYY): ")

    # Parse the user's birthdate
    bdate = datetime.strptime(dob, "%d-%m-%Y")
    day = bdate.day
    month = bdate.month

    # Get the Zodiac sign
    zodiac_sign = get_zodiac_sign(day, month)

    return name, dob, zodiac_sign

# Function to store the data in a CSV file using Pandas
def store_in_csv(name, birthdate, zodiac_sign):
    # Format the file name to as the user's name and their Zodiac sign (in lowercase)
    file_name = f"{name.lower()}_{zodiac_sign.lower()}.csv"

    # Create a DataFrame to store the user's data
    df = pd.DataFrame([[name, birthdate, zodiac_sign]], columns=["Name", "Birthdate", "Zodiac Sign"])

    # Save the DataFrame to a CSV file
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}.")

# Main program
if __name__ == "__main__":
    # Get user information
    name, birthdate, zodiac_sign = get_user_info()

    # Store data in CSV with a dynamic file name
    store_in_csv(name, birthdate, zodiac_sign)

    # Output Zodiac sign
    print(f"{name}, your Zodiac sign is: {zodiac_sign}")