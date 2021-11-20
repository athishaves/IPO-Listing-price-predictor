import requests
from bs4 import BeautifulSoup
import csv


response = requests.get('https://www.moneycontrol.com/ipo/ipo-historic-table')

soup = BeautifulSoup(response.text, 'html.parser')

print('Classes of each table')
for table in soup.find_all('table'):
    print(table.get('class'))

table = soup.find('table', class_='tablesorter')

global headers
headers = [
    'Date', 'IPO_Name', 'Profile', 'Issue_Size',
    'QIB', 'HNI', 'RII', 'Total',
    'Bid_Price', 'Listing_Open', 'Listing_Close', 'Listing_Gains', 'CMP', 'Current_Gains'
]

contents = table.find_all('tr')[2:]

data = []
data.append(headers)

for row in contents:
    columns = row.find_all('td')
    
    if(columns != []):
        date = columns[0].text.strip()
        name = str(columns[1].text.strip())
        profile = str(columns[2].a['href'].strip())
        size = float(columns[3].text.strip().replace(',',''))
        
        qib = float(columns[4].text.strip().replace(',',''))
        hni = float(columns[5].text.strip().replace(',',''))
        rii = float(columns[6].text.strip().replace(',',''))
        total = float(columns[7].text.strip().replace(',',''))
        
        issue = float(columns[8].text.strip().replace(',',''))
        listing_open = float(columns[9].text.strip().replace(',',''))
        listing_close = float(columns[10].text.strip().replace(',',''))
        listing_gains = float(columns[11].text.strip().replace(',',''))
        cmp = float(columns[12].text.strip().replace(',',''))
        
        if columns[13].text.strip() == '': current_gains = 0.0
        else: current_gains = float(columns[13].text.strip().replace(',',''))

        data.append([
            date, name, profile, size,
            qib, hni, rii, total,
            issue, listing_open, listing_close, listing_gains, cmp, current_gains,
        ])

with open('ipo_history.csv', 'w') as filename:
    writer = csv.writer(filename)
    writer.writerows(data)