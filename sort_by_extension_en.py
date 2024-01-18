# Importing Path class from the pathlib module for file path manipulation
from pathlib import Path

# Creating a dictionary to classify files based on their extension
# Each file extension is associated with a type (e.g., '.mp3' is associated with 'Sound')
dirs = {".aac": "Sound",
        ".ai": "Pictures",
        ".avi": "Movies",
        ".bat": "Scripts",
        ".bmp": "Pictures",
        ".c": "Source Code",
        ".csv": "Text",
        ".css": "Text",
        ".cpp": "Source Code",
        ".dll": "Executables",
        ".doc": "Text",
        ".docx": "Text",
        ".exe": "Executables",
        ".flac": "Sound",
        ".flv": "Movies",
        ".gif": "Pictures",
        ".gz": "Archives",
        ".html": "Text",
        ".java": "Scripts",
        ".jpeg": "Pictures",
        ".jpg": "Pictures",
        ".js": "Text",
        ".json": "Text",
        ".mkv": "Movies",
        ".mov": "Movies",
        ".mp3": "Sound",
        ".mp4": "Movies",
        ".odp": "Presentations",
        ".ods": "Text",
        ".odt": "Text",
        ".pdf": "Text",
        ".png": "Pictures",
        ".ppt": "Presentations",
        ".pptx": "Presentations",
        ".psd": "Pictures",
        ".py": "Scripts",
        ".rar": "Archives",
        ".rtf": "Text",
        ".sh": "Scripts",
        ".svg": "Pictures",
        ".tar": "Archives",
        ".tiff": "Pictures",
        ".txt": "Text",
        ".wav": "Sound",
        ".webp": "Pictures",
        ".wmv": "Movies",
        ".xls": "Text",
        ".xlsx": "Text",
        ".xlsm": "Text",
        ".xml": "Text",
        ".zip": "Archives"}

# Setting the working directory, here the user's Desktop
tri_dir = Path.home() / "Desktop"

# Retrieving all files in the working directory
files = [f for f in tri_dir.iterdir() if f.is_file()]

# Iterating over each file in the directory
for file in files:
    try:
        # Determining the destination subdirectory based on the file extension
        # If the extension is not in the dictionary, the file is classified under 'Others'
        output_dir = tri_dir / dirs.get(file.suffix.lower(), "Others")

        # Creating the subdirectory if it doesn't already exist
        output_dir.mkdir(exist_ok=True)

        # Moving the file to the appropriate subdirectory
        file.rename(output_dir / file.name)
    except Exception as error:
        # Displaying an error if file movement fails
        print(f"Error moving file {file}: {error}")
