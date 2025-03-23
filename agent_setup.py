import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

# Set API key in environment (required by aixplain)
os.environ['TEAM_API_KEY'] = os.getenv('TEAM_API_KEY')
print(f"TEAM_API_KEY set to: {os.environ.get('TEAM_API_KEY')[:10]}...")

# Import aixplain modules after setting environment variables
from aixplain.factories import ModelFactory, AgentFactory
from aixplain.modules.agent import Tool

def create_and_deploy_agent():
    """
    Create and deploy the Care Bot agent using aixplain's AgentFactory.
    Returns the deployed agent instance.
    """
    try:
        # Get API key from environment variable
        api_key = os.getenv('TEAM_API_KEY')  # Note: Changed to TEAM_API_KEY as per docs
        if not api_key:
            raise ValueError("TEAM_API_KEY environment variable not set")

        # Create agent configuration
        print("Creating Care Bot...")
        agent = AgentFactory.create(
            name="Care Bot",
            description="""A specialized healthcare chatbot focused on Tamil Nadu, India. 
            Provides accurate information about healthcare facilities, government schemes like CMCHISTN,
            medical services, and healthcare policies in Tamil Nadu.""",
            llm_id="6646261c6eb563165658bbb1"  # GPT-4o as specified in docs
        )
        
        # Test the agent with a sample query
        test_query = "What is the CMCHISTN scheme in Tamil Nadu?"
        print(f"\nTesting bot with query: {test_query}")
        response = agent.run(test_query)
        print(f"Test response: {response}")

        print("\nBot setup completed successfully!")
        print(f"Agent ID: {agent.id}")
        return agent

    except Exception as e:
        print(f"Error in bot setup: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        agent = create_and_deploy_agent()
        print("\nUse this agent ID in your Flask application:", agent.id)
    except Exception as e:
        print(f"Failed to set up bot: {str(e)}") 