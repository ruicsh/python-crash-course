messages = ["foobar", "barbaz", "bazbuz"]


def send_messages(to_send):
    sent = []
    while to_send:
        message = to_send.pop()
        sent.append(message)
    return sent


def show_messages(messages):
    for message in messages:
        print(message)


sent = send_messages(messages[:])
show_messages(sent)
show_messages(messages)
