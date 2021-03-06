## Inspiration
Students often do not have a financial background and want to begin learning about finance, but the sheer amount of resources that exist online make it difficult to know which articles are good for people to read. Thus we thought the best way to tackle this problem was to use a machine learning technique known as sentiment analysis to determine the tone of articles, allowing us to recommend more neutral options to users and provide a visual view of the different articles available so that users can make more informed decisions on the articles they read.

## What it does
This product is a web based application that performs sentiment analysis on a large scope of articles to aid users in finding biased, or un - biased articles. We also offer three data visualizations of each topic, an interactive graph that shows the distribution of sentiment scores on articles, a heatmap of the sentiment scores and a word cloud showing common key words among the articles.

## How we built it
Around 80 unique articles from 10 different domains were scraped from the web using scrapy. This data was then processed with the help of Indico's machine learning API. The API provided us with the tools to perform sentiment analysis on all of our articles which was the main feature of our product. We then further used the summarize feature of Indico api to create shorter descriptions of the article for our users. Indico api also powers the other two data visualizations that we provide to our users. The first of the two visualizations would be the heatmap which is also created through tableau and takes the sentimenthq scores to better visualize and compare articles and the difference between the sentiment scores. The last visualization is powered by wordcloud which is built on top of pillow and matplotlib. It takes keywords generated by Indico api and displays the most frequent keywords across all articles.The web application is powered by Django and a SQL lite database in the backend, bootstrap for the frontend and is all hosted on a google cloud platform app engine.

## Challenges we ran into
The project itself was a challenge since it was our first time building a web application with Django and hosting on a cloud platform. Another challenge arose in data scraping, when finding the titles of the articles, different domains placed their article titles in different locations and tags making it difficult to make one scraper that could abstract to many websites. Not only this, but the data that was returned by the scraper was not the correct format for us to easily manipulate so unpackaging dictionaries and such were small little tasks that we had to do in order for us to solve these problems. On the data visualization side, there was no graphic library that would fit our vision for the interactive graph, so we had to build that on our own!

## Accomplishments that we're proud of
Being able to accomplish the goals that we set out for the project and actually generating useful information in our web application based on the data that we ran through Indico API.

## What we learned
We learned how to build websites using Django, generate word clouds using matplotlib and pandas, host websites on google cloud platform, how to utilize the Indico api and researched various types of data visualization techniques. 

## What's next for DataFeels
Lots of improvements could still be made to this project and here are just some of the different things that could be done. The scraper created for the data required us to manually run the script for every new link but creating an automated scraper that built the correct data structures for us to directly pipeline to our website would be much more ideal. Next we would expand our website to have not just financial categories but any topic that has articles about it.

## How to run on localhost
1. Clone this in a local repository
2. Then run "pip install -r requirements.txt"
3. Then run "python manage.py runserver"