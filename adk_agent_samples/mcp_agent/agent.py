from dotenv import load_dotenv

load_dotenv()

import os
os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')
os.environ['POSTGRES_CONNECTION']= os.getenv('POSTGRES_CONNECTION_STRING')
os.environ['CONNECTION_URL']= os.getenv('CONNECTION_URL')
os.environ['P5_API_KEY']= os.getenv('P5_API_KEY')

postgres_connection_string = os.getenv('POSTGRES_CONNECTION_STRING')
connection_url = os.getenv('CONNECTION_URL')
p5_apikey = os.getenv('P5_API_KEY')

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters,SseServerParams
from google.adk.agents.llm_agent import LlmAgent

mcp_pg = MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-postgres",
                f"postgresql://{postgres_connection_string}"
            ],
        )
    )
mcp_weather = MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@h1deya/mcp-server-weather"
            ],
        )
    )
mcp_remote = MCPToolset(
        connection_params=SseServerParams(
            url=connection_url,
            headers={"P5APIKEY": p5_apikey,
                "P5AccountId": "4"},
            
            )
    )
    
root_agent = LlmAgent(
        name="mcp_agent",
        model="gemini-2.0-flash",
        tools=[mcp_pg, mcp_weather, mcp_remote],
        instruction="You are an assistant for the given data.",
    )