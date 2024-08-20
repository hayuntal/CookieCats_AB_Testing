# Game Analytics Project

![Cookie Cats](.img1.png)

## Table of Contents

1. [Overview](#overview)
2. [About the Game](#about-the-game)
3. [Project Objectives](#project-objectives)
4. [Dataset](#dataset)
5. [Methodology](#methodology)
6. [Results](#results)
7. [Tools Used](#tools-used)
8. [Setup and Installation](#setup-and-installation)


## Overview
This project focuses on A/B testing for the popular mobile game **Cookie Cats** to understand how different game designs impact player retention and engagement.
The data is loaded from a PostgreSQL database, which serves as a robust platform for handling and storing extensive gameplay data.
Python scripts are then utilized for further data manipulation, executing queries, and visualizing data distributions.
This integrated approach allows for a detailed analysis of game rounds and user interactions, aiming to provide actionable insights that can help optimize the game's features and improve player experience.


## About the Game 

### Rules
Cookie Cats is a puzzle game where players match three or more of the same colored cats to clear them from the board and earn points. The game features several levels, each with unique challenges and objectives. 

Players must strategically pop the cats to complete each level’s specific goals, such as reaching a certain score or clearing special tiles. Power-ups and special items can be collected and used to enhance gameplay or get out of tough spots. The game progresses in difficulty as more complex layouts and limitations are introduced.


### The video Game
[![Watch the Video of Game Play](https://img.youtube.com/vi/GaP5f0jVTWE/0.jpg)](https://www.youtube.com/watch?v=GaP5f0jVTWE)  
<em>Cookie Cats - Launch! (YouTube)</em>




## Project Objectives

- **Analyze Player Engagement**: Evaluate how changes in the game affect player engagement levels.
- **Test Game Features**: Conduct A/B tests on various game features to determine their impact on user retention.
- **Data-Driven Decisions**: Assist the game developers in making informed decisions based on the analysis results.

## Dataset

The dataset used in this project consists of the following columns:

- **`userid`**: Unique identifier for each user.
- **`version`**: The version of the game the user was exposed to during the A/B test (A - `gate_30`, B - `gate_40`).
- **`sum_gamerounds`**: The total number of game rounds played by the user during the first 14 days after installation.
- **`retention_1`**: Whether the user came back and played the game 1 day after installing it (True or False).
- **`retention_7`**: Whether the user came back and played the game 7 days after installing it (True or False).


## Methodology
This section details the statistical methods and processes used in the A/B testing, including:

- Data collection and preprocessing (Data Cleaning and EDA)
- Definition of control and test groups 
- Statistical tests performed (Shapiro, Levene and T-Test)
- Criteria for success evaluation

## Results
A summary of the A/B testing results, including key findings on how different variables influenced player behavior. This section will also discuss the statistical significance of the results and their implications for game development.

## Tools Used
- PostgreSQL: Used for storing and managing user data.
- Python: For data manipulation and statistical analysis.
- SQL: For data querying.
- Git: For version control.

## Setup and Installation

Follow these steps to get the project set up and running on your local machine:

### Prerequisites
Make sure you have PostgreSQL and Python installed. You'll also need to install any required Python libraries which can be found in a `requirements.txt` file in the repository.

### Environment Variables
Set up the following environment variables required for the application to connect to your PostgreSQL database:
- **`POSTGRES_DB`**: The name of your PostgreSQL database.
- **`POSTGRES_HOST`**: The host address of the PostgreSQL server (e.g., localhost if running locally).
- **`POSTGRES_PASS`**: The password for accessing the PostgreSQL database.
- **`POSTGRES_USER`**: The username for accessing the PostgreSQL database.

You can set these environment variables in your operating system, or you can use a `.env` file and load them within your application using a library like python-dotenv.

### Clone the Repository
Clone the repository and navigate into it:

   ```bash
   git clone https://github.com/hayuntal/CookieCats_AB_Testing.git
   cd CookieCats_AB_Testing
   ```

### Load Data into PostgreSQL
Transfer `cookie_cats.csv` file (exists into data directory) into the PostgreSQL database, you can use a script or a databse tool that supports CSV imports.
Ensure you create a table named `data_tbl`.
