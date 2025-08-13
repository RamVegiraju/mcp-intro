# MCP Introduction
We'll explore how you can create a basic MCP server and integrate with hosts such as Claude Desktop. Associated video coming.

## Setup
Instructions from: https://pypi.org/project/mcp/.
```
uv init mcp-server-demo
cd mcp-server-demo
uv add "mcp[cli]"
```

## Local Debugging
Ensure the transport is stdio:
```
uv run mcp dev server.py
```
Can test your tools, resources, prompts functionality on the UI.

## Claude Desktop
# You can automatically add your server to Claude Desktop config file with following command:
```
uv run mcp install main.py
```

For a Mac you can find your Claude desktop JSON config file with your servers in the following location:
```
/Users/mac-username/Library/Application Support/Claude/claude_desktop_config.json
```
Here you can add other servers manually if you would like as well traditionally most public servers have a JSON configuration you can add directly.
