from .errors import *
from .constants import *

import websocket
import threading
import random
import json
import time
import os

class TestObject:
    def __init__(self, **stuff):
        self.__dict__.update(stuff)

class Client:
    """Represents your discord client. This is the main class to interact with Discord API.
    
    Attributes
    ----------

    """
    def __init__(self):
        self.event_listeners = {}
        self._ws = websocket.WebSocket()

    def _send_request(self, request):
        self._ws.send(json.dumps(request))

    def _recieve_response(self):
        response = self._ws.recv()
        if response:
            return json.loads(response)

    def _send_heartbeat(self, interval):
        while True:
            time.sleep(interval)
            json_ = {
                "op": 1,
                "d": "null"
            }
            self._send_request(json_)

    def dispatch_event(self, event):
        listeners = self.event_listeners.get(event['t'])
        if listeners:
            for listener in listeners:
                print(event['d'])
                return listener(event['d'])


    def add_event_listener(self, event, action):
        """Adds an event listener for an event.

        event : str
            The event name to listen to.

        action : function
            The function to call upon the event.
        """
        if not event.upper() in GATEWAY_EVENTS:
            raise BadArgument('Unknown event name was passed.')

        if self.event_listeners.get(event.upper()) == None:
            self.event_listeners[event.upper()] = []

        self.event_listeners[event.upper()].append(action)

    def event_listener(self, func):
        """A decorator interface to register event listeners.

        This is equivalent of doing ``Client.add_event_listener(func)``.

        Example:
            ```
            @client.event_listener
            def message_create(message):
                print(message.content)
            ```
            The function name is considered the event name.
        """
        def predicate(func):
            event = func.__name__.upper()
            return self.add_event_listener(event, func)

        return predicate(func)
            

    def login(self, token: str):
        """Logins to the discord. This is a blocking function and will not return until client crashes or logs out
        for whatever reason.

        Parameters:

            token : str
              The bot's token to login with.
        """
        self._ws.connect('wss://gateway.discord.gg/bot/?v=7&encoding=json')
        event = self._recieve_response()
        heartbeat_interval = event['d']['heartbeat_interval'] / 1000

        threading._start_new_thread(self._send_heartbeat, (heartbeat_interval,))

        payload = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": os.name,
                    "$browser": "dispy",
                    "$device": "dispy"
                }
            }
        }
        self._send_request(payload)
        while True:
            event = self._recieve_response()
            print(event['t'])
            try:
                if event['t'] in GATEWAY_EVENTS:
                    self.dispatch_event(event['t'], )
            except:
                ...
