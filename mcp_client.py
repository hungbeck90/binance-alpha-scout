import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


MCP_URL = "https://agent.binance.com/mcp/agentic"


async def list_binance_tools():
    async with streamable_http_client(MCP_URL) as (
        read_stream,
        write_stream
    ):
        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            print("\n=== BINANCE AGENT OS MCP ===")

            tools = await session.list_tools()

            print("Connected successfully.")
            print(f"Available tools: {len(tools.tools)}\n")

            for tool in tools.tools:
                print(f"- {tool.name}")

                if tool.description:
                    print(f"  {tool.description[:150]}")

                print()


if __name__ == "__main__":
    asyncio.run(list_binance_tools())