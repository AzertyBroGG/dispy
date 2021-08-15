import dispy

client = dispy.Client()

@client.event_listener
def ready():
    print('hey listen, im ready')

@client.event_listener
def message_create(m):
    print(m['author']['username'], 'said,')
    print(m['content'])

@client.event_listener
def message_delete(m):
    print('a message has been deleted')

@client.event_listener
def message_update(m):
    print('a message has been edited')

client.login("NzYzMDMwNjQ5NTk4MjQ2OTQz.X3xxqw.DfXKUIpXdEfeNWvjy3Ve54vF1eY")