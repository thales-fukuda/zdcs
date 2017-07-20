#!/usr/bin/python3

# Importing BeautifulSoup for scraping
import bs4 as bs
import urllib.request
import sys


# Check if a string contains another
def contain(string, word):
    index = 0
    for char in string:
        if char == word[index]:
            index += 1
        if index == len(word):
            return True
    return False


def main(): 
    # Available signs
    signs = ['aquarius', 'pisces', 'aries', 'taurus',
             'gemini', 'cancer', 'leo', 'virgo',
             'libra', 'scorpio', 'sagittarius', 'capricorn']

    # Getting the sign as parameter
    sign = sys.argv[1].lower()

    trigger = False
    # Check if parameter is a valid sign
    if sign not in signs:
        trigger = True

        # If it is not valid, try to check if it was misstyped
        for word in signs:
            if contain(sign, word) or contain(word, sign):
                sign = word
                trigger = False
    
    # If it is not similar to any sign name, terminate the program
    if trigger:
        print("\n   Parameter is not a sign, maybe you misstyped it")
        return

    # Getting the URL based on the sign and accessing it
    source = urllib.request.urlopen('https://www.astrology.com/horoscope/daily/' + sign + '.html')
    site = bs.BeautifulSoup(source, 'lxml')

    # Finding the div with  the prediction
    horoscope = site.find('div' , {'class': 'page-horoscope-text'})

    # Printing
    print("\n", site.title.text, "\n \n", horoscope.get_text(), "\n")
    
if __name__ == "__main__" : main()

