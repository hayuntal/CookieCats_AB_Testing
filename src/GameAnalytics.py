class GameAnalytics:
    """
    Provides analytics functionalities for game data stored in a PostgreSQL database.

    Attributes:
        postgres_client: A client instance for interacting with the PostgreSQL database.
    """

    def __init__(self, postgres_client):
        """
        Initializes the GameAnalytics class with a PostgreSQL client.

        Parameters:
            postgres_client: The database client used to execute SQL queries.
        """
        self.postgres_client = postgres_client

    def get_data(self):
        """
        Retrieves all data from the 'data_tbl' table in the PostgreSQL database.

        Returns:
            A list containing the retrieved data rows if any data is found, otherwise None.

        Prints an error message if no data is found or an exception occurs during the query execution.
        """

        try:
            query = "SELECT * FROM data_tbl"
            data = self.postgres_client.execute_query(query)

            if data:
                return data

            else:
                print("No data found.")

        except Exception as e:
            print(f"Error retrieving data: {e}")
            return None
