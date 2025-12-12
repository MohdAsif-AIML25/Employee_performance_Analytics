import streamlit as st
from process_data import merge_and_calculate

def run_dashboard():
    # Run data processing pipeline
    df = merge_and_calculate()

    # --------------------------------------------------
    # Streamlit Dashboard Layout
    # --------------------------------------------------
    st.title("Employee Performance Dashboard")

    st.header("📊 Employee Performance Data")
    st.dataframe(df)

    st.header("⚡ Task Efficiency by Employee")
    st.bar_chart(df.set_index('name')['task_efficiency'])

    st.header("📝 Tasks Completed via API")
    st.bar_chart(df.set_index('name')['tasks_from_api'])

# --------------------------------------------------
# Runs when executing the file directly
# --------------------------------------------------
if __name__ == "__main__":
    run_dashboard()
