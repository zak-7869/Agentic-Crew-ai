# Agentic Crew AI Search System

This repository contains an implementation of a multi-agent system built using the **CrewAI** framework. It orchestrates role-based autonomous agents assigned with specific tasks and tools to perform deep, collaborative **internet searches** and web research.

## 🚀 Overview

The project showcases how to break down complex research workflows into specialized roles. By assigning distinct goals, backstories, and search tools to multiple agents, the system collaborates sequentially or hierarchically to gather real-time data from the web and compile comprehensive reports. The core application logic is housed within `app.py`.

[ User Prompt / Topic ]│▼┌────────────────────────────────────────────────────────┐│                      Crew Container                    ││                                                        ││   ┌──────────────────┐          ┌──────────────────┐   ││   │   Agent 1:       │          │   Agent 2:       │   ││   │   Researcher     │          │   Writer / Editor│   ││   └────────┬─────────┘          └────────▲─────────┘   ││            │                             │             ││     (Executes Task 1)             (Executes Task 2)    ││            │                             │             ││            ▼                             │             ││   ┌──────────────────┐                   │             ││   │  Internet Tools  │                   │             ││   │  (Search/Scrape) ├───────────────────┘             ││   └──────────────────┘                                 │└────────────────────────────────────────────────────────┘│▼[ Final Markdown Report / Output ]


## 🏗️ CrewAI Core Concepts

The application structures agent execution using CrewAI's primary building blocks:

* **Agents:** Individual AI personas designed with specific roles (e.g., Researcher, Writer), distinct goals, and customized backstories.
* **Tasks:** Well-defined assignments given to the agents containing explicit descriptions, expected output formats, and assigned tooling.
* **Tools:** Alphanumeric interfaces or search APIs (like Tavily, Serper, or custom scrapers) that agents invoke to gather real-time internet data.
* **Crew:** The orchestrator module that brings the agents and tasks together to run the workflow loop.

## 🛠️ Features

* **Role-Based Agent Design:** Employs multiple collaborative agents instead of a single isolated assistant loop.
* **Internet Search Optimization:** Equipped with specialized search tools to autonomously parse, evaluate, and extract web data.
* **Streamlined Pipeline:** Integrated into a unified execution script (`app.py`) for clean runtime monitoring.

## 📋 Prerequisites

Before running the application, ensure you have:

* Python 3.9 or higher
* Valid API keys for your LLM provider (e.g., OpenAI, Groq, Anthropic)
* Access keys for your internet search tool provider (e.g., Serper API, Tavily)

## 🔧 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd Agentic-Crew-ai
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   This repository includes a `requirements.txt` file. Install all framework dependencies directly:
   ```bash
   pip install -r requirements.txt
   ```
   *(If customizing, make sure you have `crewai` and `crewai-tools` installed).*

4. **Configure Environment Keys:**
   Expose your operational API keys to the system:
   ```bash
   # On macOS/Linux:
   export OPENAI_API_KEY="your-openai-api-key"
   export SERPER_API_KEY="your-serper-api-key"

   # On Windows (Command Prompt):
   set OPENAI_API_KEY="your-openai-api-key"
   set SERPER_API_KEY="your-serper-api-key"
   ```

## 💻 Usage

To execute the multi-agent crew execution pipeline, run:

```bash
python app.py
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.
