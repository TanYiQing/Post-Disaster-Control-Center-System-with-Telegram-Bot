import re
from datetime import datetime

import psycopg2


def get_data(message):
    ic_number = message.split("@")[0]
    phone_number = message.split("@")[1]
    try:
        conn = psycopg2.connect("postgres://mrfknbsicvtqjo:40cb1909b8ae034538bb96ca0c1ec827d86753ba50548ada7c97fda44f162738@ec2-3-213-76-170.compute-1.amazonaws.com:5432/dhecvtd68dsm3/dfvpahtam3chdu", sslmode='require')
        cursor = conn.cursor()
        # cursor.execute("SELECT ic_no,hp_no,name FROM \"App_Victim_victim\" WHERE ic_no = '{}' AND hp_no = '{}'".format(ic_number, phone_number))# some sql statement
        conn.commit()
        result = cursor.fetchall()
        ic = [i[0] for i in result]
        hp = [i[1] for i in result]
        name = [i[2] for i in result]
        age = str(calculate_age(ic[0]))
        bot_response = "Maklumat Anda:\nKad Pengenalan: " + str(ic[0]) + "\nNombor Telefon: " + str(hp[0]) + "\nNama: " + str(name[0]) + "\nUmur: " + age
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        bot_response = "Maaf, saya tidak menemui data anda... Sila semak semula dengan maklumat yang sah"

    return bot_response


def calculate_age(ic):
    ic_year = str(ic[:2])
    cur_year = datetime.now().year
    now = str(cur_year)[:2]
    if int(now + ic_year) <= cur_year:
        return int(cur_year) - (int(now + "00") + int(ic_year))
    else:
        return int(cur_year) - (int(now + "00") - 100 + int(ic_year))


def process_message(message, response_array, response):
    # Split the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scoring System
    score = 0
    for word in list_message:
        if word in response_array:
            score += 1

    print(score, response)
    return [score, response]


def get_response(message):
    # custom response
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'], 'Hello!'),
        process_message(message, ['bye', 'goodbye'], 'Bye Bye, jumpa lagi!'),
    ]

    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response
    if winning_response == 0:
        bot_response = 'Maaf, saya tidak faham maksud anda.'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response

# Test your system
# get_response('Hello')