from llama_index import ServiceContext
def set_Service_contex(llm,embed_model):
    service_context = ServiceContext.from_defaults(
        chunk_size=256,
        llm=llm,
        embed_model=embed_model
    )
    return service_context
