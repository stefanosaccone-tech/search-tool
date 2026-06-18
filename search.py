import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Our Team AI App", layout="wide")
st.title("🤖 Catalogue Search")

# Paste the exact HTML code snippet you copied from your GCP Widget tab below:
gcp_widget_code = """
<div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; background-color: #ffffff; box-shadow: 0 4px 6px rgba(0,0,0,0.05); min-height: 550px; font-family: sans-serif;">
    
    <h3 style="margin-top: 0; color: #333;">Catalogue Search</h3>
    <p style="color: #666; font-size: 14px;">Type your query below and press Enter or click search.</p>

    <!-- GOOGLE WIDGET CODE -->
    <script src="https://cloud.google.com/ai/proxies/chat-ui/index.js"></script>
    
    <!-- This tag embeds the actual search functionality -->
    <gen-search-widget
      configId="a1c8f735-5881-4d81-ac20-26fa64158c68"
      triggerId="searchWidgetTrigger">
    </gen-search-widget>

    <!-- Native Google Search Box that automatically triggers the widget -->
    <input type="text" id="searchWidgetTrigger" placeholder="Search the catalogue..." style="width: 100%; padding: 14px; font-size: 16px; border: 1px solid #0052cc; border-radius: 4px; box-sizing: border-box; outline: none; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">

</div>
"""

# This renders the Google widget inside the web page
components.html(gcp_widget_code, height=600, scrolling=True)
