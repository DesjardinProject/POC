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


def process_files_from_input(input_folder, output_folder, hash_algorithm="sha256"):
    """
    Read each text file in the input folder, process each file path listed in the file,
    and generate a hash for each file path.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each file in the input folder
    for input_filename in os.listdir(input_folder):
        input_filepath = os.path.join(input_folder, input_filename)

        # Skip if it's not a file
        if not os.path.isfile(input_filepath):
            continue

        # Prepare the output filename with '_hash_output' suffix
        output_filename = f"{os.path.splitext(input_filename)[0]}_hash_output.txt"
        output_filepath = os.path.join(output_folder, output_filename)

        with open(input_filepath, "r") as input_file, open(output_filepath, "w") as output_file:
            # Write the header to the output file
            output_file.write(f"Hashes for files listed in '{input_filename}':\n\n")

            # Process each line (file path) in the input file
            for line in input_file:
                file_path = line.strip()  # Get the file path, removing any trailing newline or whitespace

                # Skip if the line is empty
                if not file_path:
                    continue

                # Check if the file path exists
                if os.path.isfile(file_path):
                    # Calculate the hash of the file
                    file_hash = calculate_file_hash(file_path, hash_algorithm)
                    # Write the filename and its hash to the output file
                    output_file.write(f"File Path: {file_path}\n")
                    output_file.write(f"Hash ({hash_algorithm}): {file_hash}\n\n")
                    print(f"Hash for '{file_path}' written to '{output_filename}'")
                else:
                    # Write a message if the file path does not exist
                    output_file.write(f"File Path: {file_path} - Not Found\n\n")
                    print(f"File '{file_path}' not found, skipped.")


# Specify the folder paths
input_folder_path = r"C:\Users\Soma Pusarla\Documents\Desjardins\Comparision_Hashkey\Input_File"
output_folder_path = r"C:\Users\Soma Pusarla\Documents\Desjardins\Comparision_Hashkey\Output_File"

# Run the main processing function
process_files_from_input(input_folder_path, output_folder_path)
