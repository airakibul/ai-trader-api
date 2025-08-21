import streamlit as st
import requests
import base64
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------
API_URL = "http://127.0.0.1:8000"
st.set_page_config(page_title="AI Trader Frontend", layout="wide")

# -----------------------------
# Session State
# -----------------------------
if "token" not in st.session_state:
    st.session_state.token = None
if "username" not in st.session_state:
    st.session_state.username = None

# -----------------------------
# Helper Functions
# -----------------------------
def api_post(endpoint, payload, auth=True):
    headers = {}
    if auth and st.session_state.token:
        headers["Authorization"] = f"Bearer {st.session_state.token}"
    response = requests.post(f"{API_URL}{endpoint}", json=payload, headers=headers)
    return response.json()

# -----------------------------
# Authentication
# -----------------------------
st.sidebar.title("Login / Logout")

if st.session_state.token:
    st.sidebar.success(f"Logged in as {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.token = None
        st.session_state.username = None
else:
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        res = api_post("/auth/token", {"username": username, "password": password}, auth=False)
        if "access_token" in res:
            st.session_state.token = res["access_token"]
            st.session_state.username = username
            st.sidebar.success("Login successful")
        else:
            st.sidebar.error(res.get("detail", "Login failed"))

# -----------------------------
# Main Interface
# -----------------------------
st.title("AI Trader API Frontend")

task = st.selectbox("Select Task", ["Q&A", "Content Generation", "Image Generation", "Latest Answer"])

if task == "Q&A":
    query = st.text_area("Enter your question")
    provider = st.selectbox("Provider", ["auto", "openrouter", "groq", "huggingface", "stability"])
    if st.button("Get Answer"):
        payload = {"task": "qa", "query": query, "provider": provider}
        res = api_post("/ai-task" if st.session_state.token else "/ai-task-no-auth", payload)
        st.markdown(f"**Answer:** {res.get('answer','No response')}")
        st.markdown(f"*Provider used:* {res.get('provider_used','N/A')}")

elif task == "Content Generation":
    topic = st.text_input("Topic")
    platform = st.selectbox("Platform", ["facebook", "linkedin", "twitter", "instagram"])
    provider = st.selectbox("Provider", ["auto", "openrouter", "groq", "huggingface", "stability"])
    if st.button("Generate Content"):
        payload = {"task": "content_generation", "topic": topic, "platform": platform, "provider": provider}
        res = api_post("/ai-task" if st.session_state.token else "/ai-task-no-auth", payload)
        st.markdown(f"**Generated Content:** {res.get('content','No response')}")
        st.markdown(f"*Provider used:* {res.get('provider_used','N/A')}")
        st.markdown(f"*Character count:* {res.get('character_count','N/A')}")

elif task == "Image Generation":
    prompt = st.text_area("Enter prompt for image generation")
    provider = st.selectbox("Provider", ["auto", "stability", "huggingface"])
    if st.button("Generate Image"):
        payload = {"task": "image_generation", "prompt": prompt, "provider": provider}
        res = api_post("/ai-task" if st.session_state.token else "/ai-task-no-auth", payload)
        img_data = res.get("image_url")
        if img_data:
            st.image(img_data)
        st.markdown(f"*Provider used:* {res.get('provider_used','N/A')}")

elif task == "Latest Answer":
    res = api_post("/ai-task" if st.session_state.token else "/ai-task-no-auth", {"task": "latest_answer"})
    latest = res.get("data")
    if latest:
        st.markdown(f"**Query:** {latest.get('query')}")
        st.markdown(f"**Answer:** {latest.get('answer')}")
        st.markdown(f"*Provider used:* {latest.get('provider')}")
        st.markdown(f"*Timestamp:* {latest.get('timestamp')}")
    else:
        st.markdown("No latest answers available.")
