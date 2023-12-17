from llama_index import SimpleDirectoryReader
print("Started data loading...")
reader = SimpleDirectoryReader(
    input_files=["Final_conference_paper.pdf"]
)
docs = reader.load_data()
print("Data loading complete")