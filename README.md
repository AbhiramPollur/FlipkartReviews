# Flipkart Product Reviews Analyzer 

## Overview

Welcome to the Flipkart Product Reviews Analyzer, which is a Flask Web App designed to provide users with valuable insights into product reviews from Flipkart. Users can simply paste or upload the URL of a product's review page, and the app will generate a comparison between the average customer rating and the average sentiment analysis score of the reviews. Additionally, a table displaying essential information such as product name, customer rating, customer review, and summary is presented.

## Features

- **Review Comparison:** Get a quick overview of the product's average customer rating versus the sentiment analysis score out of 5, so that the user can analyze the difference in the average customer rating and the sentiment analysis score out of 5, which helps the user in their decision on the purchase of the product.
- **Detailed Table:** Access a comprehensive table which is generated and includes the key details like product name, customer rating, customer review, and summary. The user can check the rating given by a particular customer and their rating to see if they co ordinate with each other.
- **Wordclouds:** Visualize sentiments within the reviews through positive and negative word clouds, which display the most used positive and negative words respectively in the word clouds, where the larger the word, the more the word is used.

## Model Training

The sentiment analysis model is trained using a dataset comprising over 5000 reviews of the iPhone 14 left by customers, which was scraped from Flipkart and stored in a csv file. This ensures a robust understanding of customer sentiments specific to the product. The code with which the reviews were scraped is accessible in the FlipkartReviews.py script. 

## Usage

1. Navigate to your desired folder where you want to clone the repository in the terminal.
2. Copy the repository link and type "git clone" and then paste the repository URL in the terminal.
3. Download the requirements by typing "pip install -r requirements.txt" in the same folder path where the repository is cloned.
4. Make sure to download the vader_lexicon package of nltk which is in the Flask app code.
5. Once the required dependencies are installed, run "python app.py".
6. Click on the link which directs you to the local web page and you see the home page of the app. 
7. Paste or upload the Flipkart product review page URL.
8. Click on the "Analyze" button.
9. Review the comparison, detailed table, and word clouds for a comprehensive understanding of customer sentiments.

## Dependencies

- Flask==2.2.5
- BeautifulSoup==0.0.1
- NLTK==3.8.1
- textblob==0.17.1
- Wordcloud==1.9.2
- pandas==2.1.0
- seaborn==0.13.0
- matplotlib==3.8.0
- tqdm==4.66.1
- urllib3==1.26.16

## Installation

1. Clone the repository.
2. Install dependencies using 'pip install -r requirements.txt'.
3. Before running the Flask app, make sure to download the nltk 'vader_lexicon' package which is in the code for the Flask app.
4. Run the Flask app with 'python app.py'.

## Note

Ensure that you have the necessary permissions to scrape data from Flipkart and abide by their terms of service.

## Contributors

Abhiram Pollur

Feel free to contribute and make the product review analysis even more insightful!

