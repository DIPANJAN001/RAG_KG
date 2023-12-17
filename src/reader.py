from llama_index import SimpleDirectoryReader
def load_text():
    reader = SimpleDirectoryReader(
        input_files=["Naruto.pdf"]
    )
    docs = reader.load_data()
    return docs
