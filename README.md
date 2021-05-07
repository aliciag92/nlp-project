# Prediction of Home Values 
![programming](link to programming language header image)
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
- What does the distribution of IDFs look like for the most common words?
- Does the length of the README vary by programming language?
- Do different programming languages use a different number of unique words?
- What are the top word combinations (bigrams and trigrams)?

****

### Data Dictionary

Feature      | Description   | Data Type
------------ | ------------- | ------------
x |  x  | x 
x | x | x
x |  x  | x 
x |  x | x
x |  x  | x
x | x | x
x | x | x
x | x | x

****

### Pipeline Process:

#### Plan
- Understand project description and goals. 
- Form hypotheses and brainstorm ideas.
- Have all necessary imports ready for project.

#### 1. Acquire
- Scrape the README files from Github repositories.
- Functions to acquire the data are included in [acquire.py](link to acquire file).

#### 2. Prepare
- Normalize text, clean, tokenize, lemmatize and remove stopwords.
- Split the data into train, validate, test.
- Functions to prepare the data are included in [prepare.py](link to prepare file).

#### 3. Explore
- Address questions posed in planning and brainstorming and figure out drivers to predict home values.
- Create visualizations and run statistical tests (as many as needed).
- Summarize key findings and takeaways.

#### 4. Model/Evaluate
- Establish and evaluate a baseline model.
- Generate various classification algorithms and settle on the best algorithm by comparing evaluation metrics.
- Choose the best model and test that final model on out-of-sample data.
- Summarize performance, interpret, and document results.

#### 5. Deliver
- (*document results of classification report*)
- Summarization of findings can be found here in my [report summary](link to google slides). 


****

### Recreating Project
- To reproduce this project, download [acquire.py](link to acquire), [prepare.py](link to prepare file), and [repo-language-report.ipynb](link to jupy nb) in your working directory and follow the steps from the pipeline process above.
- Do any additional exploring, modeling, and evaluating of your own to deliver any new information!