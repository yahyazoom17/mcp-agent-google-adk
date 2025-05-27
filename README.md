# MCP Agent Google ADK

A powerful MCP (Model Context Protocol) Agent built using Google's Agent Development Kit (ADK) that integrates multiple data sources and services through MCP toolsets.

## Overview

This project demonstrates how to build an intelligent agent using Google ADK that can interact with:
- **PostgreSQL databases** via MCP server
- **Weather services** for real-time weather data
- **Remote services** through SSE connections

The agent uses Google's Gemini 2.0 Flash model to provide intelligent responses and can execute complex queries across multiple data sources.

## Features

- 🤖 **Multi-Modal Agent**: Powered by Gemini 2.0 Flash for advanced reasoning
- 🗄️ **Database Integration**: Direct PostgreSQL access through MCP
- 🌤️ **Weather Data**: Real-time weather information
- 🔗 **Remote Service Integration**: SSE-based remote service connections
- 🛠️ **Extensible Architecture**: Easy to add new MCP toolsets
- 🔐 **Secure Configuration**: Environment-based secret management

## Prerequisites

- Python 3.8+
- Node.js and npm (for MCP servers)
- PostgreSQL database (if using database features)
- Google API credentials
- API access (for remote services)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mcp-agent-google-adk.git
cd mcp-agent-google-adk
```

### 2. Set Up Python Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements
```

### 3. Environment Configuration

Create a `.env` file in the root directory:

```env
# Google API Configuration
GOOGLE_API_KEY=your_google_api_key_here

# PostgreSQL Configuration
POSTGRES_CONNECTION_STRING=username:password@localhost:5432/database_name

# Remote Service Configuration
CONNECTION_URL=your_sse_connection_url
API_KEY=your_api_key
```

### 4. Install Node.js Dependencies

The MCP servers require Node.js packages that are installed automatically when the agent starts:
- `@modelcontextprotocol/server-postgres` - PostgreSQL MCP server
- `@h1deya/mcp-server-weather` - Weather MCP server

## Usage

### Basic Usage

```python
from adk_agent_samples.mcp_agent import agent

# The agent is automatically configured and ready to use
response = agent.root_agent.run("What's the weather like today?")
print(response)
```

### Database Queries

```python
# Query your PostgreSQL database
response = agent.root_agent.run("Show me the latest records from the users table")
print(response)
```

### Multi-Source Queries

```python
# Combine data from multiple sources
response = agent.root_agent.run(
    "Get the current weather and also check if there are any users in our database from that city"
)
print(response)
```

## Architecture

The agent is built with three main MCP toolsets:

### 1. PostgreSQL Toolset (`mcp_pg`)
- **Connection**: Stdio-based MCP server
- **Purpose**: Direct database access and querying
- **Server**: `@modelcontextprotocol/server-postgres`

### 2. Weather Toolset (`mcp_weather`)
- **Connection**: Stdio-based MCP server  
- **Purpose**: Real-time weather data retrieval
- **Server**: `@h1deya/mcp-server-weather`

### 3. Remote Toolset (`mcp_remote`)
- **Connection**: SSE (Server-Sent Events) based
- **Purpose**: Integration with external services
- **Authentication**: API key and account ID headers

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google API key for Gemini model | Yes |
| `POSTGRES_CONNECTION_STRING` | PostgreSQL database connection | Yes |
| `CONNECTION_URL` | SSE server URL for remote services | Yes |
| `API_KEY` | Service API key | Yes |

### Agent Configuration

The agent is configured with:
- **Model**: `gemini-2.0-flash`
- **Name**: `mcp_agent`
- **Instruction**: "You are an assistant for the given data."
- **Tools**: All three MCP toolsets

## Development

### Project Structure

```
mcp-agent-google-adk/
├── adk_agent_samples/
│   └── mcp_agent/
│       ├── __init__.py
│       └── agent.py          # Main agent configuration
├── .env                      # Environment variables (create this)
├── .gitignore               # Python gitignore
├── requirements             # Python dependencies
└── README.md               # This file
```

### Adding New MCP Toolsets

To add a new MCP toolset:

1. **Create the toolset**:
```python
new_toolset = MCPToolset(
    connection_params=StdioServerParameters(
        command="npx",
        args=["-y", "@your/mcp-server-package"]
    )
)
```

2. **Add to agent tools**:
```python
root_agent = LlmAgent(
    name="mcp_agent",
    model="gemini-2.0-flash",
    tools=[mcp_pg, mcp_weather, mcp_remote, new_toolset],  # Add here
    instruction="You are an assistant for the given data.",
)
```

### Environment Setup for Development

```bash
# Install development dependencies
pip install -e .

# Set up pre-commit hooks (recommended)
pip install pre-commit
pre-commit install
```

## Troubleshooting

### Common Issues

**Issue: Google API Key not working**
```
Error: Authentication failed
Solution: Ensure your GOOGLE_API_KEY is valid and has access to Gemini API
```

**Issue: PostgreSQL connection failed**
```
Error: Connection refused
Solution: Check your POSTGRES_CONNECTION_STRING format and database accessibility
```

**Issue: MCP server installation fails**
```
Error: npx command not found
Solution: Install Node.js and npm, ensure they're in your PATH
```

**Issue: Remote service connection timeout**
```
Error: SSE connection failed
Solution: Verify CONNECTION_URL and API_KEY are correct
```

### Debug Mode

To enable verbose logging, set environment variable:
```bash
export GOOGLE_ADK_DEBUG=true
```

## Dependencies

### Core Dependencies
- `google-adk==1.0.0` - Google Agent Development Kit
- `python-dotenv==1.1.0` - Environment variable management
- `fastapi==0.115.12` - Web framework (if needed)
- `httpx==0.28.1` - HTTP client for API calls

### Google Cloud Dependencies
- `google-genai==1.16.1` - Google Generative AI
- `google-cloud-aiplatform==1.94.0` - AI Platform integration
- Various other Google Cloud services

### MCP Dependencies
- `mcp==1.9.1` - Model Context Protocol implementation
- `httpx-sse==0.4.0` - Server-Sent Events support

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [Google ADK Documentation](https://developers.google.com/adk)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)

## Support

For questions and support:
- Create an issue on GitHub
- Check the [Google ADK documentation](https://developers.google.com/adk)
- Review MCP server documentation for specific toolset issues

---

Built with ❤️ using Google ADK and Model Context Protocol
