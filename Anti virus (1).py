import os
import hashlib

def sha256_file(filepath):
    sha256 = hashlib.sha256()

    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return None

def load_hashes(filename):
    virushashlist = set()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                virushashlist.add(line.strip())
    except FileNotFoundError:
        print(f"Hash file not found: {filename}")
    return virushashlist


def dir_cmd(path, virushashlist, level=0):
    result = []

    if not os.path.exists(path):
        return [f"path not found: {path}"]

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        hash_text = sha256_file(str(full_path))
        if os.path.isfile(full_path):
            if hash_text in virushashlist:
                result.append(f"FOUND MATCH: {item}")
        else:
            result += dir_cmd(full_path, virushashlist, level + 1)

    return result


hash_file = "full-hash-sha256-aa.txt"
virushashlist = load_hashes(hash_file)

path = input("Enter the path to scan: ")
results = dir_cmd(path, virushashlist)

for r in results:
    print(r)