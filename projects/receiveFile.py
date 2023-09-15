import subprocess
from simple_chalk import green, red
import os


def recieve_files(File, Server_Addr, PORT):
    os.chdir(File)
    command = ["wget", "-r", f"{Server_Addr}:{PORT}"]
    server_process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(green(server_process.stderr.read()))
    progress = input("Press q to quit- ")
    if progress == "q":
        return
