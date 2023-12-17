
def query_engine_(kg_index):
    query_engine = kg_index.as_query_engine(include_text=True,
                                        response_mode ="tree_summarize",
                                        embedding_mode="hybrid",
                                        similarity_top_k=5,)
    return query_engine
