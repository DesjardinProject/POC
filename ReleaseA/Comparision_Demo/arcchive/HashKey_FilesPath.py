#####################################################################################################
#                                   This Code written by Soma Pusarla                               #
#                                                                                                   #
#                            We will generate the hash key value for each file                      #
#                                                 Confidential                                      #
#####################################################################################################

import os
import hashlib

def calculate_file_hash(filepath, hash_algorithm="sha256"):
    """
    Calculate the hash of a file using the specified hash algorithm.
    """
    hash_func = hashlib.new(hash_algorithm)
    with open(filepath, "rb") as file:
        chunk = file.read(8192)
        while chunk:
            hash_func.update(chunk)
            chunk = file.read(8192)
    return hash_func.hexdigest()

def main(input_folder, output_folder, hash_algorithm="sha256"):
    """
    Calculate the hash for each file in the input folder and write it to a separate output file in the output folder.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        filepath = os.path.join(input_folder, filename)
        
        # Skip if it's not a file
        if not os.path.isfile(filepath):
            continue
        
        # Calculate the hash of the file
        file_hash = calculate_file_hash(filepath, hash_algorithm)
        
        # Prepare the output filename with '_hash_output' suffix
        output_filename = f"{os.path.splitext(filename)[0]}_hash_output.txt"
        output_filepath = os.path.join(output_folder, output_filename)
        
        # Write the hash to the output file in the output folder
        with open(output_filepath, "w") as output_file:
            output_file.write(f"Filename: {filename}\n")
            output_file.write(f"Hash ({hash_algorithm}): {file_hash}\n")
        
        print(f"Hash for '{filename}' written to '{output_filepath}'")

# Example usage:
# Replace the folder paths with the actual paths for input and output folders
input_folder_path = "/tmp/scripts/Input_File"
output_folder_path = "/tmp/scripts/Output_File"
main(input_folder_path, output_folder_path)
