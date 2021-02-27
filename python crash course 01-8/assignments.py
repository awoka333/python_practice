# 8-9
"""
def show_messages(messages):
	for message in messages:
		print(message)

messages = ["おはよう", "こんにちは", "こんばんは"]
show_messages(messages)
"""

# 8-10
def send_messages(messages):
	for message in messages:
		print(message)
		sent_messages.append(message)
sent_messages = []
messages = ["おはよう", "こんにちは", "こんばんは"]

# send_messages(messages)
# for sent_message in sent_messages:
# 	print(sent_message)

# 8-11
send_messages(messages)
print("-----message-----")
for message in messages:
	print(message)
print("-----sent_message-----")
for sent_message in sent_messages:
	print(sent_message)