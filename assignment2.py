import argparse
import urllib.request
import logging
import datetime

def downloadData(url):
    """
        Reads data from a URL and returns the data as a string
        :param url:
        :return: the content of the URL
        """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')
    # return the data
    return response


import datetime
def processData(file_content):
    """
    (from the assignment) write a function that takes the contents of the
    file as the first parameter, processes the file line by line,
    and returns a dictionary that maps a person’s ID to a tuple of the form (name, birthday).

    The birthday needs to be a Datetime object, not a string. The format "%d/%m/%Y"

    :param file_content:
    :return:
    """

    result_dict = {}
    lines = file_content.split("\n")

    for line in lines:
        try:
            items = line.split(",")
            id = int(items[0])
            name = items[1]
            date_str = items[2]
            birthday = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            result_dict[id] = (name, birthday)
        except Exception as e:
            print(f"Error processing line: {line}")
            print(e)

    return result_dict

def displayPerson(id, personData):
    """
    Displays the person's name and birthday for the given ID.

    :param id: The person's ID.
    :param personData: A dictionary that maps person IDs to tuples of the form (name, birthday).
    """

    try:
        name, birthday = personData[id]
        print(f"{name} was born on {birthday:%Y-%m-%d}")
    except KeyError:
        print(f"No user found with ID {id}")



def main(url):
    """
    Downloads the data from the given URL, processes the data, and then displays the
    name and birthday of the person with the ID 3.

    :param url: The URL to download the data from.
    """

    print(f"Running main with URL = {url}...")
    url_data = downloadData(url)
    data_dict = processData(url_data)

    # Ask the user for an ID.
    while True:
        try:
            id = int(input("Enter an ID: "))
            if id < 0:
                raise ValueError("ID must be greater than or equal to 0")
            break
        except ValueError:
            print("Invalid ID. Please enter a valid ID.")

    # Display the person's name and birthday.
    displayPerson(id, data_dict)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
