#!/usr/bin/env python3

import csv
import datetime
import requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def get_start_date():
    """Interactively get the start date to query for."""
    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)


def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""
    # Downloads the file over the internet.
    response = requests.get(url, stream=True)
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines


def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one"""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    # Generates Dictionary with 'start_date' and following dates as keys
    # and list of employees that started on the given date as its value.
    matching_employees = {}
    for row in reader:
        # Formats the date in datetime format to compare it with
        # the 'start_date'.
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        name = "{} {}".format(row[0], row[1])
        if row_date not in matching_employees:
            matching_employees[row_date] = [name]
        else:
            matching_employees[row_date].append(name)
    # Iterates through the dictionary to match start_date & all successive
    # dates and print them in required format.
    for date, employees in sorted(matching_employees.items()):
        if date >= start_date:
            print("Started on {}: {}".format(date.strftime("%b %d, %Y"), employees))
    # If 'start_date' and all closest dates are empty - prints informative message.
    if start_date > list(sorted(matching_employees.keys()))[-1]:
        print("No new employees have started from the entered date")


def main():
    get_file_lines(FILE_URL)  # Downloads a file only once at start.
    start_date = get_start_date()  # gets the date.
    get_same_or_newer(start_date)  # send the date and file.


if __name__ == "__main__":
    main()
