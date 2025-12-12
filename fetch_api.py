import requests
import pandas as pd

def fetch_api_data():
    # Public API URL that returns TODO task data
    api_url = 'https://jsonplaceholder.typicode.com/todos'

    # Send GET request
    response = requests.get(api_url)

    # Check if request was successful (status_code 200)
    if response.status_code == 200:

        # Convert JSON response into a Python list
        api_data = response.json()[:9]

        # Convert list of dictionaries into a DataFrame
        api_df = pd.DataFrame(api_data)[['userId', 'title', 'completed']]

        # Rename columns to match your database naming style
        api_df.rename(
            columns={
                'userId': 'emp_id',
                'title': 'task_title',
                'completed': 'task_done'
            },
            inplace=True
        )

        return api_df
    
    else:
        # Return an empty DataFrame if API fails
        return pd.DataFrame(columns=['emp_id', 'task_title', 'task_done'])


# --------------------------------------------------
# Runs only when file is executed directly
# --------------------------------------------------
if __name__ == "__main__":
    api_df = fetch_api_data()
    print(api_df)
