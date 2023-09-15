import sys
from simple_chalk import red, chalk, green
import logging
from projects import qrc
import pyfiglet
import os
from projects import sendfile
import subprocess
from projects import receiveFile
from projects import fileOrganizer
usr = os.getenv("USER")

text_render = pyfiglet.Figlet(font='banner3-D')
Commands = [
    # ("gpt", " A chat_gpt extension"),
    ("--help", "Gives a list of all comands"),
    ("qrcode <url/text>", "This makes an custom qrcode"),
    ("sendfile <file>", "Sends file throught a python server"),
    ("recievefile <file>", "Recieves file from the Python server"),
    ("organise", "clean, Organise and sort files")
]


def info_breakdown(string) -> list:
    return string.split(" ")


def cHelp():
    for items in Commands:
        print(items[0]+" - ", items[1])


def info_engine(raw_str):
    [action, argument, *statement] = info_breakdown(raw_str)
    if len(statement) <= 0:
        statement.append(" ")
    if action != "msl":
        print(red(f"{action} is not supported"))
    elif action == 'clear':
        subprocess.Popen("clear", stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, text=True)
    else:
        match argument:
            case "--help":
                print(chalk.green("initiating Help"))
                cHelp()
            case "qrcode":
                print(chalk.green("initiating Qrcode"))
                qrc.qrc_maker(statement[0])
            case "sendfile":
                print(green(f"Uploading {statement}"))
                sendfile.send_folder(9000, statement[0])
            case "recieveFile":
                print(green(f"Downloading file to {statement}"))
                receiveFile.recieve_files(
                    "/home/marshall/Documents", "127.10.0.1",  9000)
            case "organise":
                print(green('organizing files'))
                fileOrganizer.Organise()
            case _:
                print('Command not found')


def run_brp():
    print(text_render.renderText(f"Welcome {usr}"))
    while True:
        try:
            prompt_data = input("###- ")
            info_engine(prompt_data)
        except SyntaxError as se:
            print('Err- ' + str(se))
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected")
        except ValueError as err:
            print('Err- ' + str(err))


if __name__ == "__main__":
    run_brp()
