from collections import defaultdict
import random
import time
import datetime
personal_data = {
    "name": "MARSES",
    "age": datetime.datetime.now().year - 2023
}

data_refrence = {
    "greeting" :[
        ["hi", "hello", "whatsup", "hey", "Hi there!","Hey, how's it going?", "Good evening!","Good morning!","Good night!","Nice to see you!"],
        ["hello", "hi", "Hello! I'm doing well, thank you. How about you?", "Hi! I'm good, thanks. How are you doing?", "Hey! Everything's great. How about you?", "Good day!"]
        ],
    "CHY" : [
        ["how are you", "how is your day going", "how is your day","How are you?", "How's it going?", "Are you doing okay?", "Is everything alright with you?"],
        ["fine thank you", "I'm doing well, thank you", "I'm good, thanks for asking", "I'm alright, thanks", "Everything's fine with me"]
        ],
    "current location": [        
        ["where am i", "where am i located"],
        ["nigeria"]
        ],
    "personnal_name": [
        ["what is your name","What's your name?","May I know your name, please?", "Could you introduce yourself?", "What do people call you?", "Who am I speaking with?"],
        [f"My name is {personal_data['name']}", f"I go by {personal_data['name']}", f"You can call me {personal_data['name']}", f"I'm {personal_data['name']}, nice to meet you."]
    ]
}
data_score = []

def score_calculator(score:list):
    bundles = defaultdict(list)
    for key, value in score:
        bundles[key].append(value)
    average  = {key: sum(values) for key, values in bundles.items()}
    result = dict(sorted(average.items(), key=lambda item: item[1], reverse=True))
    return result

def response_generator(data:dict):
    d = []
    for i in data:
        d.append(i)
    main_response_type = d[0]
    print(data_refrence[main_response_type][1][int(random.randrange(-1,len(data_refrence[main_response_type][1])))])

def response(msg:str):
    data = msg.split()
    for str in data:
        for d in data_refrence:
            score = 0
            for i in data_refrence[d][0]:
                if str in i:
                    score += 1
            data_score.append([d,score])
    average_score = score_calculator(data_score)
    response_generator(average_score)
while True:
    try:
        msg = input(":- ")
        print('thinking')
        time.sleep(2)
        response(msg)
        data_score.clear()
    except TypeError as err:
        print(f"typeErr {err}")
    except IndexError as err:
        print(f"{err}")