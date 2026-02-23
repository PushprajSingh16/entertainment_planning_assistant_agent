import streamlit as st
import requests

# Custom CSS for purple theme
st.markdown("""
<style>
    .stApp {
        background-color: #4a148c;
        color: white;
    }
    .css-1d391kg {
        background-color: #4a148c;
        color: white;
    }
    .css-12ttj6m {
        background-color: #6a1b9a;
        color: white;
    }
    /* Input fields */
    .stTextInput > div > div > input {
        background-color: #7b1fa2 !important;
        color: white !important;
        border: 1px solid #9c27b0 !important;
    }
    .stTextInput label {
        color: white !important;
    }
    /* Selectbox */
    .stSelectbox > div > div > select {
        background-color: #7b1fa2 !important;
        color: white !important;
        border: 1px solid #9c27b0 !important;
    }
    .stSelectbox label {
        color: white !important;
    }
    /* Buttons */
    .stButton > button {
        background-color: #ff5722 !important;
        color: white !important;
        border: none !important;
    }
    .stButton > button:hover {
        background-color: #ff7043 !important;
    }
    /* Alerts */
    .stSuccess {
        background-color: #4caf50 !important;
        color: white !important;
        border: 1px solid #66bb6a !important;
    }
    .stWarning {
        background-color: #ff9800 !important;
        color: white !important;
        border: 1px solid #ffb74d !important;
    }
    .stError {
        background-color: #f44336 !important;
        color: white !important;
        border: 1px solid #ef5350 !important;
    }
    /* Headers and text */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }
    .stCaption {
        color: #e1bee7 !important;
    }
    /* Metrics */
    .css-1xarl3l {
        background-color: #6a1b9a !important;
        border: 1px solid #7b1fa2 !important;
        color: white !important;
    }
    /* Spinner */
    .stSpinner {
        color: white !important;
    }
    /* Sidebar headers */
    .sidebar .sidebar-content h1, .sidebar .sidebar-content h2, .sidebar .sidebar-content h3 {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Entertainment Planning Assistant",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.header("🎭 About")
    st.write("AI-powered entertainment planning using Groq LLM.")
    st.write("Get detailed plans for movies and events in your city.")
    
    st.header("⚙️ Settings")
    api_url = st.text_input("API URL", "http://127.0.0.1:8000", help="Backend API endpoint")
    
    st.header("📊 Stats")
    if st.button("Check Backend Health"):
        try:
            res = requests.get(f"{api_url}/health", timeout=5)
            if res.status_code == 200:
                data = res.json()
                st.success(f"✅ Backend healthy (v{data.get('version', 'unknown')})")
            else:
                st.error("❌ Backend not responding")
        except:
            st.error("❌ Cannot connect to backend")

# Main content
st.title("🎬 Entertainment Planning Assistant")
st.caption("Plan your perfect movie night or event outing!")

col1, col2 = st.columns(2)

with col1:
    movie = st.text_input("🎥 Movie / Event", placeholder="Border 2", help="Enter the movie or event name")

with col2:
    city_options = ["Indore", "Mumbai", "Delhi", "Bangalore", "Chennai", "Pune", "Jaipur", "Ahmedabad", 
                   "Kolkata", "Hyderabad", "Chandigarh", "Goa", "Udaipur", "Agra", "Varanasi", 
                   "Lucknow", "Kanpur", "Nagpur", "Bhopal", "Patna", "Ranchi", "Guwahati", "Other"]
    city = st.selectbox("📍 City", city_options, help="Select your city")
    
    if city == "Other":
        custom_city = st.text_input("Enter Custom City", placeholder="Your city name")
        if custom_city:
            city = custom_city

if st.button("🎯 Generate Plan", type="primary", use_container_width=True):
    if not movie or not city:
        st.warning("Please enter both movie/event and city.")
        st.stop()

    with st.spinner("Planning your entertainment..."):
        try:
            res = requests.get(
                f"{api_url}/plan",
                params={"movie": movie, "city": city},
                timeout=60
            )
            data = res.json()
            
            st.success(f"Plan generated for **{data['movie']}** in **{data['city']}**!")
            
            # Display plan with better formatting
            st.markdown("---")
            st.subheader("📋 Your Entertainment Plan")
            
            # Split plan into sections
            plan_text = data["plan"]
            sections = plan_text.split("•")
            
            for section in sections:
                if section.strip():
                    st.markdown(f"• {section.strip()}")
            
            # Add some visual elements
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Estimated Cost", "₹200-500")
            with col2:
                st.metric("Duration", "2-3 hours")
            with col3:
                st.metric("Rating", "⭐ 4.2/5")
                
        except requests.exceptions.JSONDecodeError:
            st.error("Failed to parse response. Please check backend.")
        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using FastAPI, Streamlit & Groq")