# Capitalizer Automation

This project contains a Python script that automatically capitalizes any text copied to the clipboard and removes line breaks. The script will process text if it's not already all caps or if it contains line breaks.

## Setup and Installation

1.  **Install Python**: If you don't have Python installed, download it from the official website: <mcurl name="Python.org" url="https://www.python.org/downloads/"></mcurl>

2.  **Navigate to the project directory**: Open your terminal or command prompt and go to the directory where you saved this project.

    ```bash
    cd "c:\Users\babyk\OneDrive\Documents\GitHub\Capitalizer Automation"
    ```

3.  **Install dependencies**: Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Script

To run the script, you have two options:

1.  **Using the Python command (manual)**:

    Execute the following command in your terminal:

    ```bash
    python capitalizer.py
    ```

    The script will run in the background, monitoring your clipboard. To stop it, press `Ctrl+C` in the terminal where it's running.

**Toggle Functionality:** You can enable or disable the clipboard processing at any time by pressing the `Home` key.

2.  **Using the batch file (automated)**:

    Simply double-click the `run_capitalizer.bat` file. This will automatically install dependencies (if not already installed) and run the Python script. A command prompt window will open and remain open while the script is running. To stop the script, close this command prompt window.