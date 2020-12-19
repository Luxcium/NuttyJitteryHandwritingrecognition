from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import math

dividend_name = input('Which stock dividend you want invest in? ')
money_amount = input('How many $CAD you want to invest? ')

# WEBSCRAP
theurl = f"https://tsx.exdividend.ca/s/?q={dividend_name}"
req = Request(theurl, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
dividendinfos = page_soup.find_all("td")
shares_amount = int(money_amount) / float(dividendinfos[13].text)
shares_amount_truncate = math.trunc(shares_amount)
s_a_t = shares_amount_truncate
dividend_amount = float(dividendinfos[7].text)
yield_ = (dividendinfos[5].text)

textq = (dividendinfos[6].text)
result = textq.startswith(' Q')
if result == True:
 shares_times_div_amount = (int(s_a_t)* float(dividend_amount)*4)
 annual_dividend = (round(shares_times_div_amount, 2))
textm = (dividendinfos[6].text)
result = textm.startswith(' M')
if result == True:
 shares_times_div_amount = (int(s_a_t)* float(dividend_amount)*12)
 annual_dividend = (round(shares_times_div_amount, 2))

print(
    f'If you buy now, with {money_amount}$ into \"{dividend_name}\" stock you will get {shares_amount_truncate} shares and make {annual_dividend}$ per year with a yield of {yield_}.'
)
