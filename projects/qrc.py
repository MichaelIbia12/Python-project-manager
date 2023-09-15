import qrcode
from simple_chalk import red, green
import os
usr = os.getenv("USER")
try:
    os.mkdir(f"/home/{usr}/Pictures/Qrcodes")
    print("Created directory")
except FileExistsError:
    pass


def qrc_maker(url=str):
    if url == " ":
        print(red("Statement not present"))
        url_input = input("#Url/text- ")
        if url_input == "":
            print("Url/text not found")
            url_input = input("#Url/text- ")
        else:
            code = qrcode.make(url_input)
            code.save(f'/home/{usr}/Pictures/Qrcodes/{url_input.removeprefix("http://")}.png')
            print(green(f'Saved to /Pictures/Qrcodes/ as {url_input.removeprefix("http://")}.png'))
    else:
        code = qrcode.make(url)
        code.save(f'/home/{usr}/Pictures/Qrcodes/{url.removeprefix("http://")}.png')
        print(green(f'Saved to /Pictures/Qrcodes/ as {url.removeprefix("http://")}.png'))

qrc_maker("https://www.test.com//gogg/hiior₦@ef")