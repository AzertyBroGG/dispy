import dispy

client = dispy.Client()

@client.event_listener
def message_create(m):
    print(m['author']['username'], 'said,')
    print(m['content'])

@client.event_listener
def message_delete(m):
    print('a message has been deleted')

client.login("NzYzMDMwNjQ5NTk4MjQ2OTQz.X3xxqw.IJfOHf6PpPy6Wb5QbiCGbnhcoAE")