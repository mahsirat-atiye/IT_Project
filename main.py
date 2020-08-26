import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)

FOOLAD = "http://www.tsetmc.com/Loader.aspx?ParTree=151311&i=46348559193224090#"
page = requests.get(
    FOOLAD
)

print(page.status_code)

from bs4 import BeautifulSoup
from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# print(list(soup.children))


for script in soup.find_all('script'):
    # if "TradeHistory" in script.text:
    for line in script:
        scriptString = str(line)
        if "TradeHistory" in scriptString:
            TradeHistory = scriptString.split("\n")[1]
            TradeHistory = eval(TradeHistory[21: -2])
