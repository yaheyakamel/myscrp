import requests
import bs4
counter = 0
url = f'https://www.banquemisr.com/ar-EG/Home/CAPITAL-MARKETS/Mutual-Funds'
page = requests.get(url)

soup = bs4.BeautifulSoup(page.content, "html.parser")
funds = []

funds = soup.findAll('div', {'class': "table-responsive"})

for j in range(len(funds)):

        counter += 1

        funds.append(print("Investment Funds :" + funds[j].text))

        print()
