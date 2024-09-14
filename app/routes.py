from flask import Blueprint, request, jsontify
from .agents.vector_agent import VectorAgent
from .agents.navigation_agent import NavigationAgent

main = Blueprint('main', __name__)

@main.route('/agent', methods=['POST'])
def agent_route():
    message = request.get_json().get('message')

    if not message:
        return jsontify({'error': 'No message provided'}), 400

    agent = NavigationAgent.choose_agent(message)

    result = agent.perform_task()
    return jsontify(result)
