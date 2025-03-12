from preswald import connect, get_df, table, text, slider, plotly
import plotly.express as px
import pandas as pd

connect()

# Corrected: using defined data source name from preswald.toml
df = get_df("list_of_orders")

# If it fails, use pandas directly:
if df is None:
    try:
        df = pd.read_csv("data/List of Orders.csv")
        text("✅ Loaded data using pandas directly.")
    except Exception as e:
        text(f"⚠️ Error loading data with pandas: {e}")
        df = None

if df is not None:
    text("# My Data Analysis App")

    threshold = slider("Threshold", min_val=1, max_val=len(df), default=10)
    filtered_df = df.head(threshold)
    table(filtered_df, title="Filtered Data")

    fig = px.scatter(
        filtered_df,
        x="Order Date",
        y="State",
        color="City",
        title="Orders Visualization"
    )
    plotly(fig)
else:
    text("⚠️ Dataset could not be loaded. Please check your CSV file again.")
