# PGAGI Assignment

This project is a Streamlit-based app that uses OpenAI's GPT models to generate questions based on user input.

## Features

- Streamlit web interface
- Integration with OpenAI API (via `openai>=1.0.0`)
- Modular design using `utils.py`

## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Killfrenzy-ai/automated-talent-scout-using-openai-API.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key to a `.env` file:
   ```
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```
