import streamlit as st
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

st.set_page_config(page_title="Multi-CSV Data Agent", layout="wide")
st.title("📊 Ask Questions Across Multiple CSVs")

# -----------------------------------
# Upload multiple CSVs
# -----------------------------------
uploaded_files = st.file_uploader(
    "Upload one or more CSV files",
    type=["csv"],
    accept_multiple_files=True
)

if uploaded_files:
    dataframes = {}
    
    st.subheader("Uploaded Data")
    for i, file in enumerate(uploaded_files):
        df = pd.read_csv(file)
        df_name = f"df_{i}"
        dataframes[df_name] = df

        st.markdown(f"**{df_name}**")
        st.dataframe(df)

    # -----------------------------------
    # Create LLM
    # -----------------------------------
    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    # -----------------------------------
    # Create Pandas Agent (multi-DF)
    # -----------------------------------
    agent = create_pandas_dataframe_agent(
        llm,
        list(dataframes.values()),
        verbose=False,
        allow_dangerous_code=True
    )

    # -----------------------------------
    # Strong system prompt
    # -----------------------------------
    SYSTEM_PROMPT = """
You are a data analysis assistant.

Rules:
- Use ONLY the provided pandas DataFrames.
- Do NOT use external knowledge.
- Do NOT make assumptions beyond the data.
- If the answer cannot be computed from the data, respond exactly with:
  "Not found in the uploaded CSVs."
- You may perform pandas operations only.
"""

    # -----------------------------------
    # User question
    # -----------------------------------
    question = st.text_input("Ask a question using the uploaded CSVs")

    if question:
        with st.spinner("Analyzing..."):
            try:
                response = agent.run(
                    f"""
{SYSTEM_PROMPT}

User Question:
{question}
"""
                )

                st.subheader("🤖 Answer")
                st.success(response)

            except Exception as e:
                st.error("Unable to answer the question using the uploaded CSVs.")
