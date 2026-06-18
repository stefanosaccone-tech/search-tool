import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Our Team AI App", layout="wide")
st.title("🤖 Catalogue Search")

# Paste the exact HTML code snippet you copied from your GCP Widget tab below:
gcp_widget_code = """
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Catalogue Search", layout="wide")

# We increase the height to 800px so there is plenty of room for search results to display inline
st.title("📖 Catalogue Search")

gcp_widget_code = """
<div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; background-color: #ffffff; box-shadow: 0 4px 6px rgba(0,0,0,0.05); min-height: 700px; font-family: sans-serif;">

    <script src="https://cloud.google.com/ai/gen-app-builder/client?hl=en_US"></script>

    <input placeholder="Type your search here and press Enter..." id="searchWidgetTrigger" 
           style="width: 100%; padding: 14px; font-size: 16px; border: 2px solid #1a73e8; border-radius: 4px; box-sizing: border-box; outline: none; margin-bottom: 20px;" />

    <gen-search-widget
      configId="a1c8f735-5881-4d81-ac20-26fa64158c68"
      triggerId="searchWidgetTrigger"
      displayMode="INLINE">
    </gen-search-widget>

</div>
"""

# This renders the Google widget inside the web page
components.html(gcp_widget_code, height=600, scrolling=True)
