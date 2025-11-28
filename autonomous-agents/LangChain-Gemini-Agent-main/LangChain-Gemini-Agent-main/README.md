# AI Research Agent with LangChain and Google Gemini

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-v0.x-green.svg)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-orange.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

## Project Overview

This project demonstrates the creation of an AI-powered research agent using the **LangChain** framework and **Google's Gemini model**. The agent is designed to answer user queries by autonomously leveraging external tools like web search (DuckDuckGo) and Wikipedia, synthesizing information, and presenting it in a structured, easy-to-read format.

It's a foundational step into building more complex, tool-using AI systems.

## Features

-   **Intelligent Reasoning:** Utilizes Google Gemini (`gemini-1.5-flash` or `gemini-1.5-pro`) to understand queries, plan research steps, and synthesize findings.
-   **Web Search Capability:** Integrates with `DuckDuckGoSearchRun` to fetch up-to-date information from the internet.
-   **Wikipedia Integration:** Uses `WikipediaQueryRun` to access and summarize foundational knowledge from Wikipedia.
-   **Structured Output:** Employs Pydantic models to ensure the research results (topic, summary, sources, tools used) are always returned in a consistent, machine-readable JSON format.
-   **Persistent Storage:** Includes a custom `save_tool` to save comprehensive research summaries to a text file locally.
-   **Modular Design:** Built with LangChain's agent and tool abstractions, making it extensible and easy to swap components.

## Getting Started

Follow these steps to set up and run the AI Research Agent on your local machine.

### Prerequisites

-   **Python 3.9+** installed on your system.
-   A **Google Gemini API Key**. You can obtain one from the [Google AI Studio](https://ai.google.dev/).

### Installation

1.  **Clone the repository:**
    If you haven't already, clone this repository to your local machine:
    ```bash
    git clone [https://github.com/Punith18-18/LangChain-Gemini-Agent.git](https://github.com/Punith18-18/LangChain-Gemini-Agent.git)
    cd LangChain-Gemini-Agent
    ```
2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS / Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    Once your virtual environment is active, install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    *(If you haven't created `requirements.txt` yet, run `pip freeze > requirements.txt` first.)*

### Configuration

1.  **Create a `.env` file:**
    In the root of your `LangChain-Gemini-Agent` directory, create a new file named `.env`.
2.  **Add your API key:**
    Open the `.env` file and add your Google Gemini API key:
    ```
    GOOGLE_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
    ```
    Replace `YOUR_ACTUAL_GEMINI_API_KEY_HERE` with the API key you obtained from Google AI Studio. **Do not share this file publicly.**

### Running the Agent

1.  **Activate your virtual environment** (if not already active):
    ```bash
    # On Windows:
    .\venv\Scripts\activate
    # On macOS / Linux:
    source venv/bin/activate
    ```
2.  **Run the main script:**
    ```bash
    python main.py
    ```
3.  The agent will prompt you with `What can i help you research? `. Enter your research query.

    Example interaction:
    ```
    What can i help you research? what is life

    > Entering new AgentExecutor chain...
    # (Agent's thought process and tool calls will be displayed here due to verbose=True)
    ...
    > Finished chain.
    topic='What is Life?' summary="Defining life is a complex scientific and philosophical question. ..." sources=['Scientific American: What is Life?', 'National Geographic: What is Life?'] tools_used=['default_api.search', 'default_api.wikipedia']
    ```

## Project Structure
## Future Improvements

-   **Memory Integration:** Implement conversational memory to allow for multi-turn interactions and follow-up questions.
-   **Advanced Tooling:** Add more specialized tools (e.g., a calculator, specific data APIs, summarization tools).
-   **Error Handling:** Enhance error handling within tools and the agent's parsing logic for more graceful failures.
-   **User Interface:** Develop a simple web-based or desktop UI for a more interactive experience.
-   **Prompt Optimization:** Further refine the system prompt to guide the LLM's behavior and output quality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
