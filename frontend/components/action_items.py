"""
Compontents for displaying action items in the ATS Scorer frontend.
"""
from typing import Any, Dict, List, Tuple

import streamlit as st

#Defines display order
SEVERITY_RANK = {"critical": 0, "high": 1, "medium": 2, "low": 3}

#Reads actions item from detailed_feedback
def _collect_action_items(analysis: Dict[str, Any]) -> List[Tuple[str, str, str]]:
    """Return list of (severity, source_title, action_text)."""
    items: List[Tuple[str, str, str]] = []

    #If we have detailed feedback, read the action items from there.
    #  Otherwise, fall back to suggestions.
    for issue in analysis.get("detailed_feedback") or []:
        level = (issue.get("severity_level") or "low").lower()
        title = issue.get("issue_title", "")
        for action in issue.get("action_items") or []:
            items.append((level, title, action))

    if not items:
        for suggestion in analysis.get("suggestions") or []:
            items.append(("medium", "General", suggestion))
    
    #Sort using SEVERITY_RANK
    items.sort(key=lambda row: SEVERITY_RANK.get(row[0], 99))
    return items

#Displays them as a list with icons and severity levels
def display_action_items(analysis: Dict[str, Any]) -> None:
    #Sorts and collects action items from the analysis result
    items = _collect_action_items(analysis)
    if not items:
        return

    st.markdown("### ⚡ Action Items")
    st.caption("Concrete steps to improve your score, sorted by urgency.")

    for level, source, action in items:
        icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}.get(level, "🟢")
        st.markdown(f"- {icon} **[{source}]** {action}")