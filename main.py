import websocket
import json
import threading
import time
import random

def send_json_request(ws, request):
    ws.send(json.dumps(request))

def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    print("Heartbeat begin")
    while True:
        time.sleep(interval)
        json_ = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, request)
        print('Heartbeat sent')

ws = websocket.WebSocket()
ws.connect('wss://gateway.discord.gg/bot/?v=7&encoding=json')
event = recieve_json_response(ws)
heartbeat_interval = event['d']['heartbeat_interval'] * random.random()

threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

token = "NzYzMDMwNjQ5NTk4MjQ2OTQz.X3xxqw.IJfOHf6PpPy6Wb5QbiCGbnhcoAE"
payload = {
    "op": 2,
    "d": {
        "token": token,
        "properties": {
            "$os": "Windows",
            "$browser": "Chrome",
            "$device": "PC"
        }
    }
}
send_json_request(ws, payload)

while True:
    event = recieve_json_response(ws)
    try:
        if event['t'] == 'MESSAGE_CREATE':
            print(event['d'])
        quit()
    except:
        ...