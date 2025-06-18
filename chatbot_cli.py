#from langchain_ollama import OllamaLLM
from langchain_community.llms import Ollama

model=Ollama(model="gemma2:2b")

while 1:
	user_input=input("Talk to Gemma: ")

	if user_input.lower()=='exit' or user_input.lower()=='q':
		break
	

	result=model.invoke(user_input)


	print(result)