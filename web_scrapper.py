import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia page URL for the largest US companies by revenue
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.text, "lxml")

    # Find the table in the page
    table = soup.find("table", {"class": "wikitable sortable"})

    # Extract the table headers
    headers = [header.text.strip() for header in table.find_all("th")]

    # Define empty list to store the data
    companies_data = []

    # Extract each row of the table
    for row in table.find_all("tr")[1:]: 
        cells = row.find_all("td")
        if len(cells) >= 6: 
            rank = cells[0].text.strip()  # Rank
            name = cells[1].text.strip()  # Company name
            industry = cells[2].text.strip()  # Industry
            revenue = cells[3].text.strip()  # Revenue
            revenue_growth = cells[4].text.strip()  # Revenue growth
            headquarters = cells[5].text.strip()  # Headquarters
            
            # Append the data to the list
            companies_data.append([rank, name, industry, revenue, revenue_growth, headquarters])

    # Convert the list into a Pandas DataFrame
    df = pd.DataFrame(companies_data, columns=["Rank", "Company", "Industry", "Revenue", "Revenue Growth", "Headquarters"])

    # Print the DataFrame
    print(df)

    # data save to CSV file
    df.to_csv("largest_us_companies_by_revenue.csv", index=False)
    print("Data has been saved to 'largest_us_companies_by_revenue.csv'")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")