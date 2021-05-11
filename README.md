# Social Media Language Scrape
![programming](https://online.csp.edu/wp-content/uploads/2019/02/Programming-Languages-for-Beginners-CSP.png)
****

## About the Project

****

Natural Language Processing (NLP) uses programming & machine learning techniques to help understand and make use of large amounts of text data.


For this project, I will be scraping data from GitHub repository README files in order to build a model that can predict what programming language a repository is, given the text of the README file.

### Objectives for this project include:
- Building a dataset based on a list of GitHub repositories to scrape, and writing the python code necessary to extract the text of the README file for each page, and the primary language of the repository.
- Documenting process and analysis throughout the data science pipeline.
- Constructing a classification model that can predict what programming language a repository is in, given the text of the README file.
- Deliverables:
    - A well-documented jupyter notebook that contains my analysis.
    - One or two content slides suitable for a general audience that summarize findings with a well-labeled visualization included in slides.

**** 

### Initial hypotheses
- What are the most frequently occuring words in READMEs?
- Are there any words that uniquely identify a programming language?
- What are the top word combinations (bigrams and trigrams)?

****

### Data Dictionary

Feature      | Description   | Data Type
------------ | ------------- | ------------
repo | GitHub repositories webpage | object 
clean_content | Cleaned text from README files of GitHub repositories | object
language | Programming language used in README files of GitHub repositories | object 

****

### Pipeline Process:

#### Plan
- Understand project description and goals. 
- Form hypotheses and brainstorm ideas.
- Have all necessary imports ready for project.

#### 1. Acquire
- Scrape the README files from Github repositories.
- Functions to acquire the data are included in [acquire.py](https://github.com/aliciag92/nlp-project/blob/main/acquire.py).

#### 2. Prepare
- Normalize text, clean, tokenize, lemmatize and remove stopwords.
- Split the data into train, validate, test.
- Functions to prepare the data are included in [prepare.py](https://github.com/aliciag92/nlp-project/blob/main/prepare.py).

#### 3. Explore
- Address questions posed in planning and brainstorming and figure out drivers to predict home values.
- Create visualizations (as many as needed).
- Summarize key findings and takeaways.

#### 4. Model/Evaluate
- Establish and evaluate a baseline model.
- Generate various classification algorithms and settle on the best algorithm by comparing evaluation metrics.
- Choose the best model and test that final model on out-of-sample data.
- Summarize performance, interpret, and document results.

#### 5. Deliver
- The best performing model uses a Decision Tree algorithm and TF-IDF to vectorize the text.
- The model increased from a baseline accuracy of 38% to 50% accuracy on out-of-sample data.
- The models are overfit as they performed well on training data initially. However, the models' accuracies significantly decreased when testing on validate (out-of-sample) data.
- Additionally, the models do not do a good job in predicting programming languages like HTML, PHP, and TypeScript. However, the final Decision Tree model does do a good job in predicting if the text from a GitHub repository's README file is either Python or JavaScript.
- It is also evident that README files for Python are better predictors than for JavaScript.
- Summarization of findings can be found here in my [report summary](https://docs.google.com/presentation/d/1j3zTydqPnEYJ2_No2I4rslAjM_WKgqBbzRsuY3LZ3yM/edit?usp=sharing). 

****
### Next Steps
- Gather higher quantity of READMEs from GitHub repositories.
- Create new features by implementing feature engineering.
- Run statistical testing.
- Conduct more modeling.

****

### Recreating Project
- To reproduce this project, download [acquire.py](https://github.com/aliciag92/nlp-project/blob/main/acquire.py), [prepare.py](https://github.com/aliciag92/nlp-project/blob/main/prepare.py), and [repo-language-report.ipynb](https://github.com/aliciag92/nlp-project/blob/main/repo-language-report.ipynb) in your working directory and follow the steps from the pipeline process above.
- Do any additional exploring, modeling, and evaluating of your own to deliver any new information!