from bs4 import BeautifulSoup
import requests
response = requests.get(url="https://news.ycombinator.com/news")
Soup = BeautifulSoup(response.text, "html.parser")
Title = Soup.select(".titleline a")
Title2 = []
Link2 = []
for i in range(0,len(Title),2):
    Title2.append(Title[i].getText())
    Link2.append(Title[i].get("href"))
#Link = Title.get("href")
Upvotes = Soup.find_all(name="span", class_="score")
TitleUpvote = [int(T.getText().split()[0]) for T in Upvotes]
print(Title2)
print(Link2)
print(TitleUpvote)
Pos = 0
Max = TitleUpvote[0]
for i in range(len(TitleUpvote)):
    if TitleUpvote[i] > Max:
        Pos = i
        Max = TitleUpvote[i]
print(Title2[Pos])
print(Link2[Pos])
print(Max)