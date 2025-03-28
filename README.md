# Customer product reviews insights

In this project I am analysing a dataset with thousands of Amazon product reviews in order to understand customer sentiment and write a summary of products in each category. 

Dataset [Amazon product reviews](https://project-nlp-business-case-automated-customers-reviews-i9hz7yj4.streamlit.app/)

What was done:
- Data pre-processing: clean up missing values, clean up product names etc. 
- Sentiment analysis using Destilbert.
- Categorisation of products using keyword matching and LinearRegression.
- Artice for top 3 + worst product in each category using Chatgpt 3.5 API.
- Prompt-tuning.
- Deployment of a website with review summaries per category: [Reviews summaries](https://project-nlp-business-case-automated-customers-reviews-i9hz7yj4.streamlit.app/)

<img width="753" alt="Screenshot 2025-03-28 at 12 56 50" src="https://github.com/user-attachments/assets/8a48c549-31f6-4253-97c6-51b251956dd7" />


Files: 
- sentiment.ipynb: sentiment analysis
- categories.ipynb: categorisation
- review_summarisation.ipynb: write article per category
- app.py: deploy to a web page
- 
