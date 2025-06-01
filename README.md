# 💡 Flowbit

Flowbit is a modular multi-agent AI system that classifies input (e.g. JSON, Email), routes it to the appropriate agent, and stores extracted data in a shared memory module using SQLite.

---

## 🚀 Features

- 🧠 Input classification via LLM
- 🔁 Intelligent routing to JSON or Email processing agents
- 📦 Shared memory with logging using SQLite
- 📄 Works with text, JSON, and email formats
- ⚙️ Easy to expand with additional agents

---

## 🗂️ Project Structure

flowbit/
├── agents/ # All agent logic
│ ├── classifier_agent.py # Uses LLM to classify input
│ ├── json_agent.py # Handles JSON input
│ └── email_agent.py # Handles email input
│
├── memory/ # Memory logging and retrieval
│ └── memory_store.py
| |___ targeted schema
│
├── sample_inputs/ # Sample input files
│ ├── sample_email.txt
│ └── sample_json.json
│
├── main.py # Entry point and flow controller
├── requirements.txt # Python dependencies
└── README.md


---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/flowbit.git
cd flowbit
**### 2. Create a virtual environment**
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
**###3. Install dependencies**
bash
Copy
Edit
pip install -r requirements.txt
Ensure you have access to OpenAI or a compatible LLM if you're using GPT-based classification.

**⚙️ How to Run**

python main.py
You can simulate different types of inputs inside main.py by switching between:
run_flow(email_data)
run_flow(json_data)
You can also see the memory logs

🧠 Memory Logs
All processed inputs are logged into memory.db. You can view memory logs printed at the end of each run.

🧪 Sample Inputs
Add your test inputs under sample_inputs/. You can add:

sample_email.txt — for raw email-style input

sample_json.json — for structured JSON
