import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

# Set API key in environment (required by aixplain)
os.environ['TEAM_API_KEY'] = os.getenv('TEAM_API_KEY')
print(f"TEAM_API_KEY set to: {os.environ.get('TEAM_API_KEY')[:10]}...")

# Import aixplain modules after setting environment variables
from aixplain.factories import ModelFactory, AgentFactory

app = Flask(__name__)

# Get the agent ID from environment variable
AGENT_ID = os.getenv('AGENT_ID')
TEAM_API_KEY = os.getenv('TEAM_API_KEY')

if not AGENT_ID or not TEAM_API_KEY:
    raise ValueError("AGENT_ID and TEAM_API_KEY must be set in environment variables")

# Initialize the agent
agent = AgentFactory.get(AGENT_ID)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Care Bot - Tamil Nadu Healthcare Assistant</title>
            <style>
                body { 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                    margin: 0; 
                    padding: 0;
                    line-height: 1.6;
                    background-color: #f8fcfd;
                    color: #2c3e50;
                }
                .container { 
                    max-width: 800px; 
                    margin: 0 auto;
                    padding: 40px 20px;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.05);
                    border-radius: 10px;
                    background-color: white;
                    margin-top: 40px;
                    margin-bottom: 40px;
                }
                h1 { 
                    color: #1a73e8; 
                    border-bottom: 2px solid #e6f2fa;
                    padding-bottom: 15px;
                    margin-top: 0;
                }
                .chat-form { 
                    margin-top: 30px; 
                }
                textarea { 
                    width: 100%; 
                    padding: 15px; 
                    margin-bottom: 15px;
                    border: 1px solid #d9e8f6;
                    border-radius: 8px;
                    font-size: 16px;
                    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
                    resize: vertical;
                    font-family: inherit;
                    transition: border-color 0.2s;
                }
                textarea:focus {
                    outline: none;
                    border-color: #4dabf7;
                    box-shadow: 0 0 0 3px rgba(77, 171, 247, 0.2);
                }
                button { 
                    background-color: #1a73e8; 
                    color: white; 
                    padding: 12px 24px; 
                    border: none; 
                    border-radius: 6px;
                    cursor: pointer;
                    font-weight: 600;
                    font-size: 16px;
                    transition: background-color 0.2s;
                }
                button:hover { 
                    background-color: #1557b0; 
                }
                #response { 
                    margin-top: 30px; 
                    padding: 20px; 
                    border-radius: 8px; 
                    background-color: #e6f2fa;
                    min-height: 60px;
                    border-left: 4px solid #1a73e8;
                }
                p {
                    color: #5f6368;
                    font-size: 17px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Care Bot: Tamil Nadu Healthcare Assistant</h1>
                <p>Ask any questions about healthcare services, hospitals, or medical schemes in Tamil Nadu.</p>
                <div class="chat-form">
                    <textarea id="query" rows="4" placeholder="Type your healthcare query here..."></textarea>
                    <button onclick="sendQuery()">Send Query</button>
                </div>
                <div id="response"></div>
                <script>
                    async function sendQuery() {
                        const query = document.getElementById('query').value;
                        const response = document.getElementById('response');
                        response.innerHTML = 'Loading...';
                        
                        try {
                            const result = await fetch('/chat', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json',
                                },
                                body: JSON.stringify({ query: query })
                            });
                            const data = await result.json();
                            response.innerHTML = data.response;
                        } catch (error) {
                            response.innerHTML = 'Error: Could not get response from the server.';
                        }
                    }
                </script>
            </div>
        </body>
    </html>
    """

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({'error': 'No query provided'}), 400

        # Use the agent to get response
        response = agent.run(data['query'])
        
        # Extract the actual text from the response object
        # The agent response is a complex object with nested data
        response_text = response.data.output
        
        return jsonify({'response': response_text})

    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True) 