import psycopg2
import os


class PostgresClient:
    """
    Manages connections to a PostgreSQL database, allowing for executing queries and handling the database interaction.

    This class provides methods to connect to the database, execute queries, and close the connection.
    """

    def __init__(self):
        """
        Initializes the PostgresClient with database configuration loaded from environment variables.
        """
        self.host = os.getenv("POSTGRES_HOST")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASS")
        self.database = os.getenv("POSTGRES_DB")

        self.connection = None
        self.cursor = None

        if None in [self.host, self.user, self.password, self.database]:
            print("Database configuration is incomplete. Please check environment variables.")
        else:
            print("Database configuration loaded successfully")

    def connect(self):
        """
        Establishes a connection to the PostgreSQL database using the loaded credentials.
        """
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Successfully connected to PostgreSQL")

        except psycopg2.Error as e:
            print("Error while connecting to PostgreSQL: %s", str(e))
            raise e

    def execute_query(self, query, params=None):
        """
        Executes a SQL query using an active database connection. Returns fetched data or the affected row count.
        """
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, params)
                if cursor.description:
                    return cursor.fetchall()
                else:
                    return cursor.rowcount
            except psycopg2.Error as e:
                print(f"Error executing query: {e}")
                raise

    def close(self):
        """
        Closes the database connection and cursor, ensuring all resources are properly released. Confirms closure.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("PostgreSQL connection is closed")
