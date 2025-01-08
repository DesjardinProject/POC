import hashlib
import os

def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def save_hash_to_file(file_path, hash_value, output_file):
    """Save the file path and its hash value to a text file."""
    try:
        with open(output_file, "a") as f:
            f.write(f"{file_path}: {hash_value}\n")
        print(f"Saved hash for {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    # Specify the files you want to hash
    files_to_hash = [
        "/FCELCM_Consolidated/ELCM/MAIN/UIXML/ENG/",
        "/FCELCM_Consolidated/MAIN/UIXML/ENG/",
    ]

    # Output file to store the hash values
    output_file = "UIXML_hashes.txt"

    # Calculate and store the hash for each file
    for file_path in files_to_hash:
        hash_value = calculate_hash(file_path)
        if hash_value:
            save_hash_to_file(file_path, hash_value, output_file)

if __name__ == "__main__":
    main()
