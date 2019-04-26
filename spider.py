from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

page=1
while(page<4):
    url = "https://www.coolfunnyquotes.com/category/short-funny-quotes/"+str(page)+"/"
    urlAsHtml=urlopen(url).read()
    htmlPage=bs(urlAsHtml,"html.parser")
#print(htmlPage.p)
    quotes=htmlPage.findAll("p",{"class":"quote"})
    for q in quotes:
        quote=q
        print("quotes from the page "+str(page))
        print(quote.text)
    page+=1

