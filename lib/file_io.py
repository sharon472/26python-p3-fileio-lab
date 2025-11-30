def write_file(file_name, file_content):
    """Creates a .txt file and writes content to it."""
    full_name = f"{file_name}.txt"
    with open(full_name, "w") as f:
        f.write(file_content)


def append_file(file_name, append_content):
    """Appends content to an existing .txt file."""
    full_name = f"{file_name}.txt"
    with open(full_name, "a") as f:
        f.write(append_content)  # Write exactly what is passed


def read_file(file_name):
    """Reads and returns the content of a .txt file."""
    full_name = f"{file_name}.txt"
    with open(full_name, "r") as f:
        return f.read()



