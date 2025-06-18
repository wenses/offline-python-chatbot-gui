import os, sys

if sys.platform=='win32':
    os.system('color b')
    os.system('cls')
    print("INSTALLING...REQUIERD STUFF :)")
    os.system('color b')
    os.system('ollama pull gemma2:2b')
    os.system('pip install langchain langchain-ollama ollama')
elif sys.platform=='linux':
    os.system('clear')
    print(f'\033[32m installing stuff')
    os.system('sudo apt update')
    os.system('ollama pull gemma2:2b')
    os.system('pip3 install langchain langachain-ollama ollama')
    print(f'\033[31m Recomended: Use a virtual environment e.g python3 -m venv myvenv')
