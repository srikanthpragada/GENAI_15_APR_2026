from langchain_ollama import OllamaLLM
 
model = OllamaLLM(model="gemma3")
print(model.invoke("Which is the capital of Spain? Just give name."))
#print(model.invoke("Who won IPL 2025"))
