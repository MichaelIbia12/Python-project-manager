import subprocess
import os
from simple_chalk import red, green
usr = os.getenv("USER")
current_directory = os.getcwd()
server_addr = "127.10.0.1"


def send_folder(PORT, File):
    if not os.path.exists(f"/home/{usr}/{File}"):
        print(red(f"Error: Directory /home/{usr}/{File} does not exist."))
        return

    try:
        os.chdir(f"/home/{usr}/{File}")
        command = ["python3", "-m", "http.server",
                   str(PORT), "--bind", server_addr]
        server_process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(green(f"File changed to {File}"))
        print(green(f"Sending at {server_addr}:{PORT} \n"))
        print(
            green(f"Run wget -r {server_addr}:{PORT} in the recieving computer"))
        progress = input("Press q to quit- ")
        if progress == "q":
            server_process.terminate()
            os.chdir(current_directory)
            print(green(f"File changed back to {current_directory}"))
            return
        print(green(server_process.stdout.read()))
        print(red(server_process.stderr.read()))
    # OS error hndling and PermisionError not working
    except OSError as e:
        print(f"Port {PORT} already in use")
    except PermissionError:
        print(3333)
    except Exception as e:
        print(red(f"An error occurred: {e}"))
    except KeyboardInterrupt as e:
        print(red(f"key interupted as {e}"))

