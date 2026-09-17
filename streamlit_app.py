import os
import streamlit as st
import streamlit.components.v1 as components

# Configure page to wide mode with collapsed sidebar
st.set_page_config(
    page_title="HackBridge — Multi-Tenant Hackathon Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Completely eliminate all Streamlit chrome: sidebar, headers, footers, margins
st.markdown("""
<style>
    /* Hide all default Streamlit interface elements */
    #MainMenu { display: none !important; }
    header { display: none !important; }
    footer { display: none !important; }
    div[data-testid="stHeader"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }
    div[data-testid="collapsedControl"] { display: none !important; }
    div[data-testid="stToolbar"] { display: none !important; }
    div[data-testid="stDecoration"] { display: none !important; }
    div[data-testid="stStatusWidget"] { display: none !important; }

    /* Remove any margins/padding from the main app body */
    html, body, .main, [data-testid="stAppViewContainer"], .block-container, [data-testid="stVerticalBlock"] {
        padding: 0 !important;
        margin: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        max-width: 100vw !important;
        overflow: hidden !important;
    }

    /* Fixed full-screen iframe covering 100% viewport */
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
        z-index: 999999 !important;
    }
</style>
""", unsafe_allow_html=True)

base_dir = os.path.dirname(os.path.abspath(__file__))
static_index = os.path.join(base_dir, "static", "index.html")

if os.path.exists(static_index):
    # Embed the React SPA across 100% of the screen with zero outer Streamlit text
    if hasattr(st, "iframe"):
        st.iframe(src="/app/static/index.html", height=1200)
    else:
        components.iframe(src="/app/static/index.html", height=1200)
else:
    st.error("Build assets not found in static/. Please build and sync assets.")
