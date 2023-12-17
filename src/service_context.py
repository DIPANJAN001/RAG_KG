from llama_index import ServiceContext
from HugginfaceModels import embed_model,llm
print("Setting up Service context...")
service_context = ServiceContext.from_defaults(
    chunk_size=256,
    llm=llm,
    embed_model=embed_model
)
print("Service context setting complete")