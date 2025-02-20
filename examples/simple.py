import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent

load_dotenv()

# Initialize the model
llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)

# task = 'Find the founders of browser-use, open the first link of the result in another tab, then get back to the search tab and visit https://pomofocus.io/'

# task = 'Visit https://www.amazon.com.br/, visit the first product link you find, extract the first review, then extract the product price and then get back to the previous page'

# task = 'Visit https://pomofocus.io/, create a task with name "Task de Drica" using the keyboard shortcut (pressing n to create a task and Ctrl + enter to save)'

# task = 'Visit https://pomofocus.io/, find the "Premium Features" section and after this find and click the "START" button to begin the timer. After this, visit https://www.amazon.com.br and then go back to the previous page'

# task = 'Visit https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select and select Opel option'

task = 'Visit https://www.trivago.com.br/ and change the country in the dropdown at the footer to Argentina'

agent = Agent(task=task, llm=llm)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())
