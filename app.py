import streamlit as st
import pandas as pd
import folium
import geopandas as gpd
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.title("India Area Mapping Dashboard")

# -----------------------------
# Load Excel Data
# -----------------------------
df = pd.read_excel("data.xlsx")

# -----------------------------
# Load District Boundary GeoJSON
# -----------------------------
districts = gpd.read_file("india_states.geojson")
districts = districts.rename(columns={"dtname": "District"})

# -----------------------------
# Sidebar Filter
# -----------------------------
district_list = df["District"].unique()
selected_district = st.sidebar.selectbox(
    "Select District",
    ["All India"] + list(district_list)
)

# -----------------------------
# Create Base Map
# -----------------------------
if selected_district == "All India":
    m = folium.Map(location=[22.5937, 78.9629], zoom_start=5)
    filtered_df = df
    filtered_boundary = None
else:
    filtered_df = df[df["District"] == selected_district]
    filtered_boundary = districts[districts["District"] == selected_district]

    if not filtered_boundary.empty:
        centroid = filtered_boundary.geometry.centroid.iloc[0]
        m = folium.Map(location=[centroid.y, centroid.x], zoom_start=11)
    else:
        m = folium.Map(location=[22.5937, 78.9629], zoom_start=5)

# -----------------------------
# Add Boundary (Only if selected)
# -----------------------------
if selected_district != "All India" and filtered_boundary is not None:
    folium.GeoJson(
        filtered_boundary,
        style_function=lambda x: {
            "fillColor": "#00000000",
            "color": "blue",
            "weight": 3
        }
    ).add_to(m)

# -----------------------------
# Add Area Markers (All visible by default)
# -----------------------------
marker_cluster = MarkerCluster().add_to(m)

for index, row in filtered_df.iterrows():
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
# Show Map
# -----------------------------
st_folium(m, width=1200, height=650)
