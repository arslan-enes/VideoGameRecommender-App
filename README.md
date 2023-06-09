[![Heroku - App](https://img.shields.io/static/v1?label=Heroku&message=App&color=2ea44f&logo=heroku)](https://nameless-plains-67729.herokuapp.com/)
[![FlaskAPI - ML](https://img.shields.io/static/v1?label=FlaskAPI&message=ML&color=2ea44f&logo=github)](https://github.com/arslan-enes/VideoGameRecommendation)
[![Kaggle - Dataset](https://img.shields.io/static/v1?label=Kaggle&message=Dataset&color=2ea44f&logo=kaggle)](https://www.kaggle.com/datasets/enesarslan8/metacritic-pc-games-of-all-time-2023-53k)
[![LinkedIn - Post](https://img.shields.io/static/v1?label=LinkedIn&message=Post&color=2ea44f&logo=linkedin)](https://www.linkedin.com/in/arslannenes/)

# Video Game Recommender

This project aims to develop a video game recommendation system that suggests game recommendations to users based on similarity between summary and critic reviews of the games and the provided text. The recommendation system uses a pre-filled embedding space that includes summaries and critic reviews from a wide range of PC games throughout history. The system utilizes this information to generate personalized game recommendations by finding the closest matches to the user's input in the embedding space using a KNN model. 

The machine learning process is handled separately in another service. The Django app sends requests and receives a list of recommended game IDs. Then, the app retrieves the game information from a MongoDB database using those IDs and displays it to the user.


![image](https://github.com/arslan-enes/VideoGameRecommender-App/assets/84344512/ac03842f-f30d-4440-b205-359c657b485c)


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technical](#technical)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

Finding new video games to play can be overwhelming, especially with the vast number of options available. The video game recommendation project addresses this issue by leveraging machine learning techniques to offer personalized game recommendations to users.

## Features

The video game recommendation project includes the following features:

1. Game Database: The project maintains a comprehensive database of video games, including information such as genre, platform, release date, and user ratings.
2. Recommendation Engine: By analyzing user input, the recommendation engine generates accurate and relevant game suggestions for each text.
3. User Interface: The project provides a user-friendly interface for users to interact with the system and view recommendations.

## Technical

Here are the top library and technologies used throughout the development:

- Python (Data Collection, Data Analysis, NLP Processing, ML Processing, Flask API, Django Application)
- Scrapy (Dataset crawled from the all-time PC games list of Metacritic)
- Pandas, Seaborn (Data analysis, wrangling operations)
- TensorFlow (Universal Sentence Encoder-Lite) (NLP model used to create an embedding space with information from game summaries and reviews)
- Scikit-learn (NearestNeighbors) (Machine Learning library used to find the nearest neighbors of user input)
- Flask-Restful (API that serves as a recommender, taking user text information and returning IDs of recommended games)
- Django-App (Simply posts requests to the Flask API with user text and retrieves results from the MongoDB database based on the ID)
- MongoDB (Database containing all the information about the games)
- HTML-CSS-Javascript (Web Page Interactions)


Please feel free to ask about the project from the social links provided at the top.
