import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO) #Provide use full information
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) # Give messages that helps in monitoring
from llama_index import (SimpleDirectoryReader,# To Read Unstructured data
                         LLMPredictor,#Generating Predictions using LLM
                         ServiceContext,#Supplies Contextual Data 
                         KnowledgeGraphIndex)#Both Construction and manipulation of of KG
#
from llama_index.graph_stores import SimpleGraphStore #For storing Graph data
from llama_index.storage.storage_context import StorageContext
from llama_index.llms import HuggingFaceInferenceAPI # Module to leverage Open source LLMs
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from llama_index.embeddings import LangchainEmbedding #For Embeddings
from pyvis.network import Network
HF_TOKEN = "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"
#   LLMs
llm = HuggingFaceInferenceAPI(
    model_name="HuggingFaceH4/zephyr-7b-beta", token=HF_TOKEN
)


#Embedding Model
embed_model = LangchainEmbedding(
  HuggingFaceInferenceAPIEmbeddings(api_key=HF_TOKEN,model_name="thenlper/gte-large")
)


#Load the data
reader = SimpleDirectoryReader(
    input_files=["Final_conference_paper.pdf"]
)
docs = reader.load_data()
print(f"Loaded {len(docs)} docs")
#setup the service context

service_context = ServiceContext.from_defaults(
    chunk_size=256,
    llm=llm,
    embed_model=embed_model
)

#Storage
graph_store = SimpleGraphStore()
storage_context = StorageContext.from_defaults(graph_store=graph_store)

# #Building Knowledge Graph
#Construct the Knowlege Graph Index
index = KnowledgeGraphIndex.from_documents( documents=docs,
                                           max_triplets_per_chunk=1,
                                           service_context=service_context,
                                           storage_context=storage_context,
                                          include_embeddings=True)

#Query the Knowledge Graph
query = "What is MicroGrid?"
query_engine = index.as_query_engine(include_text=True,
                                     response_mode ="tree_summarize",
                                     embedding_mode="hybrid",
                                     similarity_top_k=5,)
#
message_template =f"""<|system|>Please check if the following pieces of context has any mention of the  keywords provided in the Question.If not then don't know the answer, just say that you don't know.Stop there.Please donot try to make up an answer.</s>
<|user|>
Question: {query}
Helpful Answer:
</s>"""
#
response = query_engine.query(message_template)
#
print(response.response.split("<|assistant|>")[-1].strip())