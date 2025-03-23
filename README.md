# Care Bot: Tamil Nadu Healthcare Assistant

A specialized healthcare chatbot focused on Tamil Nadu, India. Provides accurate information about healthcare facilities, government schemes like CMCHISTN, medical services, and healthcare policies in Tamil Nadu.

## Features

- User-friendly web interface for healthcare queries
- AI-powered responses using aixplain's language models
- Information about healthcare services, hospitals, and medical schemes in Tamil Nadu

## Tech Stack

- **Backend**: Flask (Python)
- **AI Integration**: aixplain
- **Environment Management**: python-dotenv
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Gunicorn

## Setup and Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in a `.env` file:
   ```
   TEAM_API_KEY=your_aixplain_api_key
   AGENT_ID=your_agent_id
   ```
4. Run the application: `python app.py`

## Deployment

This application is configured for deployment on Heroku using the included Procfile.

## License

[MIT](https://choosealicense.com/licenses/mit/) 