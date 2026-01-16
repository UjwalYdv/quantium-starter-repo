import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("output.csv")

# Convert date column to datetime and sort
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales"},
)

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    [
        html.H1("Pink Morsel Sales Analysis"),
        html.P(
            "This chart shows total Pink Morsel sales over time. "
            "It can be used to assess whether sales were higher before or after "
            "the price increase on 15 January 2021."
        ),
        dcc.Graph(figure=fig),
    ]
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
