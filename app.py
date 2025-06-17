import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Connect to your working database
conn = sqlite3.connect("data/mlb.db")
df = pd.read_sql_query("SELECT * FROM events", conn)
conn.close()

# Convert Value column to numeric (some are strings like ".390")
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

# Sidebar filters
st.sidebar.header("Filters")

statistic = st.sidebar.selectbox("Select a Statistic", sorted(df["Statistic"].dropna().unique()))
teams = ["All"] + sorted(df["Team"].dropna().unique())
selected_team = st.sidebar.selectbox("Select a Team", teams)

# Filter by Statistic
filtered_df = df[df["Statistic"] == statistic]

# Optional: filter by team
if selected_team != "All":
    filtered_df = filtered_df[filtered_df["Team"] == selected_team]

# Slider for value range
min_val = int(filtered_df["Value"].min()) if not filtered_df["Value"].isnull().all() else 0
max_val = int(filtered_df["Value"].max()) if not filtered_df["Value"].isnull().all() else 0
value_range = st.sidebar.slider("Filter by Value", min_val, max_val, (min_val, max_val))
filtered_df = filtered_df[(filtered_df["Value"] >= value_range[0]) & (filtered_df["Value"] <= value_range[1])]

# Title
st.title("MLB Top 25 Dashboard")

# Show filtered data
st.subheader(f"Filtered data for {statistic}")
st.dataframe(filtered_df)

# Bar chart
fig_bar = px.bar(filtered_df, x="Player", y="Value", color="Team", title="Bar Chart")
st.plotly_chart(fig_bar)

# Pie chart
fig_pie = px.pie(filtered_df, names="Player", values="Value", title="Pie Chart")
st.plotly_chart(fig_pie)

# Line chart
fig_line = px.line(filtered_df, x="Player", y="Value", title="Line Chart")
st.plotly_chart(fig_line)

