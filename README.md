# basic-antivirus
A lightweight Python-based file integrity checker and signature scanner designed to scan local directories recursively and detect known malicious files using a SHA-256 hash database.



# Simple Python Antivirus / File Integrity Checker

A lightweight, educational utility built in Python that scans directories recursively, computes SHA-256 hashes for files, and compares them against a known database of file signatures (hashes) to detect potential threats or matches.

## Features

* **Recursive Directory Scanning:** Automatically traverses through target directories and subdirectories.
* **SHA-256 Hashing:** Computes cryptographic SHA-256 hashes for files using optimized memory chunks to safely handle large files.
* **Signature Matching:** Compares scanned file hashes against an external list of known indicators/signatures.
* **File Structure Inspection Utility:** Includes a secondary utility script to inspect and visualize local directory trees.

---

## Project Structure

```text
├── Anti virus (1).py         # Core signature-matching scanner script
├── Anti virus.py             # Simple directory tree inspector script
└── full-hash-sha256-aa.txt   # Database of SHA-256 signatures/hashes
