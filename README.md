# EchoPath

EchoPath is a simple Python program that displays real-time resource usage on Windows. It shows the current CPU, memory, and disk usage, updating every second. This tool is useful for monitoring system performance in a lightweight and easy-to-understand manner.

## Features

- Displays CPU usage as a percentage.
- Displays memory usage as a percentage.
- Displays disk usage as a percentage.
- Updates every second.
- Simple and lightweight.

## Requirements

- Windows Operating System
- Python 3.x
- `psutil` library (can be installed via pip)

## Installation

1. Ensure Python is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
2. Install the `psutil` library using pip:

   ```bash
   pip install psutil
   ```

3. Download the `echopath.py` file.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `echopath.py` is located.
3. Run the program:

   ```bash
   python echopath.py
   ```

4. The program will display real-time CPU, memory, and disk usage. Press `Ctrl+C` to exit.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Acknowledgments

- This program uses the `psutil` library for accessing system information.