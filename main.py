import requests
from bs4 import BeautifulSoup
import html
import codecs


req = requests.get("https://www.imdb.com/chart/toptv").text



soup = BeautifulSoup(req, "html.parser")
texted_titles = []
combined = []
href = []
titles = soup.select("td a")
years = soup.find_all("span", class_="secondaryInfo")
for tl in titles:
    if tl.getText() != " \n":
        try:
            href.append("https://www.imdb.com" + tl.get("href"))
            x = f'{len(texted_titles) + 1}> "{tl.getText()}"'
            texted_titles.append(html.unescape(x))
        except ValueError:
            href.append("https://www.imdb.com" + tl.get("href"))
            x = f'1** "{tl.getText()}"'
            texted_titles.append(x)
years_normalized = [html.unescape(str(year).split("(")[1].split(")")[0]) for year in years]
for i in range(len(texted_titles)):
    x = f"{texted_titles[i]}: {years_normalized[i]}, url: {href[i]}."
    combined.append(x)
print(combined)
with codecs.open("film.txt", "w", "utf-16") as l:
    for i in combined:
        if combined.index(i) == 0:
            l.writelines(f"{i}")
        else:
            l.writelines(f"\n{i}")

