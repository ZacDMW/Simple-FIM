import hashlib
import os
import time

# 1. Define the path to monitor (current directory for this demo)
# In a real scenario, this could be a system folder like /etc/ or System32
MONITOR_DIR = './files_to_monitor'
BASELINE_FILE = 'baseline.txt'

def calculate_hash(filepath):
    """Reads a file and calculates its SHA-256 hash."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # Read the file in chunks to handle large files efficiently
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def create_baseline():
    """Calculates hashes for all files and saves them to baseline.txt."""
    if not os.path.exists(MONITOR_DIR):
        os.makedirs(MONITOR_DIR)
        print(f"Created directory: {MONITOR_DIR}. Put some files in there!")
    
    print("Calculating baseline...")
    with open(BASELINE_FILE, 'w') as f:
        for filename in os.listdir(MONITOR_DIR):
            filepath = os.path.join(MONITOR_DIR, filename)
            if os.path.isfile(filepath):
                file_hash = calculate_hash(filepath)
                f.write(f"{filename}|{file_hash}\n")
    print("Baseline created! System is now 'known good'.")

def monitor_files():
    """Continuously checks files against the baseline."""
    print("Beginning surveillance... (Press Ctrl+C to stop)")
    
    # Loading the baseline into a dictionary
    baseline = {}
    with open(BASELINE_FILE, 'r') as f:
        for line in f:
            filename, file_hash = line.strip().split('|')
            baseline[filename] = file_hash

    while True:
        time.sleep(2) # Checks every 2 seconds
        for filename in os.listdir(MONITOR_DIR):
            filepath = os.path.join(MONITOR_DIR, filename)
            if os.path.isfile(filepath):
                current_hash = calculate_hash(filepath)
                
                # Checks if file is new
                if filename not in baseline:
                    print(f"[ALERT] New File Created: {filename}")
                
                # Checks if file has changed
                elif baseline[filename] != current_hash:
                    print(f"[ALERT] File Modified: {filename}")
        
        #Checks for deleted files by comparing keys

if __name__ == "__main__":
    choice = input("Select Mode: (A) Create Baseline or (B) Begin Monitoring: ").upper()
    if choice == 'A':
        create_baseline()
    elif choice == 'B':
        if os.path.exists(BASELINE_FILE):
            monitor_files()
        else:
            print("Error: No baseline found. Run mode A first.")
