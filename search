import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Our Team AI App", layout="wide")
st.title("🤖 Catalogue Search")

# Paste the exact HTML code snippet you copied from your GCP Widget tab below:
gcp_widget_code = """
<script src="https://cloud.google.com/ai/proxies/..."></script>
<gen-search-widget
  configId="xxxxxx-xxxx-xxxx-xxxx-xxxxxxxx"
  triggerId="searchWidgetTrigger">
</gen-search-widget>
<input type="text" id="searchWidgetTrigger" placeholder="Ask our AI anything..." style="width:100%; padding:10px; font-size:16px;">
"""

# This renders the Google widget inside the web page
components.html(gcp_widget_code, height=600, scrolling=True)
