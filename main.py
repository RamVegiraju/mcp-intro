# server.py
from mcp.server.fastmcp import FastMCP

# for more structured data
from pydantic import BaseModel, Field

# create a MCP server
mcp = FastMCP("hello-mcp-py")


class BioData(BaseModel):
    """Human biodata structure"""

    age: int = Field(description="Age of the person")
    gender: str = Field(description="Gender of the person")
    occupation: str = Field(description="Occupation of the person")
    interests: list[str] = Field(description="Interests of the person")

# random people list
people_db: dict[str, BioData] = {
    "Ram":  BioData(age=20, gender="Male",   occupation="Engineer", interests=["Reading", "Traveling"]),
    "Shyam":BioData(age=22, gender="Male",   occupation="Doctor",   interests=["Reading", "Traveling"]),
    "Sita": BioData(age=21, gender="Female", occupation="Teacher",  interests=["Reading", "Traveling"]),
    "Gita": BioData(age=23, gender="Female", occupation="Lawyer",   interests=["Reading", "Traveling"]),
    "Hari": BioData(age=24, gender="Male",   occupation="Engineer", interests=["Reading", "Traveling"]),
}

# simple add tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# return biodata tool using pydantic model and people list (mock database)
@mcp.tool()
def return_biodata(name: str) -> BioData:
    """Return biodata for a known person name."""
    try:
        return people_db[name]
    except KeyError:
        # MCP hosts will display this as a tool error
        raise ValueError(f"Person '{name}' not found in database")

if __name__ == "__main__":
    mcp.run(transport="stdio")