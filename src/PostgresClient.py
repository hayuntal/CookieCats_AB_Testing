import psycopg2
import os


class PostgresClient:
    def __init__(self):
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
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("PostgreSQL connection is closed")
