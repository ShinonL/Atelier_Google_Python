from bs4 import BeautifulSoup
import requests
import pandas as pd


dataset = []
for date in range(20, 28):
    r = requests.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{date}-ianuarie-ora-13-00/")
    link = BeautifulSoup(r.text, "html.parser")

    table = link.find_all('table', attrs={'width': '710'})
    print(table)
    headers = []
    
    for i in table:
        for tbody in i.find_all('tbody'):
            rows = []
            for tr in tbody.find_all('tr'):
                if tr.find_all('td'):
                    headers = [td.get_text() for td in tr.find_all('td')]
                    for column in range(0, len(headers)):
                        translations = headers[column].maketrans("ăîâșț", "aiast")
                        headers[column] = headers[column].translate(translations)
                    dataset.append(headers)
    # dataset[-1].insert(0, f"{date}-jan")

df = pd.DataFrame(dataset)
df.to_csv('Covid_Information.csv')