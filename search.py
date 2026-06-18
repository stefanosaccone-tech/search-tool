import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Our Team AI App", layout="wide")
st.title("🤖 Catalogue Search")

# Paste the exact HTML code snippet you copied from your GCP Widget tab below:
gcp_widget_code = """
<!-- Widget JavaScript bundle -->
<script src="https://cloud.google.com/ai/gen-app-builder/client?hl=en_US"></script>

<!-- Search widget element is not visible by default -->
<gen-search-widget
  configId="a1c8f735-5881-4d81-ac20-26fa64158c68"
  triggerId="searchWidgetTrigger">
</gen-search-widget>

<!-- Element that opens the widget on click. It does not have to be an input -->
<input placeholder="Search here" id="searchWidgetTrigger" />
"""

# This renders the Google widget inside the web page
components.html(gcp_widget_code, height=600, scrolling=True)
