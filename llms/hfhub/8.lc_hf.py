from langchain_huggingface import HuggingFaceEndpoint
import keys

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B",
    task="text-generation",
    huggingfacehub_api_token= keys.HUGGINGFACE_KEY)
 

print(llm.invoke("What is the capital of Austria?"))
