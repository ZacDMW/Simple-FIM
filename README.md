# Simple File Integrity Monitor (FIM)

### Project Overview
A Python-based security tool that monitors a specific directory for unauthorized changes. It calculates the SHA-256 hash of files to create a "trusted baseline" and continuously checks for modifications.

**Why build this?**
File Integrity Monitoring is a critical requirement for compliance standards like **PCI-DSS** and is a core function of modern **EDR (Endpoint Detection & Response)** systems. I built this to understand how integrity checks work at a low level.

### Technologies Used
* **Language:** Python 3
* **Libraries:** `hashlib` (for SHA-256 hashing), `os`, `time`
* **Concept:** Cryptographic Hashing & Integrity Verification

### How to Run
1. Clone the repository.
2. Create a folder named `files_to_monitor` in the same directory.
3. Add some dummy text files into that folder.
4. Run the script: `python main.py`
5. **Step A:** Select "Create Baseline" to calculate initial hashes.
6. **Step B:** Modify one of the text files (change a word).
7. **Step C:** Run the script in "Monitor Mode" to detect the alert.

### What I Learned
* How to implement SHA-256 hashing in Python.
* The importance of baselining in Intrusion Detection Systems (IDS).
* How to handle file I/O operations securely.
