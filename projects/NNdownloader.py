from playwright.sync_api import sync_playwright
import requests
import json
import playwright
import os
import time
from simple_chalk import red, green
import _asyncio
import random
json_file = open("projects/data/NN.json", "a")
usr = os.getenv("USER")
series_url = "https://www.thenetnaija.net/videos/series/"
movie_url = "https://www.thenetnaija.net/videos/movies/"

data = {
    "mv": {},
    "sr": {}
}


def Netupdate(estimated_code: int):
    try:
        for i in range(estimated_code, 50):
            req_series = requests.get(f"{series_url}{i}-xxxx").content
            req_movies = requests.get(f"{movie_url}{i}-xxxx").content
            req_sr_add, req_mv_add = req_series.splitlines(), req_movies.splitlines()
            link_Tag_sr, link_Tag_mv = req_sr_add[8].split(), req_mv_add[8].split()
            link_sr, link_mv = link_Tag_sr[2].decode(), link_Tag_mv[2].decode()

            if link_sr.startswith("href") or link_mv.startswith("href"):
                l_st, l_mv = link_sr.replace('"', " ").replace("href=", " "), link_mv.replace('"', " ").replace("href=", " ")
                if l_st.find("/series/") != -1:
                    ln = l_st.replace("/", " ").split()
                    code, *name = ln[4].split("-")
                    data["sr"][code] = {"name": " ".join(name)}
                if l_mv.find("/movie/") != -1:
                    ln = l_mv.replace("/", " ").split()
                    code, *name = ln[4].split("-")
                    data["mv"][code] = {"name": " ".join(name)}

    except ConnectionResetError:
        print("Server went down")
    json.dump(data, json_file, indent=4)

def movie_downloader(index):
    rq = requests.get(f"{movie_url}{index}-xxxx").content
    split_rq = rq.splitlines()
    link_tag = split_rq[8].split()
    link_str = link_tag[2].decode()
    if link_str.startswith("href"):
        link = link_str.replace('"', "").replace("href=", " ")
        print(link)
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            page.goto(link)
            button = page.locator("#dbo-dl-1")
            button.evaluate('(element) => element.click()')

            page.wait_for_load_state("networkidle", timeout=120000)
                
            with page.expect_download() as d_file:
                download = page.locator(".download")
                download.evaluate('(element) => element.click()')
            f_url = d_file.value.url
            file_ele = page.locator("h1")
            file_link = file_ele.inner_html()
            print(d_file.__sizeof__())
            if  os.path.exists(f"/home/{usr}/Downloads/{file_link}"):
                print(red(f"{file_link} already exists"))
                f_conf = input("Do you want to still download it y/n :-")
                if f_conf.lower() == "y":
                    count = 0
                    if  os.path.exists(f"/home/{usr}/Downloads/{count}{file_link}"):
                        count+= 1
                        d_file.value.save_as(f"/home/{usr}/Downloads/{count}{file_link}")
                    else:
                        d_file.value.save_as(f"/home/{usr}/Downloads/{count}{file_link}")
                elif f_conf.lower() == "n":
                        print(green("File not downloaded: file already exits"))
                        browser.close()
                else:
                    print("invalid input")
                    browser.close()
            else:
                d_file.value.save_as(f"/home/{usr}/Downloads/{file_link}")
            while not os.path.exists(f"/home/{usr}/Downloads/{file_link}"):
                time.sleep(2)

            if os.path.exists(f"/home/{usr}/Downloads/{file_link}"):
                print(green(f"{file_link} is downloaded"))
                browser.close()
            else:
                print(green(f"{file_link} is not downloaded"))
                f_conf = input("Should I try again: y/n")
                if f_conf.lower() == "y":
                    download(index, 0)
                elif f_conf.lower() == "n":
                    browser.close()
                else:
                    print("invalid input")
                    browser.close()
                    
def series_downloader(index, season_number, loop):
    rq = requests.get(f"{series_url}{index}-xxxx").content
    split_rq = rq.splitlines()
    link_tag = split_rq[8].split()
    link_str = link_tag[2].decode()
    if link_str.startswith("href"):
        link = link_str.replace('"', "").replace("href=", " ")
        print(link)
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            page.goto(link)
            button = page.locator("#dbo-dl-1")
            button.evaluate('(element) => element.click()')

            page.wait_for_load_state("networkidle", timeout=120000)

def download(code, type):
    try:
        if type == "movies" or int(type) == 0:
            movie_downloader(code)
        else:
            print(f"{code} is invalid")
        if type == "series" or int(type) == 1:
           season_question = input("Season? - ")
           episode_question = input("Episode? -")
           question_series = input("Do you want to download the whole season Y/n-")
           if question_series.lower() == "y":
                if int(season_question):
                    series_downloader(code, season_question, episode_question, question_series.lower())
                else:
                    series_downloader(code, season_question, episode_question, question_series.lower())
           elif question_series.lower() == "n":
                if int(season_question):
                    series_downloader(code, season_question, episode_question)
                else:
                    series_downloader(code, season_question, episode_question)
                            

    except requests.exceptions.ConnectionError:
        print(red("Please connect to an internet service"))
    except playwright._impl._api_types.TimeoutError or _asyncio.execptions.InvalidStateError:
        print(red(f"Sorry network issues: time out for {code} after 12s"))

download(3820, 0)
