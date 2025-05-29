import hashlib
import os

def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file"""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
        return None

def save_original_hash(file_path):
    """Save the original hash of the file to hash_record.txt"""
    hash_value = calculate_hash(file_path)
    if hash_value:
        with open("hash_record.txt", "w") as f:
            f.write(hash_value)
        print("✅ Original hash saved successfully in 'hash_record.txt'.")

def check_file_integrity(file_path):
    """Check if the current file hash matches the original"""
    current_hash = calculate_hash(file_path)
    try:
        with open("hash_record.txt", "r") as f:
            original_hash = f.read()
        if current_hash == original_hash:
            print("✅ File is safe. No changes detected.")
        else:
            print("⚠️ WARNING: File has been modified!")
    except FileNotFoundError:
        print("❌ Hash record not found. Please save the original hash first.")

def main():
    print("\n🔒--- File Integrity Checker ---🔒")
    print("1. Save original file hash")
    print("2. Check file integrity")
    choice = input("Enter your choice (1/2): ")

    file_path = input("Enter the full path of the file: ").strip()

    if not os.path.exists(file_path):
        print("❌ The file does not exist.")
        return

    if choice == "1":
        save_original_hash(file_path)
    elif choice == "2":
        check_file_integrity(file_path)
    else:
        print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
