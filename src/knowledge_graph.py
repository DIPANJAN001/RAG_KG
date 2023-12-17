from llama_index import KnowledgeGraphIndex
from service_context import service_context
from storage_context import storage_context
from reader import docs

print("Building knowledge Graph...")
index = KnowledgeGraphIndex.from_documents( documents=docs,
                                           max_triplets_per_chunk=1,
                                           service_context=service_context,
                                           storage_context=storage_context,
                                          include_embeddings=True)
print("Knowldge Graph building complete")
