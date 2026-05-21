# Agentic Crew AI

## Description

This project implements an agentic AI system using CrewAI framework. It leverages agent tasks and tools for internet search capabilities, allowing multiple AI agents to collaborate and accomplish complex tasks autonomously.

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip or conda

### Steps

1. Clone the repository:
```bash
git clone https://github.com/zak-7869/agentic-crew-ai.git
cd agentic-crew-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and settings
```

## Usage

1. Run the main agent:
```bash
python main.py
```

2. The agents will perform tasks using internet search tools to gather information and provide insights.

## Technologies Used

- **CrewAI**: Multi-agent orchestration framework
- **Python**: Core programming language
- **Internet Search Tools**: For real-time information retrieval
- **Task Management**: Agent task coordination

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
