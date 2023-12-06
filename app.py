from flask import Flask, render_template, request
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import re
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

nltk.downloader.download('vader_lexicon')

app = Flask(__name__)

# Load your saved DataFrame
df = pd.read_csv(r"C:\Users\Abhiram P\Desktop\FlipkartReviews\Iphone14.csv")

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()


# Function to clean and get sentiment score
def get_sentiment_score(review):
    review = review.lower()
    review = re.sub(r'[^a-zA-Z\s]', '', review)
    return sia.polarity_scores(review)['compound']


# Function to scrape reviews from a given URL
def scrape_reviews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = []
    ratings = []

    # Modify this based on the structure of the reviews page
    review_elements = soup.find_all('div', class_='review')

    for review_element in review_elements:
        rating = float(review_element.find('span', class_='rating').text)
        summary = review_element.find('p', class_='summary').text.strip()

        ratings.append(rating)
        reviews.append(summary)

    return ratings, reviews


# Flask route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        rows = soup.find_all('div', attrs={'class': 'col _2wzgFH K0kLPL'})
        customer_df = pd.DataFrame(columns=['Product name', 'Rating', 'Summary', 'Review'])
        for row in rows:
            sub_row = row.find_all('div', attrs={'class': 'row'})
            rating = sub_row[0].find('div').text
            summary = sub_row[0].find('p').text
            review = sub_row[1].find_all('div')[1].text
            product_name = soup.find('div', attrs={'class': '_2s4DIt _1CDdy2'})
            customer_df.append({'Product name': product_name, 'Rating': rating, 'Summary': summary, 'Review': review}, ignore_index=True)


        customer_df['sentiment_score'] = customer_df['Review'].apply(get_sentiment_score)

        average_sentiment = customer_df['sentiment_score'].mean()
        rating_out_of_5 = (average_sentiment + 1) * 2.5
        customer_rating = customer_df['Rating'].mean()
        # Generate word clouds for positive and negative reviews
        positive_reviews = ' '.join(customer_df[customer_df['sentiment_score'] > 0]['Review'])
        wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(positive_reviews)

        negative_reviews = ' '.join(customer_df[customer_df['sentiment_score'] < 0]['Review'])
        wordcloud_negative = WordCloud(width=800, height=400, background_color='white').generate(negative_reviews)

        # Render the template with the data
        return render_template('result.html', average_customer_rating=customer_rating, sentiment_rating=rating_out_of_5,
                               positive_wordcloud=wordcloud_positive.to_html(),
                               negative_wordcloud=wordcloud_negative.to_html(),
                               table_data=customer_df.to_html())

    # Render the main page
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error_message='Page not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
