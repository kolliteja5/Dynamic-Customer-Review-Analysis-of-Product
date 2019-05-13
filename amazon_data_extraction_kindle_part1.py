import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import requests
from bs4 import BeautifulSoup as bs
import nltk
from nltk.corpus import stopwords
stopwords_ = set(stopwords.words('english'))
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.downloader.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()
positive_words = []
negative_words = []
neutral_words = []
#print(stopwords_)

#reading the parameter file for the specific path:
data = pd.ExcelFile("parameter_file.xlsx")
df = data.parse("Sheet1")
URL = []

URL = df["URL"].tolist()[0]
#print(URL)
#print(df.columns)
attrs =  df["Class_Name"].tolist()
#print(attrs)





kindle_reviews = []

for i in range(df["No_Pages_Extract"][0],df["No_Pages_Extract"][1]):
    ip = []
    
    url = URL
    response = requests.get(url)
    soup = bs(response.content,"html.parser")
    reviews = soup.findAll("span",attrs=attrs)
    for i in range(len(reviews)):
        ip.append(reviews[i].text)
    kindle_reviews = kindle_reviews+ip
    
with open("kindle_reviews_original_output.txt","w",encoding='utf8') as output:
    output.write(str(kindle_reviews))
    
#joining all the reviews into single paragraph
ip_rev_string  = " ".join(kindle_reviews)

#removing unwanted symbols if exist:
ip_rev_string = re.sub("[^A-Za-z" "]+"," ", ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ",ip_rev_string)

#words that contain in iphone 7  reviews:
ip_reviews_words = ip_rev_string.split(" ")

#stopwords_ = stopwords_.split("\n")

temp = ["This", "is", "awsome", "Data", "Science"]
[i for i in temp if i not in "is"]

ip_reviews_words = [w for w in ip_reviews_words if not w in stopwords_]

ip_rev_string = " ".join(ip_reviews_words)
#print(ip_reviews_words)
"""
#generating the overall wordcloud:
wordcloud_ip = WordCloud(
                            background_color = 'black',
                            width = 1800,
                            height = 1400,
                            ).generate(ip_rev_string)
plt.imshow(wordcloud_ip)
"""

for word in ip_reviews_words:
    if(sid.polarity_scores(word)['compound']) >= 0.5:
        positive_words.append(word)
    elif(sid.polarity_scores(word)['compound']) <= -0.5:
        negative_words.append(word)
    else:
        neutral_words.append(word)
        
#print(positive_words)
positive_words_string = " ".join(positive_words)
#print(positive_words_string)
negative_words_string = " ".join(negative_words)
#print(negative_words_string)
neutral_words_string = " ".join(neutral_words)
#print(neutral_words_string)

#generating the overall wordcloud:
def diagram(df):
    wordcloud_ip = WordCloud(
                            background_color = 'black',
                            width = 1800,
                            height = 1400,
                            ).generate(df)
    return plt.imshow(wordcloud_ip)

#diagram(negative_words_string)
#diagram(positive_words_string)
diagram(neutral_words_string)





    