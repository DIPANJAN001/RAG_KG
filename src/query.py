from knowledge_graph import index
query = "What is MicroGrid"
print("Running Query...")
query_engine = index.as_query_engine(include_text=True,
                                     response_mode ="tree_summarize",
                                     embedding_mode="hybrid",
                                     similarity_top_k=5,)
print("Query engine complete")