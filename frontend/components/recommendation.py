"""
Component for displaying recommendations based on the analysis results
"""
from typing import Any, Dict

import streamlit as st


def display_recommendations(analysis: Dict[str, Any]) -> None:
    suggestions = analysis.get("suggestions") or []
    if not suggestions:
        return

    #Displays suggestion as a bulleted list under 'Recommendations'
    st.markdown("### 💡 Recommendations")
    for suggestion in suggestions:
        st.markdown(f"- {suggestion}")