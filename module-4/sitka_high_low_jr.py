# Name: Jose Rodriguez
# Date: 6/28/2026
# Assignment: CSD 325 Module 4 Assignment
# Program: High/Low Temperatures

# Changes made:
# Added a menu for High Temperatures, Low Temperatures, and Exit.
# Added low temperature data from the CSV file.
# Added a blue graph for low temperatures.
# Added a loop so the program continues until the user exits.
# Added an exit message when the user chooses to quit.

import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt


filename = 'sitka_weather_2018_simple.csv'

# Read dates, high temperatures, and low temperatures from the file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)


# Function to show the high temperature graph.
def show_highs():
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


# Function to show the low temperature graph.
def show_lows():
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


# Main menu loop.
while True:
    print("\nSitka Weather Program")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        show_highs()

    elif choice == '2':
        show_lows()

    elif choice == '3':
        print("Thank you for using the Sitka Weather Program. Goodbye!")
        sys.exit()

    else:
        print("Invalid selection. Please enter 1, 2, or 3.")
