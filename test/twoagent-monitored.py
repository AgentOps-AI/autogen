import os
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from agentops import Client

ao_client = Client(api_key=os.environ.get('AGENTOPS_API_KEY'),
                   tags=['autogen', 'Autogen Example'])

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# pass in the AgentOps client instance for agent monitoring and visibility
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list}, ao_client=ao_client)
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
