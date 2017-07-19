import bs4 as bs
import urllib.request
import sys

def main():
    sign = sys.argv[1]
    sauce = urllib.request.urlopen('https://www.astrology.com/horoscope/daily/' + sign + '.html')
    soup = bs.BeautifulSoup(sauce, 'lxml')
    horoscopo = soup.find('div' , {'class': 'page-horoscope-text'})

    print(soup.title.text)
    print(horoscopo.get_text())

if __name__ == "__main__" : main()
