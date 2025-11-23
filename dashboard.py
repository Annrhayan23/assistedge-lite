
import streamlit as st, os, json
st.title("AssistEdge Lite – RPA Bot")

if os.path.exists("workflow.json"):
    wf = json.load(open("workflow.json"))
    st.json(wf)

if st.button("Run Workflow"):
    import player
    st.success("Workflow executed!")
