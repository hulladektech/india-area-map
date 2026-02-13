import streamlit as st
import pandas as pd
import folium
import json
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(layout="wide")
st.title("India Area Mapping Dashboard")

# -----------------------------
# Load Excel Data
# -----------------------------
df = pd.read_excel("data.xlsx")

# -----------------------------
# Load GeoJSON (No GeoPandas)
# -----------------------------
with open("india_states.geojson", "r", encoding="utf-8") as f:
    geo_data = json.load(f)

# -----------------------------
# Sidebar Filter
# -----------------------------
district_list = sorted(df["District"].unique())
selected_district = st.sidebar.selectbox(
    "Select District",
    ["All India"] + district_list
)

# -----------------------------
# Create Base Map
# -----------------------------
if selected_district == "All India":
    m = folium.Map(location=[22.5937, 78.9629], zoom_start=5)
    filtered_df = df
else:
    filtered_df = df[df["District"] == selected_district]
    m = folium.Map(location=[22.5937, 78.9629], zoom_start=6)

# -----------------------------
# Add Boundary Layer
# -----------------------------
if selected_district != "All India":
    filtered_features = [
        feature for feature in geo_data["features"]
        if feature["properties"].get("dtname") == selected_district
    ]

    if filtered_features:
        folium.GeoJson(
            {"type": "FeatureCollection", "features": filtered_features},
            style_function=lambda x: {
                "fillColor": "#00000000",
                "color": "blue",
                "weight": 3
            }
        ).add_to(m)

# -----------------------------
# Add Area Markers
# -----------------------------
marker_cluster = MarkerCluster().add_to(m)

for _, row in filtered_df.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=8,
        popup=f"""
        <b>State:</b> {row['State']}<br>
        <b>District:</b> {row['District']}<br>
        <b>Area:</b> {row['Area']}
        """,
        color="blue",
        fill=True,
        fill_color="red",
        fill_opacity=0.7
    ).add_to(marker_cluster)

# -----------------------------
# Display Map
# -----------------------------
st_folium(m, width=1200, height=650)
