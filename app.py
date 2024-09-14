import os

def export_dummy_text(output_file):
    """Export dummy text to a text file."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write("This is a test.\n")
    print(f"Dummy text exported to {output_file}")

def main():
    # Change this to your project folder
    output_file = 'utils/folder_structure.txt'

    # Print the output file path
    print(f"Output file: {output_file}")

    # Export dummy text to a text file
    export_dummy_text(output_file)

if __name__ == "__main__":
    main()
