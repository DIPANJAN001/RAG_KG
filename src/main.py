from query import query_engine
from meassage_template import message_template

if __name__=='main':
    response = query_engine.query(message_template)
    print(response.response.split("<|assistant|>")[-1].strip())