import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.de/-/de/GA03464-GB/dp/B0BDJ3ND5X/"
HEADERS = {"UserAgent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"} 

def trackPrices():
    price = float(getPrice()) #Preis einlesen
    if price > PRICE_VALUE: #wenn aktueller Preis größer als Zielpreis
        diff = int(price - PRICE_VALUE) #Berechnung wie viel über Zielpreis
        print(f"Still {diff} € too expensive!") #Ausgabe um wie viel zu teuer
    else:
        print("Cheaper!")
        #sendEmail()
    pass

def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    #price = soup.find(id='priceblock_ourprice').get_text().strip()[1:4] #geht nicht für Amazon.de
    #price = soup.find(id='a-price-hole').get_text()
    price = soup.find('span', id='a-price-hole').text.strip()
    print(title)
    print(price)
    #Converting the string to integer
    price = int(float(price))
    return price
    
if __name__ == "__main__":
    trackPrices()
