# Keylogger with Python and Pynput

This is a simple keylogger script written in Python using the `pynput` library. The script logs all keystrokes into a text file with timestamps. This can be used for monitoring keyboard activity on your computer.

## Features

- Logs every keystroke with a timestamp.
- Saves the logs to a specified directory.
- Lightweight and easy to set up.

## Prerequisites

- Python 3.x
- `pynput` library

You can install the required library using pip:

```bash
pip install pynput

Usage

1. Clone the repository:

git clone

https://github.com/rain-old/python-Keylogger.git

-name.git

cd repo-name

1. Specify the log directory:

Open the script and set the log_dir variable to the path where you want to save the keylogs. For example:

log_dir = "/path/to/your/log/ directory/"

Ensure that the directory exists, or the script will throw an error.

2. Run the script:

Execute the script using Python:

python keylogger.py

The script will start logging keystrokes to the specified directory in a file named keylogs.txt.

3. Stop the script:

To stop the keylogger, you can terminate the script manually (e.g., by pressing Ctrl + C in the terminal).

Security and Ethics

• This script is intended for educational purposes only.

• Use this code responsibly and only on systems that you own or have explicit permission to monitor.

• Unauthorized use of a keylogger can be illegal and unethical.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions for improvements.

Acknowledgments

• pynput library for handling keyboard input in Python
