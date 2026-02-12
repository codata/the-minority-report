import os
import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".tmr"
CONFIG_FILE = CONFIG_DIR / "config.json"

DEFAULT_CONFIG = {
    "ollama_hosts": ["http://10.147.18.253:11434"]
}

def load_config():
    if not CONFIG_FILE.exists():
        return {}
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Failed to load config: {e}")
        return {}

def save_config(config):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Configuration saved to {CONFIG_FILE}")

def get_ollama_hosts():
    # Priority: Env Var > Config > Default
    env_hosts = os.environ.get('OLLAMA_HOSTS') or os.environ.get('OLLAMA_HOSTS_RAW') or os.environ.get('OLLAMA_HOST')
    
    if env_hosts:
        return [h.strip() for h in env_hosts.split(',')]
        
    config = load_config()
    return config.get("ollama_hosts", DEFAULT_CONFIG["ollama_hosts"])

def add_ollama_host(host):
    config = load_config()
    hosts = config.get("ollama_hosts", [])
    if host not in hosts:
        hosts.append(host)
    config["ollama_hosts"] = hosts
    save_config(config)

def set_ollama_hosts(hosts):
    config = load_config()
    config["ollama_hosts"] = hosts
    save_config(config)
