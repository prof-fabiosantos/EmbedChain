import os
from embedchain import App
os.environ["OPENAI_API_KEY"] = ''

wikipedia_bot = App()

# Embed Online Resources

wikipedia_bot.add("https://en.wikipedia.org/wiki/Donald_Trump")
wikipedia_bot.add("https://en.wikipedia.org/wiki/Barack_Obama")

while True:
    question = input("Faça uma pergunta?.\n >>")

    if question == 'quit':
        break

    response = wikipedia_bot.query(question)
    print(f"\n{response}\n")
