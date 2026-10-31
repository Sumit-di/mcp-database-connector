from mcp.server.fastmcp import FastMCP

# Initialise the FASTMCP server
mcp = FastMCP("Enterprise Database Connector")

# Mock database records for demonstration purposes
DATABASE = {
    "users": [{
        "id": 1,
        "name": "John Doe",
        "role": "Administrator"},
    {"id": 2,
        "name": "Jane Smith",
        "role": "Developer"}
    ],
    "metrics": [{"cpu_usage": "14%", "memory": "4.2GB / 16GB"}]
}

@mcp.tool()
def query_database(table_name: str) -> str:
    """
    Query the mock database table like 'users' or 'Metrics'.
    
    """
    if table_name in DATABASE:
        return str(DATABASE[table_name])

    return f"Error: Table '{table_name}' not found."

if __name__ == "__main__":
    mcp.run(transport="stdio")  
  