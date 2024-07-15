from g4f.client import Client

client = Client()
model = "gpt-3.5-turbo"

messages_1 = [{"role": "user", "content": "pretend you are a human having a conversation, try to have smalltalk"}]  # initialize conversation history
messages_2 = [{"role": "user", "content": "pretend you are a human having a conversation, try to have smalltalk"}]  # initialize conversation history

while True:
    response = client.chat.completions.create(
        model=model,
        messages=messages_1,
    )
    result = response.choices[0].message
    print("1:"+result.content)
    messages_1.append({"role": "assistant", "content": result.content})
    messages_2.append({"role": "user", "content": result.content})
    input("Press enter to continue")

    response = client.chat.completions.create(
        model=model,
        messages=messages_2,
    )

    result = response.choices[0].message
    print("2:"+result.content)
    messages_2.append({"role": "assistant", "content": result.content})
    messages_1.append({"role": "user", "content": result.content})
    input("Press enter to continue")
