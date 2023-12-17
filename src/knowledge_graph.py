from llama_index import KnowledgeGraphIndex


def build_kg(doc,ser_con,stor_con):
    try:
       
        index = KnowledgeGraphIndex.from_documents( documents=doc,
                                                max_triplets_per_chunk=2,
                                                service_context=ser_con,
                                                storage_context=stor_con,
                                                include_embeddings=True)
        
    except :
        print("Rate Limit reached")
    return index
    

