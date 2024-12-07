#  Stock Movement Analysis Based on Social Media Sentiment
The primary goal of this project is to analyze the correlation between social media sentiment and stock market movements. By leveraging Natural Language Processing (NLP) techniques, the project aims to extract sentiments from user-generated content (e.g., Telegram messages) and assess their impact on stock price trends. Ultimately, the project seeks to build a model that can forecast stock price movements based on aggregated sentiment data, helping in decision-making for investments or market analysis.

### Python libraries and dependencies were likely used in this project:

1.scikit-learn

For machine learning models and evaluation metrics.

Key components:
GaussianNB, MultinomialNB, BernoulliNB
accuracy_score

2.nltk (Natural Language Toolkit)

For text preprocessing and natural language processing.

Key components:
stopwords

PorterStemmer

3.numpy

For numerical operations and handling arrays.
4.pandas

For data manipulation and handling datasets.

5.matplotlib 

For data visualization (if used for plotting).

6.TextBlob


The project performs the following tasks:

1.Data Collection: Gathered social media messages (e.g., Telegram) and stock market data.

2.Data Preprocessing: Cleaned and formatted text, timestamps, and stock data.

3.Sentiment Analysis: Used TextBlob to compute sentiment polarity and categorize as positive, negative, or neutral.

4.Feature Engineering: Created temporal features and aggregated sentiment scores.

5.Data Analysis: Explored correlations between sentiment trends and stock price movements.

6.Model Development: Built and evaluated predictive models for stock price trends based on sentiment.

7.Insights and Results: Derived actionable insights and evaluated sentiment impact on market trends.

### Machine Learning models trained and evaluated

The Following Machine Learning models trained and evaluated :

1.Gaussian Naive Bayes (GaussianNB)

2.Multinomial Naive Bayes (MultinomialNB)

3.Bernoulli Naive Bayes (BernoulliNB)

### Best Performing Machine learning Model

Bernoulli Naive Bayes (BernoulliNB) is found to be the best Performing Classifier with:

Accuracy:0.6578947368421053







