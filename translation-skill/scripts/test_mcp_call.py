
import sys
import json
import subprocess
import threading

def read_output(process):
    """Reads stdout from the process and prints it."""
    for line in iter(process.stdout.readline, ''):
        if line.strip():
            print(f"STDOUT: {line.strip()}")
            # Try to catch JSON responses
            if line.strip().startswith('{'):
                try:
                    data = json.loads(line.strip())
                    if "result" in data or "error" in data:
                        # This is likely our response
                        # We can't return it easily from this thread, but we can print it
                        pass
                except:
                    pass

def main():
    # Start the server process once
    process = subprocess.Popen(
        [sys.executable, "translation-skill/scripts/mcp_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=sys.stderr, # Pipe stderr directly to our stderr
        text=True,
        bufsize=1 # Line buffered
    )

    try:
        print("Testing MCP Server Initialize...")
        # 1. Initialize
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test-client", "version": "1.0"}
            }
        }
        
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        
        # Read response (simple blocking read for demo)
        # FastMCP outputs JSON lines
        response_line = process.stdout.readline()
        print(f"Initialize Response: {response_line}")
        
        # Check if initialized
        if "serverInfo" not in response_line:
             # It might be a log line? FastMCP shouldn't print logs to stdout if configured correctly, 
             # but we saw logs in stderr in previous run.
             pass

        # Send initialized notification
        init_notif = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized"
        }
        process.stdin.write(json.dumps(init_notif) + "\n")
        process.stdin.flush()

        print("\nTesting understand_and_translate tool...")
        # 2. Call Tool
        tool_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": "understand_and_translate",
                "arguments": {
                    "term": "Digital Twin",
                    "context": "A digital representation of a physical object.",
                    "languages": "fr",
                    "models": "gpt-oss:latest"
                }
            }
        }
        process.stdin.write(json.dumps(tool_request) + "\n")
        process.stdin.flush()
        
        # Read response
        # The tool might take time (LLM call), so we block reading
        response_line = process.stdout.readline()
        print(f"Tool Call Response: {response_line}")

    finally:
        process.terminate()

if __name__ == "__main__":
    main()
