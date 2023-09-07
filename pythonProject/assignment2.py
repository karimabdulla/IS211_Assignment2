import argparse
import logging
import urllib
from datetime import datetime
def download_data(url):
  """Downloads the contents of the file located at the given URL.

  Args:
    url: The URL of the file to download.

  Returns:
    The contents of the file.
  """
  response = urllib.urlopen(url)
  return response.read()
def process_data(data, line_number=None):
  """Processes the data in the given string and returns a dictionary that maps
    a person's ID to a tuple of the form (name, birthday).

  Args:
    data: The data to process.

  Returns:
    A dictionary that maps IDs to tuples.
  """
  person_data = {}
  for line in data.splitlines():
    id, name, birthday = line.split(',')
    try:
      birthday_date = datetime.datetime.strptime(birthday, '%d/%m/%Y')
    except ValueError:
      # The birthday is in an invalid format.
      logging.error('Error processing line #%d for ID #%d', line_number, id)
      continue

    person_data[id] = (name, birthday_date)

  return person_data
def display_person(id, person_data):
  """Displays the name and birthday of the person with the given ID.

  Args:
    id: The ID of the person to display.
    person_data: A dictionary that maps IDs to tuples of the form (name, birthday).
  """
  if id not in person_data:
    print('No user found with that id')
    return

  name, birthday = person_data[id]
  print('Person #%d is %s with a birthday of %s' % (id, name, birthday))

  def main():
      parser = argparse.ArgumentParser()
      parser.add_argument('--url', required=True)
      args = parser.parse_args()

      # Download the data from the URL.
      data = download_data(args.url)

      # Process the data and create a dictionary that maps IDs to tuples.
      person_data = process_data(data)

      # Set up a logger to log errors.
      logging.basicConfig(filename='errors.log', level=logging.ERROR)

      # Get the user's input.
      while True:
          id = input('Enter an ID to lookup (0 to exit): ')
          if id <= 0:
              break

          display_person(id, person_data)

 if __name__ == '__main__':
              main() 