📊 MultiCSVDataAssistant

MultiCSVDataAssistant is a Streamlit-based AI application that allows users to upload one or more small CSV files and ask natural-language questions about the data.
The app uses LangChain’s Pandas DataFrame Agent to ensure answers are computed strictly from the uploaded data, with no hallucinations or external knowledge.

✨ Features

📁 Upload multiple CSV files

🧮 Each CSV is converted into a Pandas DataFrame

🤖 A LangChain DataFrame Agent reasons over the data

🔒 Strong system prompt ensures the model uses only the uploaded CSVs

❌ If the answer is not present, the app responds honestly

⚡ Designed for small CSVs (< 20 rows) — fast and cost-efficient

🖥️ Simple, clean Streamlit UI

🧠 How It Works

User uploads one or more CSV files

Each CSV is loaded into a Pandas DataFrame

A LangChain Pandas DataFrame agent is created

A strict system prompt constrains the agent to:

Use only the DataFrames

Perform only pandas operations

Avoid assumptions or external knowledge

The user asks a question

The agent executes pandas logic and returns the answer

The answer is displayed in the Streamlit app

🛠️ Tech Stack

Python

Streamlit – UI

Pandas – Data processing

LangChain – Agent framework

OpenAI API – LLM reasoning

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/Kay3/multi-csv-data-assistant.git
cd MultiCSVDataAssistant

2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

🔑 OpenAI API Key Setup

Create an OpenAI API key and set it as an environment variable.

macOS / Linux
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"

Windows (PowerShell)
setx OPENAI_API_KEY "sk-xxxxxxxxxxxxxxxx"


Restart your terminal after setting the key.

▶️ Run the App
streamlit run app.py


The app will open in your browser at:

http://localhost:8501

💬 Example Questions

“What is the average value in the salary column?”

“Which product has the highest sales across all CSVs?”

“How many rows meet condition X?”

“Compare totals between the uploaded files”

“Is there any record with status = inactive?”

If the answer cannot be computed from the data:

Not found in the uploaded CSVs.

🔐 Security Notes

This app enables allow_dangerous_code=True for the Pandas DataFrame agent

This is safe for local or trusted environments

Do not expose publicly without additional sandboxing

Uploaded CSVs should be trusted

For large or public datasets, consider a retrieval-based approach instead of DataFrame agents.

🚧 Limitations

Designed for small CSVs (< 20 rows)

Not suitable for unstructured text-heavy columns

Not intended for public multi-user deployment without hardening

🚀 Future Improvements

💬 Chat-style conversation history

📊 Automatic chart generation

🧠 Display generated pandas code

🔐 Authentication & access control

☁️ Cloud deployment (Streamlit Cloud / AWS)

📄 License

MIT License

🙌 Acknowledgements

Streamlit

LangChain

OpenAI
