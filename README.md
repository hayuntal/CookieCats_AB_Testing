# Game Analytics Project

## Overview
This project is designed to provide robust analytics on game data for the mobile game **Cookie Cats**. The focus is on analyzing user engagement and retention through game rounds using a PostgreSQL database. It consists of several Python scripts that manage database connections, execute queries, and visualize data distributions.

## Repository Structure

### Modules

- **`GameAnalytics.py`**: Contains the `GameAnalytics` class, which interfaces with a PostgreSQL database to retrieve game-related data and perform analytical operations.

- **`PostgresClient.py`**: Manages database connections, allowing for the execution of queries and handling of database interactions. It utilizes environment variables to manage database credentials securely.

- **`utilis.py`**: Includes functions for visualizing data distributions. It provides detailed histograms and boxplots to compare game rounds across different user groups.

- **`main.ipynb`**: A Jupyter notebook that demonstrates how to use the functionalities provided by the other scripts in practical scenarios.

### Features

- **Data Retrieval**: Fetch game data from a PostgreSQL database efficiently.
- **Data Visualization**: Generate histograms and boxplots to analyze the distribution of game rounds between control and test groups.
- **Database Interaction**: Connect, execute queries, and close connections with robust error handling.

## Installation

To set up this project:

1. Ensure Python and PostgreSQL are installed on your system.
2. Clone this repository.
3. Install required Python packages:
   ```bash
   pip install psycopg2 matplotlib
   ```
4. Set up the necessary environment variables for database access:
- **POSTGRES_HOST**: The hostname of your PostgreSQL server.
- **POSTGRES_USER:** Your database username.
- **POSTGRES_PASS:** Your database password.
- **POSTGRES_DB:** The database name.

## Contributing
Contributions to this project are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.



