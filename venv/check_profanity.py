import urllib.request
import  io

def read_text():
    quotes = open("D:\\1marabcoders\\full stack\\movie_quotes\\movie_quotes.txt")
    content_of_file = quotes.read()
    print(content_of_file.replace(' ','%20'))
    quotes.close()
    check_profanity(content_of_file)

def check_profanity(text_to_check):
    u =urllib.request.urlopen("http://www.wdylike.appspot.com/?q=--%20Houston,%20we%20have%20a%20problem.%20(Apollo%2013)",data= None)
    f = io.TextIOWrapper(u, encoding='utf-8')
    text = f.read()
    print(text)


read_text()