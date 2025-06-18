from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma2:2b")
print(llm.invoke("The meaning of life is"))