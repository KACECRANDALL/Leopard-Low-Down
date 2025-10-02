import sys
import subprocess
import os
import json

CONFIG_FILE = 'publish_config.json'

def run_git_command(args):
    result = subprocess.run(['git'] + args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running git {' '.join(args)}:\n{result.stderr}")
        sys.exit(result.returncode)
    else:
        print(result.stdout)

def main():
    if not os.path.exists(CONFIG_FILE):
        print(f"Config file '{CONFIG_FILE}' not found. Please run this script in the repo directory with the config file present.")
        sys.exit(1)
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        cfg = json.load(f)
    files = cfg.get('files', [])
    message = cfg.get('message', 'Automated commit')
    # Add files
    for file in files:
        run_git_command(['add', file])
    # Commit
    run_git_command(['commit', '-m', message])
    # Push (force if specified)
    if cfg.get('force', False):
        run_git_command(['push', '--force', 'origin', cfg.get('branch', 'main')])
    else:
        run_git_command(['push', 'origin', cfg.get('branch', 'main')])
    print('Publish complete.')

if __name__ == '__main__':
    main()
