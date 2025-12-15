from pathlib import Path          # Import Path class for modern, object-oriented filesystem paths
import logging                    # Import logging module for structured log messages

# Configure logging: INFO level and a simple format with timestamp + message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files you want to scaffold for your project
files = [
    "src/__init__.py",            # Marks 'src' as a Python package
    "src/helper.py",              # Placeholder for helper functions
    "src/prompt.py",              # Placeholder for prompt-related code
    ".env",                       # Environment variables file
    "setup.py",                   # Packaging/installation script
    "app.py",                     # Main application entry point
    "research/trials.ipynb"       # Jupyter notebook for experiments
]

# Iterate over each file path in the list
for filepath in files:
    path = Path(filepath)         # Convert string to Path object for cleaner operations

    # Ensure the parent directory exists (e.g., 'src', 'research')
    # parents=True → create intermediate directories if needed
    # exist_ok=True → don’t raise error if directory already exists
    path.parent.mkdir(parents=True, exist_ok=True)

    # Check if file does not exist OR is empty
    if not path.exists() or path.stat().st_size == 0:
        path.touch()              # Create an empty file (like 'open(..., "w").close()')
        logging.info(f"Created empty file: {path}")   # Log creation
    else:
        logging.info(f"{path.name} already exists")   # Log if file already present
