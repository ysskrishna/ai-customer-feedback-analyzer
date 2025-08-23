# AI Customer Feedback Analyzer

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.47+-red.svg)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg)](https://openai.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.9+-orange.svg)](https://pydantic.dev/)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-green.svg)](https://docs.astral.sh/uv/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A powerful, AI-powered customer feedback analyzer built with Streamlit and OpenAI's GPT Models. Features intelligent sentiment analysis, actionable item extraction, and structured feedback insights. Perfect for businesses seeking to systematically analyze customer feedback with automated categorization, priority assessment, and actionable recommendations.


## 📌 Features

### **Intelligent Analysis**

- **Sentiment Analysis**: Automatically detects positive, negative, or neutral sentiment
- **Actionable Item Extraction**: Identifies specific actions with priority levels (High, Medium, Low)
- **Smart Categorization**: Organizes feedback into relevant categories:
  - Product Quality
  - Customer Service
  - Pricing
  - Delivery
  - User Experience
  - Features
  - Bugs
  - Suggestions
  - Other

### **Structured Output**

- **JSON Format**: Clean, structured data for easy integration
- **Priority Assessment**: Intelligent prioritization based on impact and severity
- **Evidence-Based Reasoning**: Each actionable item includes concrete reasoning from the feedback
- **Concise Insights**: Maximum 5 actionable items per analysis to focus on what matters most

## 🛠 Tech Stack

* **Python 3.11+**
* **Streamlit** (Web UI)
* **OpenAI GPT-4o** (AI Analysis)
* **Pydantic** (Data Validation)
* **Python-dotenv** (Environment Management)
* **UV** (Package Management)

## 🚀 Quick Start

### **Prerequisites**
- Python 3.11 or higher
- OpenAI API key
- UV package manager (recommended) or pip

### **1. Clone the Repository**

```bash
git clone https://github.com/ysskrishna/ai-customer-feedback-analyzer.git
cd ai-customer-feedback-analyzer
```

### **2. Install Dependencies**

```bash
# Install UV if you haven't already
pip install uv

# Install project dependencies
uv sync
```

### **3. Set Up Environment**

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### **4. Run the Application**

```bash
uv run streamlit run main.py
```

### **5. Open in Browser**

Visit **[http://localhost:8501](http://localhost:8501)**

## 📂 Project Structure

```
ai-customer-feedback-analyzer/
├── ai/                          # AI analysis logic
│   ├── analyzer.py             # Main feedback analysis function
│   ├── client.py               # OpenAI client configuration
│   └── prompts.py              # Analysis prompts and instructions
├── core/                       # Core application logic
│   └── config.py              # Configuration and environment setup
├── models/                     # Data models and schemas
│   ├── enums.py               # Enum definitions for categories and priorities
│   └── models.py              # Pydantic models for structured output
├── workspace/                  # Workspace files
│   └── ai_customer_feedback.md # Documentation
├── main.py                     # Main Streamlit application
├── pyproject.toml             # Project configuration and dependencies
└── README.md                  # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is released under the **MIT License**.
See [LICENSE](LICENSE) for details.

## 👨‍💻 Author

**Y. Siva Sai Krishna** ([@ysskrishna](https://github.com/ysskrishna))

Built with ❤️ for better customer understanding and business insights.