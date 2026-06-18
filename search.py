import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Our Team AI App", layout="wide")
st.title("🤖 Catalogue Search")

# Paste the exact HTML code snippet you copied from your GCP Widget tab below:
gcp_widget_code = """
<div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; background-color: #ffffff; box-shadow: 0 4px 6px rgba(0,0,0,0.05); min-height: 500px;">
    
    <script src="https://cloud.google.com/ai/proxies/chat-ui/index.js"></script>
    <gen-search-widget
      configId="a1c8f735-5881-4d81-ac20-26fa64158c68"
      triggerId="searchWidgetTrigger">
    </gen-search-widget>
    <label style="font-family: sans-serif; font-weight: bold; color: #333; display: block; margin-bottom: 8px;">Search the Catalogue:</label>
    <input type="text" id="searchWidgetTrigger" placeholder="Type your search query here..." style="width:100%; padding: 12px; font-size: 16px; border: 1px solid #cccccc; border-radius: 4px; box-sizing: border-box;">
</div>
"""

# This renders the Google widget inside the web page
components.html(gcp_widget_code, height=600, scrolling=True)
