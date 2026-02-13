# 🌍 India Dynamic Area Mapping Dashboard (Cloud Version)

This project is a fully deployable Streamlit web application that
displays an interactive India map with dynamic area markers.

Users can: - View full India map with all spots - Filter by district -
Auto zoom into selected district - Highlight district boundary - Deploy
publicly using Streamlit Community Cloud

------------------------------------------------------------------------

# 🏗 Project Structure

    india-area-map/
    │
    ├── app.py
    ├── data.xlsx
    ├── india_states.geojson
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# 📊 Excel File Format (data.xlsx)

  State   District   Area   Latitude   Longitude
  ------- ---------- ------ ---------- -----------

### Rules:

-   Column names must be EXACT:
    -   State
    -   District
    -   Area
    -   Latitude
    -   Longitude
-   Latitude & Longitude must be numeric
-   No empty values in Latitude or Longitude
-   District spelling must match GeoJSON

------------------------------------------------------------------------

# 🗺 GeoJSON Requirement

Use India District Boundary GeoJSON file.

It must contain a property like:

    dtname

The app filters using this property to highlight boundaries.

------------------------------------------------------------------------

# ⚙ Local Development Setup

## 1️⃣ Create Virtual Environment

``` bash
python -m venv venv
venv\Scripts\activate
```

## 2️⃣ Install Dependencies

``` bash
pip install streamlit pandas folium streamlit-folium openpyxl
```

## 3️⃣ Run Locally

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

# ☁ Deploy to Streamlit Community Cloud

## Step 1: Create GitHub Repository

1.  Go to GitHub
2.  Create new public repository
3.  Upload:
    -   app.py
    -   data.xlsx
    -   india_states.geojson
    -   requirements.txt

------------------------------------------------------------------------

## Step 2: Create requirements.txt

    streamlit
    pandas
    folium
    streamlit-folium
    openpyxl

⚠ Do NOT include geopandas in cloud version.

------------------------------------------------------------------------

## Step 3: Deploy

1.  Visit https://share.streamlit.io
2.  Login with GitHub
3.  Click "New App"
4.  Select repository
5.  Select main file: app.py
6.  Deploy

After deployment, you will receive a public link:

    https://your-app-name.streamlit.app

Anyone can open this link without knowing the code.

------------------------------------------------------------------------

# 🧠 How the App Works

1.  Reads Excel data
2.  Cleans Latitude & Longitude
3.  Loads GeoJSON using JSON (no geopandas for cloud stability)
4.  Displays all markers by default
5.  Auto fits map using fit_bounds()
6.  Filters and highlights boundary when district selected

------------------------------------------------------------------------

# 🛠 Common Cloud Errors & Fixes

------------------------------------------------------------------------

## ❌ ModuleNotFoundError: folium

Cause: Missing dependency in requirements.txt

Fix: Ensure folium is listed in requirements.txt

------------------------------------------------------------------------

## ❌ Location values cannot contain NaNs

Cause: Empty Latitude or Longitude in Excel

Fix added in app:

``` python
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df = df.dropna(subset=["Latitude", "Longitude"])
```

------------------------------------------------------------------------

## ❌ Boundary Not Showing

Cause: - District name mismatch - Incorrect dtname property

Fix: Check property name inside geojson file.

------------------------------------------------------------------------

## ❌ Map Not Fully Visible

Fix: Use:

``` python
m.fit_bounds(bounds)
```

------------------------------------------------------------------------

# 🚀 Production Tips

-   Keep GeoJSON file small
-   Avoid geopandas in cloud
-   Validate Excel before upload
-   Use consistent naming

------------------------------------------------------------------------

# 🔮 Future Upgrade Ideas

-   State → District → Area 3-level drilldown
-   Login system
-   Google Sheets live integration
-   Database backend
-   Custom domain
-   Admin panel

------------------------------------------------------------------------

# 🎓 What This Project Demonstrates

-   Excel-driven GIS mapping
-   Cloud deployment with Streamlit
-   JSON-based boundary filtering
-   Production-safe dependency handling
-   Error-proof geospatial validation

------------------------------------------------------------------------

# 👨‍💻 Author Note

This dashboard can be extended for:

-   E-waste collection mapping
-   Audit visit tracking
-   Sustainability reporting
-   Carbon footprint visualization
-   Revenue heatmap analysis

------------------------------------------------------------------------

✅ Cloud Version Stable\
✅ Public Shareable Link\
✅ No Heavy GIS Dependencies

Happy Deploying 🚀
