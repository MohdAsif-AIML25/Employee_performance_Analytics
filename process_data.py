import pandas as pd
from fetch_sql import fetch_sql_data
from fetch_api import fetch_api_data

def merge_and_calculate():
    # --------------------------------------------------
    # 1️⃣ Load data from database + API
    # --------------------------------------------------
    sql_df = fetch_sql_data()     # Employee & performance data
    api_df = fetch_api_data()     # External API task data
    
    # --------------------------------------------------
    # 2️⃣ Convert boolean 'task_done' to integer (True=1, False=0)
    # --------------------------------------------------
    api_df['task_done'] = api_df['task_done'].astype(int)

    # --------------------------------------------------
    # 3️⃣ Summarize API data
    # Group by employee (emp_id) and count completed tasks
    # --------------------------------------------------
    api_summary = (
        api_df.groupby('emp_id')['task_done']
              .sum()
              .reset_index()
    )
    api_summary.rename(columns={'task_done': 'tasks_from_api'}, inplace=True)

    # --------------------------------------------------
    # 4️⃣ Merge SQL + API summary data
    # --------------------------------------------------
    merged_df = pd.merge(sql_df, api_summary, on='emp_id', how='left')

    # Fill missing API values with 0 (meaning no tasks found)
    merged_df['tasks_from_api'] = merged_df['tasks_from_api'].fillna(0)

    # --------------------------------------------------
    # 5️⃣ Calculate task efficiency
    # Formula:
    # (tasks from DB + tasks from API) / hours worked
    # --------------------------------------------------
    merged_df['task_efficiency'] = (
        merged_df['tasks_completed'] + merged_df['tasks_from_api']
    ) / merged_df['hours_worked']

    # --------------------------------------------------
    # 6️⃣ Debug Prints (optional)
    # --------------------------------------------------
    print("SQL DataFrame:")
    print(sql_df)
    print("\nAPI DataFrame:")
    print(api_df)
    print("\nMerged DataFrame:")
    print(merged_df)

    return merged_df

# --------------------------------------------------
# Runs only when executed directly
# --------------------------------------------------
if __name__ == "__main__":
    df = merge_and_calculate()
    print("\nFinal DataFrame returned:")
    print(df)
