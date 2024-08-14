# Mobile Game A/B Testing Analysis

## Overview
This project evaluates two different level gate designs in the mobile game "Cookie Cats" to determine which one enhances player retention and engagement more effectively. The control group encounters a game gate at level 30, whereas the test group encounters it at level 40. Our goal is to assess which strategy leads to higher retention rates after one week of installation.

## Table of Contents
- [Installation](#installation)
- [Dataset](#dataset)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results and Discussion](#results-and-discussion)
- [Contributing](#contributing)
- [License](#license)

## Installation
To get started with this project, clone this repository and install the required packages.


## Dataset
The analysis is based on data collected from the game, including several key metrics:
- **userid**: Unique identifier for each player.
- **version**: Indicates whether the player was in the control group (`gate_30`) or the test group (`gate_40`).
- **sum_gamerounds**: The total number of game rounds played by the player during the first week after installation.
- **retention_1**: Whether the player came back and played the game 1 day after installing.
- **retention_7**: Whether the player returned to play 7 days after installing.

