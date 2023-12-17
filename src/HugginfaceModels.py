from llama_index.llms import HuggingFaceInferenceAPI # Module to leverage Open source LLMs
from llama_index.embeddings import LangchainEmbedding #For Embeddings
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from env import HF_TOKEN
print("Importing Huggingface Models...")
llm = HuggingFaceInferenceAPI(
    model_name="HuggingFaceH4/zephyr-7b-beta", token=HF_TOKEN
)


#Embedding Model
embed_model = LangchainEmbedding(
  HuggingFaceInferenceAPIEmbeddings(api_key=HF_TOKEN,model_name="thenlper/gte-large")
)
print("Huggingface model import complete")