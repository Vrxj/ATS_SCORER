"""
component for displaying strengths and critical issues in the resume analysis
"""
from typing import Any, Dict, List
import streamlit as st

#Display a bulleted list of strengths, or a message if the list is empty.
def display_strengths(strengths: List[str]) -> None:
    st.markdown("### 💪 Strengths")
    if not strengths:
        st.info("Keep improving your resume to unlock strengths!")
        return
    for item in strengths:
        st.markdown(f"- {item}")

#Display a bulleted list of critical issues, or a message if the list is empty.
def display_critical_issues(analysis: Dict[str, Any]) -> None:
    #get fields
    critical = analysis.get("critical_issues") or []
    summary = analysis.get("issues_summary") or []

    if not critical and not summary:
        st.success("### ✅ No Critical Issues Found!")
        st.markdown("Your resume doesn't have any urgent issues. Nice work.")
        return

    #if critical issues, show
    st.markdown("### 🚨 Critical Issues")
    st.error("These issues should be addressed first for better ATS performance.")

    for item in critical:
        st.markdown(f"- {item}")
        
    #if there are additional issues in the summary that are not critical, 
    #show them in an expandable section
    extra = [s for s in summary if s not in critical]
    if extra:
        with st.expander("📋 Additional flagged items", expanded=False):
            for item in extra:
                st.markdown(f"- {item}")