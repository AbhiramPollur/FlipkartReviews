# Flipkart Product Reviews Analyzer 

##Overview
The Flipkart Product Reviews Analyzer is a Flask Web App designed to provide users with valuable insights into product reviews from Flipkart. Users an simply paste and upload the URL of a product's review page, and the app will generate a comparison between the average customer rating and the average sentiment analysis score of the reviews. Additionally, a table displaying essential information such as product name, customer rating, customer review and summary is presented.

##Features
**Review Comparison:** Get a quick overview of the product's average customer rating versus the sentiment analysis score out of 5.
**Detailed Table:** A table is generated with key details like product name, customer rating, customer review and summary.
**Wordclouds:** Positive and negative wordclouds offer a visual representation of sentiments within the reviews.

##Model Training
The sentiment analysis model is trained using a dataset comprising over 5000 reviews of the Iphone 14 left by customers which was scraped from flipkart.This ensures a robust understanding of customer sentiments specific to the product.

##Usage
1. Paste or upload the Flipkart product review page URL.
2. Click on the "Analyze" button.
3. Review the comparison, detailed table, and wordclouds for comprehensive understanding of the customer sentiments.

##Dependencies
Flask
BeautifulSoup
NLTK
TextBlob
Wordcloud

##Installation
1. Clone the repository
2. Install dependencies using 'pip install -r requirements.txt'
3. Run the Flask app with 'python app.py'

##Note
Ensure that you have the necessary permissionsto scrape data from Flipkartand abide by their terms of service.

##Contributors
Abhiram Pollur

Feel free to contribute and make the product review analysis even more insightful!
