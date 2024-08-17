import matplotlib.pyplot as plt
from PostgresClient import *

COLUMNS = ['userId', 'version', 'sum_gamerounds', 'retention_1', 'retention_7']


def show_distributions_gamerounds(data):
    data_control_group = data[data['version'] == 'control_group']['sum_gamerounds']
    data_test_group = data[data['version'] == 'test_group']['sum_gamerounds']
    groups_data = [group['sum_gamerounds'].tolist() for name, group in data.groupby('version')]

    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))

    axs[0].hist(data_control_group, bins=50, color='blue', alpha=0.7)
    axs[0].set_title('Distribution of Game Rounds - \n Control Group', fontsize=10)
    axs[0].set_xlabel('Number of Game Rounds')
    axs[0].set_ylabel('Frequency')

    axs[1].hist(data_test_group, bins=50, color='green', alpha=0.7)
    axs[1].set_title('Distribution of Game Rounds - \n Test Group', fontsize=10)
    axs[1].set_xlabel('Number of Game Rounds')
    axs[1].set_ylabel('Frequency')

    axs[2].boxplot(groups_data)
    axs[2].set_title('Boxplot of Game Rounds by Group', fontsize=10)
    axs[2].set_xlabel('Group')
    axs[2].set_ylabel('Number of Game Rounds')
    axs[2].set_xticklabels(data['version'].unique())

    plt.tight_layout()
    plt.show()


class GameAnalytics:
    def __init__(self, postgres_client):
        self.postgres_client = postgres_client

    def get_data(self):

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

    @staticmethod
    def get_columns():
        return COLUMNS
