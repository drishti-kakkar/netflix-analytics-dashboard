import streamlit as st
import pandas as pd
import plotly.express as px

from time import sleep
# ----------------------------
# CUSTOM NETFLIX STYLE
# ----------------------------

st.markdown("""
    <style>

    .main {
        background-color: #141414;
        color: white;
    }

    h1, h2, h3 {
        color: #E50914;
    }

    .stMetric {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    padding: 20px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

    section[data-testid="stSidebar"] {
        background-color: #111111;
    }
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #111111,
        #1a1a1a
    );
    border-right: 1px solid #E50914;
}
    .stDownloadButton button {
        background-color: #E50914;
        color: white;
        border-radius: 8px;
        border: none;
    }

    .stButton button {
    .stDownloadButton button:hover {
    background-color: white;
    color: #E50914;
}

.stButton button:hover {
    background-color: white;
    color: #E50914;
}
.stMetric:hover {
    transform: scale(1.03);
    transition: 0.3s;
}

.stPlotlyChart:hover {
    transform: scale(1.01);
    transition: 0.3s;
}
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(229,9,20,0.3);
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}
iframe {
    border-radius: 20px;
    box-shadow: 0px 6px 30px rgba(0,0,0,0.4);
}
        background-color: #E50914;
        color: white;
        border-radius: 8px;
        border: none;
    }

    </style>
""", unsafe_allow_html=True)
# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# TITLE
# ----------------------------

st.markdown("""
<div style='text-align: center;'>

<img src='https://upload.wikimedia.org/wikipedia/commons/7/7a/Logonetflix.png'
width='320'>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="
position: relative;
width: 100%;
height: 500px;
overflow: hidden;
border-radius: 25px;
">

<img src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba"
style="
width: 100%;
height: 120%;
object-fit: cover;
filter: brightness(55%);
">

<div style="
position: absolute;
top: 50%;
left: 50%;
transform: translate(-50%, -50%);
text-align: center;
width: 100%;
">

<h1 style="
color:  white;
font-size: 70px;
font-weight: bold;
margin-bottom: 10px;
">
Streaming Intelligence System
</h1>

<p style="
color: white;
font-size: 24px;
">
Real-Time Content Analytics • Viewer Trends • Global Insights
</p>

</div>

</div>
""", unsafe_allow_html=True)



st.markdown("""
<center>

<h2 style='color:white;'>
"See What the World is Watching."
</h2>

</center>
""", unsafe_allow_html=True)

# FEATURED MOVIES SECTION
st.subheader("Trending Netflix Content")

poster1, poster2, poster3 = st.columns(3)

with poster1:
    st.image(
        "https://image.tmdb.org/t/p/w500/x2LSRK2Cm7MZhjluni1msVJ3wDF.jpg",
        use_container_width=True
    )

with poster2:
    st.image(
        "https://image.tmdb.org/t/p/w500/9PFonBhy4cQy7Jz20NpMygczOkv.jpg",
        use_container_width=True
    )

with poster3:
    st.image(
        "https://image.tmdb.org/t/p/w500/reEMJA1uzscCbkpeRJeTT2bjqUp.jpg",
        use_container_width=True
    )
st.markdown("""
<h1 style="
text-align:center;
color:white;
font-size:55px;
margin-top:20px;
">
Netflix Insights Hub
</h1>
""", unsafe_allow_html=True)
st.markdown("""
<div style="
    background-color:#E50914;
    padding:15px;
    border-radius:10px;
    text-align:center;
    color:white;
    font-size:22px;
    font-weight:bold;
">
    Real-Time Netflix Analytics Dashboard
</div>
""", unsafe_allow_html=True)

st.markdown("""
## Discover trends, genres, countries, and streaming insights from Netflix data.

Analyze content interactively with advanced filters and business intelligence dashboards.
""")
st.toast("Netflix Dashboard Loaded Successfully 🚀")
search_title = st.text_input(
    "Search Netflix Title"
)
st.markdown("Analyze Netflix movies and TV shows interactively.")

# ----------------------------
# LOAD DATA
# ----------------------------

with st.spinner("Loading Netflix Analytics Dashboard..."):
    sleep(2)
    netflix = pd.read_csv("dataset/netflix_titles.csv")

# ----------------------------
# SIDEBAR FILTER
# ----------------------------
st.divider()
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg",
    width=80
)

st.sidebar.markdown("""
## Netflix Filters
Choose dashboard filters below.
""")
selected_country = st.sidebar.selectbox(
    "Choose Country",
    ["All"] + list(netflix["country"].dropna().unique())
)

selected_type = st.sidebar.selectbox(
    "Choose Content Type",
    netflix["type"].unique()
)

filtered_data = netflix[
    netflix["type"] == selected_type
]

if selected_country != "All":
    filtered_data = filtered_data[
        filtered_data["country"] == selected_country
    ]
if search_title:
    filtered_data = filtered_data[
        filtered_data["title"].str.contains(
            search_title,
            case=False,
            na=False
        )
    ]
# ----------------------------
# KPI CARDS
# ----------------------------
insight1, insight2 = st.columns(2)

with insight1:
    st.warning("""
    Content production increased sharply after 2016.
    """)

with insight2:
    st.info("""
    United States dominates Netflix content distribution.
    """)
total_titles = filtered_data.shape[0]

total_countries = filtered_data["country"].nunique()

latest_year = filtered_data["release_year"].max()
st.divider()

st.subheader("Dashboard KPIs")
col1, col2, col3 = st.columns(3)

col1.metric("Total Titles", total_titles)

col2.metric("Countries", total_countries)

col3.metric("Latest Release Year", latest_year)

# ----------------------------
# DATAFRAME
# ----------------------------
st.divider()
st.markdown("""
<h2 style='color:#E50914;'>
Live Netflix Dataset
</h2>
""", unsafe_allow_html=True)

st.dataframe(
    filtered_data.head(20),
    use_container_width=True
)
csv = filtered_data.to_csv(index=False)

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_netflix_data.csv",
    mime="text/csv"
)

tab1, tab2 = st.tabs([
    "Ratings Analysis",
    "Release Trend"
])
# ----------------------------
# PIE CHART
# ----------------------------

fig1 = px.pie(
    filtered_data,
    names="rating",
    title="Content Ratings Distribution"
)
st.divider()

chart1, chart2 = st.columns(2)

with chart1:
    with tab1:
        st.plotly_chart(
            fig1,
            use_container_width=True
        )

# ----------------------------
# RELEASE YEAR TREND
# ----------------------------

year_data = filtered_data["release_year"].value_counts().sort_index()

fig2 = px.line(
    x=year_data.index,
    y=year_data.values,
    title="Content Release Trend",
    markers=True
)

fig2.update_layout(
    paper_bgcolor="#141414",
    plot_bgcolor="#141414",
    font_color="white"
)

st.divider()

with chart2:
    with tab2:
        st.plotly_chart(
            fig2,
            use_container_width=True
        )
# ----------------------------
# TOP GENRES
# ----------------------------

genre_data = filtered_data["listed_in"].value_counts().head(10)

fig3 = px.bar(
    x=genre_data.index,
    y=genre_data.values,
    title="Top Genres"
)
st.divider()
st.plotly_chart(fig3, use_container_width=True)

st.divider()

st.subheader("Top 10 Netflix Titles")

st.table(
    filtered_data[
        ["title", "country", "release_year"]
    ].head(10)
)

st.sidebar.info(
    "This dashboard analyzes Netflix content using Python and Streamlit."
)



st.markdown("""
<hr>

<center>

<h3 style='color:#E50914;'>
Built with ❤️ using Python, Plotly & Streamlit
</h3>

<p>
Netflix Analytics Dashboard © 2026
</p>

</center>
""", unsafe_allow_html=True)
st.divider()

st.subheader("Top Netflix Countries")

country_data = filtered_data["country"].value_counts().head(10)

fig4 = px.bar(
    x=country_data.index,
    y=country_data.values,
    title="Top Countries"
)

st.plotly_chart(fig4, use_container_width=True)

st.divider()

st.info("""
This dashboard provides insights into Netflix content trends,
genres, countries, ratings, and release patterns using
interactive analytics visualizations.
""")

with st.expander("About This Dashboard"):

    st.write("""

    This dashboard was built using:

    - Python
    - Pandas
    - Plotly
    - Streamlit

    Features include:
    - Interactive filtering
    - KPI analytics
    - Time-series analysis
    - Genre analysis
    - Country insights
    - Downloadable datasets

    """)

    st.markdown("""
<h2 style='color:#E50914;'>
Live Content Intelligence Feed
</h2>
""", unsafe_allow_html=True)

latest_titles = filtered_data[
    ["title", "release_year"]
].head(5)

for index, row in latest_titles.iterrows():

    st.markdown(f"""
    {row['title']} 
    • Released: {row['release_year']}
    """)