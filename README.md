[![Heroku - App](https://img.shields.io/static/v1?label=Heroku&message=App&color=2ea44f&logo=heroku)](https://nameless-plains-67729.herokuapp.com/)
[![FlaskAPI - ML](https://img.shields.io/static/v1?label=FlaskAPI&message=ML&color=2ea44f&logo=github)](https://github.com/arslan-enes/VideoGameRecommendation)
[![Kaggle -   ](https://img.shields.io/static/v1?label=Kaggle&message=++&color=2ea44f&logo=kaggle)](https://www.kaggle.com/enesarslan8)
[![LinkedIn -   ](https://img.shields.io/static/v1?label=LinkedIn&message=++&color=2ea44f&logo=linkedin)](https://www.linkedin.com/in/arslannenes/)

# Video Game Recommender

This project aims to develop a video game recommendation system that suggests game recommendations to users based on similarity between summary and critic reviews of the games and the provided text. The recommendation system uses a pre-filled embedding space that includes summaries and critic reviews from a wide range of PC games throughout history. The system utilizes this information to generate personalized game recommendations by finding the closest matches to the user's input in the embedding space using a KNN model. 

The machine learning process is handled separately in another service. The Django app sends requests and receives a list of recommended game IDs. Then, the app retrieves the game information from a MongoDB database using those IDs and displays it to the user.


![image](https://github.com/arslan-enes/VideoGameRecommender-App/assets/84344512/ac03842f-f30d-4440-b205-359c657b485c)


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Finding new video games to play can be overwhelming, especially with the vast number of options available. The video game recommendation project addresses this issue by leveraging machine learning techniques to offer personalized game recommendations to users. By analyzing user preferences, gaming history, and other relevant factors, the system can suggest games that are likely to align with the user's interests.

## Features

The video game recommendation project includes the following features:

1. User Registration: Users can create an account and provide their preferences and gaming history to receive personalized recommendations.
2. Game Database: The project maintains a comprehensive database of video games, including information such as genre, platform, release date, and user ratings.
3. Recommendation Engine: By analyzing user data and game information, the recommendation engine generates accurate and relevant game suggestions for each user.
4. User Feedback: Users can provide feedback on recommended games, helping to further refine the recommendation engine and improve future suggestions.
5. User Interface: The project provides a user-friendly interface for users to interact with the system, view recommendations, and manage their preferences.

## Requirements

To run the video game recommendation project, you need the following:

- Python (version 3.6 or later)
- Flask (web framework)
- PostgreSQL (relational database)
- SQLAlchemy (Python SQL toolkit and Object-Relational Mapper)
- Scikit-learn (machine learning library)
- Pandas (data manipulation library)
- NumPy (numerical computing library)
- Other dependencies as specified in the project files

## Installation

Follow these steps to set up the video game recommendation project:

1. Clone the repository: `git clone https://github.com/your-username/video-game-recommendation.git`
2. Navigate to the project directory: `cd video-game-recommendation`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up the PostgreSQL database and update the configuration in the project files.
5. Run the database migrations to create the required tables: `flask db upgrade`
6. Start the application: `flask run`

## Usage

Once the project is set up and running, you can access the web interface by opening a web browser and navigating to `http://localhost:5000`. From there, users can register, provide their preferences, and receive personalized game recommendations. Users can also explore the game database, view game details, and provide feedback on recommended games.

## Contributing

Contributions to the video game recommendation project are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request on the project's GitHub repository.

## License

The video game recommendation project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code as per the terms of the license.
