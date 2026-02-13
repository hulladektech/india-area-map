# 📍 India Dynamic Area Mapping Dashboard

An interactive India map dashboard built using **Streamlit + Folium +
GeoPandas**.

------------------------------------------------------------------------

## 🚀 Features

-   Full India map with all area spots
-   District-based filtering
-   Auto zoom into selected district
-   District boundary highlight
-   Multiple areas inside same district supported
-   Excel-driven dynamic update

------------------------------------------------------------------------

## 🏗 Project Structure

    india_dynamic_map/
    │
    ├── app.py
    ├── data.xlsx
    ├── india_states.geojson
    └── README.md

------------------------------------------------------------------------

## 📊 Excel File Format (`data.xlsx`)

  State   District   Area   Latitude   Longitude
  ------- ---------- ------ ---------- -----------

### Important Rules:

-   Column names must be EXACT:
    -   State
    -   District
    -   Area
    -   Latitude
    -   Longitude
-   Latitude & Longitude must be numeric
-   Spelling must match GeoJSON district names

------------------------------------------------------------------------

## 🗺 GeoJSON File

Download India District Boundary GeoJSON.

Ensure it contains a column like:

    dtname

In the code we rename it to:

``` python
districts = districts.rename(columns={"dtname": "District"})
```

If your file has different column name, check using:

``` python
st.write(districts.columns)
```

------------------------------------------------------------------------

## ⚙ Installation Steps

### 1️⃣ Create Virtual Environment

``` bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Required Packages

``` bash
pip install streamlit pandas folium geopandas openpyxl streamlit-folium
```

------------------------------------------------------------------------

## ▶ Run the Application

``` bash
streamlit run app.py
```

Browser will open automatically.

------------------------------------------------------------------------

## 🎯 Application Behavior

### Default View:

-   Full India map
-   All area spots visible

### When District Selected:

-   Map zooms into district
-   District boundary highlighted
-   Only selected district areas visible

------------------------------------------------------------------------

## 🛠 Common Errors & Fixes

### ❌ KeyError: 'Value'

Cause: Excel does not contain Value column. Fix: Remove Value logic or
correct column name.

------------------------------------------------------------------------

### ❌ KeyError: 'st_nm'

Cause: GeoJSON file does not contain that column. Fix: Run:

``` python
st.write(states.columns)
```

Then update column reference accordingly.

------------------------------------------------------------------------

### ❌ Map Blank

Check: - District spelling match - No empty Latitude/Longitude - Case
sensitivity (Mumbai ≠ mumbai)

------------------------------------------------------------------------

## 🔮 Future Upgrade Ideas

-   State → District → Area 3-level drill-down
-   State button panel instead of dropdown
-   Marker color by status
-   Marker size by score
-   Google Sheets integration
-   Public deployment on Streamlit Cloud

------------------------------------------------------------------------

## 🎓 What This Project Teaches

-   Reading Excel dynamically
-   Using GeoJSON boundary files
-   Filtering geospatial data
-   Building interactive dashboards
-   Handling common pandas errors
-   GIS-style zoom & boundary highlighting

------------------------------------------------------------------------

## 👨‍💻 Author Notes

This project can be extended for:

-   E-waste collection mapping
-   Audit visit tracking
-   Revenue hotspot visualization
-   Sustainability reporting
-   Carbon impact dashboards

------------------------------------------------------------------------

Happy Building 🚀
