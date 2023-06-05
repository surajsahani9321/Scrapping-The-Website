import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the "Search Postings" heading
search_heading = soup.find('h2', text='Search Postings')

# Check if the search heading exists
if search_heading:
    # Find the table containing the postings
    table = search_heading.find_next('table')
    
    # Find all the rows in the table
    rows = table.find_all('tr')
    
    # Extract the first 5 postings
    postings = rows[1:6]
    
    # Iterate over the postings and extract the required fields
    for posting in postings:
        columns = posting.find_all('td')
        est_value_notes = columns[0].text.strip()
        description = columns[1].text.strip()
        closing_date = columns[2].text.strip()

        # Print the extracted fields
        print('Est. Value Notes:', est_value_notes)
        print('Description:', description)
        print('Closing Date:', closing_date)
        print('---')
else:
    print('Search Postings heading not found.')

