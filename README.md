# dispy
A simple (and experimental) API wrapper around Discord API.

## Precaution
This library is ultimately an experimental library. This is not meant to be used in production enivornment at all. We don't provide any assurance of how stable this library is. If you are looking for something to use in production enivornment, Please use [discord.py](https://github.com/Rapptz/discord.py)

## Features
- Easy to Use & Object oriented
- Extension to create message commands easily

## Examples
```py
import dispy

client = dispy.Client()

@client.on('message_create')
def message_create(message: dispy.DiscordMessage):
  if message.author.is_me():
    return
  
  message.channel.create_message(f"{message.author.name} said, {message.content}")

client.login('your-bot-token')
```

## Contributing
All pull requests, bug fixes are welcomed. Please see the [Contribution Guide](CONTRIBUTING.MD)


