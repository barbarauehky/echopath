import psutil
import time
import os

def clear_console():
    """Clear the console for Windows."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_resource_usage():
    """Displays real-time resource usage."""
    try:
        while True:
            clear_console()

            # Get CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU Usage: {cpu_usage}%")

            # Get Memory usage
            memory_info = psutil.virtual_memory()
            print(f"Memory Usage: {memory_info.percent}%")

            # Get Disk usage
            disk_info = psutil.disk_usage('/')
            print(f"Disk Usage: {disk_info.percent}%")

            # Wait for a second
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting EchoPath...")
        exit()

if __name__ == "__main__":
    print("EchoPath - Real-time Resource Usage Monitor")
    print("Press Ctrl+C to exit.\n")
    display_resource_usage()