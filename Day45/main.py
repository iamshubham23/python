# from bs4 import BeautifulSoup
# import lxml
# with open("python/Day45/website.html") as file:
#     contents=file.read()
# soup=BeautifulSoup(contents,"lxml")    
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())

# all_anchor_tags=soup.find_all(name="a")
# # print(all_anchor_tags)
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))

# # heading=soup.find(name="h1",id="name")
# # print(heading)    
# # sub_heading=soup.find(name="h3",class_="heading")
# # print(sub_heading)
# name=soup.select_one(selector="#name")
# print(name)
# headings=soup.select(".heading")
# print("headings")


# from bs4 import BeautifulSoup
# import requests
# response=requests.get("https://thehackernews.com")
# yc_web_page=response.text
# article_texts=[]
# article_links=[]
# soup=BeautifulSoup(yc_web_page,"html.parser")
# print(soup.title)
# articles=soup.find_all(name="div",class_="home-desc")
# # print(articles.getText())for article_tags in articles:
# for article_tags in articles:
#     article_text=article_tags.getText()
#     article_texts.append(article_text)
# print(article_texts[1])

# # article_tag=soup.find(name="a",class_="story-link")
# # article_link=article_tag.get("href")
# # print(article_link)


from bs4 import BeautifulSoup
import requests
URL="https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(URL)
website_html=response.text
soup=BeautifulSoup(website_html,"html.parser")
all_movies=soup.find_all(name="h2")
movies_title=[movie.getText() for movie in all_movies ]
movies=movies_title[::-1]  #[::-1] is used for reversing the list /slice operator
# for n in range(len(movies_title)-1,0,-1):
#      movies=movies_title[n]

with open("python/Day45/movies.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
        