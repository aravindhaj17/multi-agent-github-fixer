import streamlit as st
from orchestrator.graph import create_graph

# Page configuration
st.set_page_config(
    page_title="AI Multi-Agent Code Debugger",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Multi-Agent Code Debugger")

st.markdown(
"""
Analyze GitHub issues with AI agents that **explain the bug, generate a fix, and create tests automatically**.
"""
)

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    issue = st.text_area(
        "GitHub Issue",
        placeholder="Example: Application crashes when user id does not exist",
        height=120
    )

with col2:
    repo_code = st.text_area(
        "Code Snippet",
        placeholder="Paste the code you want the AI agents to analyze...",
        height=120
    )

run_button = st.button("🚀 Run AI Agents")

if run_button:

    if not issue.strip() or not repo_code.strip():
        st.warning("⚠️ Please enter both a GitHub issue and code snippet.")
    else:

        with st.spinner("AI agents are analyzing the issue..."):

            app = create_graph()

            result = app.invoke({
                "issue": issue,
                "repo_code": repo_code
            })

        st.success("Analysis complete!")

        # Tabs for results
        tab1, tab2, tab3 = st.tabs(["🔍 Research", "🛠 Fix", "🧪 Tests"])

        with tab1:
            st.subheader("Research Analysis")
            st.write(result["research_result"])

        with tab2:
            st.subheader("Generated Fix")
            st.code(result["fix"], language="python")

        with tab3:
            st.subheader("Generated Tests")
            st.code(result["tests"], language="python")