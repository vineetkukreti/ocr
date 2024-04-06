from bs4 import BeautifulSoup

# Assuming your HTML content is stored in a file named "your_html_file.html"
with open("templates\\result.html", "r") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the table within the specified div class
div_content = soup.find("div", class_="content-container")
table = div_content.find("table")

# Extract data from the table
if table:
    rows = table.find_all("tr")
    for row in rows:   
        columns = row.find_all("td")
        for column in columns:
            print(column.text.strip())  # or do something else with the data
else:
    print("Table not found.")
