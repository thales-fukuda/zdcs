#!/usr/bin/python3

# Importing BeautifulSoup for scraping
import bs4 as bs
import urllib.request
import sys

def main(): 
    # Getting the sign as parameter
    sign = sys.argv[1]
    
    # Getting the URL based on the sign and accessing it
    source = urllib.request.urlopen('https://www.astrology.com/horoscope/daily/' + sign + '.html')
    soup = bs.BeautifulSoup(source, 'lxml')

    # Finding the div with  the prediction
    horoscope = soup.find('div' , {'class': 'page-horoscope-text'})
    # Printing
    print("\n", soup.title.text, "\n \n", horoscope.get_text(), "\n")

if __name__ == "__main__" : main()

