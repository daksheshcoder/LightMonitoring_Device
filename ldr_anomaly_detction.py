import conf, json, time, math, statistics,requests
from boltiot import Bolt
#function to calculate the Z-score
def compute_bounds(history_data,frame_size,factor):
    #code to check if it collected enough data to caluculate z-score.
    if len(history_data)<frame_size :
        return None
    if len(history_data)>frame_size :
        del history_data[0:len(history_data)-frame_size]
    #code to caluculate the mean.
    Mn=statistics.mean(history_data)
    Variance=0
    for data in history_data :
        Variance += math.pow((data-Mn),2)
    #code to caluculate the z-score.
    Zn = factor * math.sqrt(Variance / frame_size)
    High_bound = history_data[frame_size-1]+Zn
    Low_bound = history_data[frame_size-1]-Zn
    return [High_bound,Low_bound]
#connecting to the telegram
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        #print("This is the Telegram URL")
        #print(url)
        #print("This is the Telegram response")
        #print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False
history_data=[]
#code to find the z-score and send telegram message if found anomaly
while True:
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    if data['success'] != 1:
        print("There was an error while retriving the data.")
        print("This is the error:"+data['value'])
        time.sleep(10)
        continue

    print ("This is the value "+data['value'])
    sensor_value=0
    try:
        sensor_value = int(data['value'])
    except e:
        print("There was an error while parsing the response: ",e)
        continue

    bound = compute_bounds(history_data,conf.FRAME_SIZE,conf.MUL_FACTOR)
    if not bound:
        required_data_count=conf.FRAME_SIZE-len(history_data)
        print("Not enough data to compute Z-score. Need ",required_data_count," more data points")
        history_data.append(int(data['value']))
        time.sleep(10)
        continue

    try:
        if sensor_value > bound[0] :
            print ("The light level increased suddenly. Sending an SMS.")
            message = "Someone has turned on the lights"
            telegram_status= send_telegram_message(message)
            print("This is the Telegram status:",telegram_status)
        elif sensor_value < bound[1]:
            print ("The light level decreased suddenly. Sending an SMS.")
            message = "Someone has turned off the lights"
            telegram_status= send_telegram_message(message)
            print("This is the Telegram status:",telegram_status)
        history_data.append(sensor_value)
    except Exception as e:
        print ("Error",e)
    time.sleep(10)