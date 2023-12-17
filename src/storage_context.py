from llama_index import KnowledgeGraphIndex
from llama_index.graph_stores import SimpleGraphStore
from llama_index.storage.storage_context import StorageContext
def set_Storage_context():
    graph_store = SimpleGraphStore()
    storage_context = StorageContext.from_defaults(graph_store=graph_store)
    return storage_context