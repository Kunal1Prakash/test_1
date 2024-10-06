import streamlit as st
import pandas as pd

# Load your CSV files
#kyb_dump = pd.read_csv('kyb_dump.csv')
merged_df= pd.read_csv('Overall_Enterprise_Base.csv')

# Merge the data on 'mid' column
#merged_df = pd.merge(kyb_dump, overall_enterprise, left_on='mid', right_on='pg_mid')
# Streamlit app layout
st.title("MID Lookup Tool")

# Create a dropdown for selecting MID
unique_mids = merged_df['pg_mid'] # Get unique MIDs from merged dataframe
selected_mid = st.selectbox("Select MID:", unique_mids)

# Show results when a MID is selected
if selected_mid:
    result = merged_df[merged_df['pg_mid'] == selected_mid]
    if not result.empty:
        st.write(result)  # Display the filtered result
    else:
        st.write("No results found for MID:", selected_mid)
