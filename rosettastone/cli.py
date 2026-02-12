import argparse
import sys
from .config import set_ollama_hosts, get_ollama_hosts

def init_main():
    print("Initialize The Minority Report Configuration")
    print("--------------------------------------------")
    
    current_hosts = get_ollama_hosts()
    print(f"Current Ollama Hosts: {', '.join(current_hosts)}")
    
    try:
        new_hosts_input = input("Enter Ollama hosts (comma separated) [Leave empty to keep current]: ").strip()
        
        if new_hosts_input:
            hosts = [h.strip() for h in new_hosts_input.split(',') if h.strip()]
            set_ollama_hosts(hosts)
            print(f"Updated hosts: {hosts}")
        else:
            print("No changes made.")
            
    except KeyboardInterrupt:
        print("\n\nCancelled.")
        sys.exit(0)

if __name__ == "__main__":
    init_main()
