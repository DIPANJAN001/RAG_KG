from service_context import set_Service_contex
from storage_context import set_Storage_context
from knowledge_graph import build_kg
from meassage_template import meassage_template_
from HugginfaceModels import Call_HuggingFace_Model
from reader import load_text
from query import query_engine_
from genarate_response import generate_respnose
from visualize_kg import plot_kg
if __name__=="__main__":
    query = "Who leads hyuga clan?"
    print("START")
    print("Loading HuggingFace Models...")
    llm_,embed_model_=Call_HuggingFace_Model()
    print("HuggingFace Models loaded")
    print("-------------------------------------------------")
    print("Loading text...")
    docs=load_text()
    print("Text loaded")
    print("-------------------------------------------------")
    print("Setting up service context...")
    service_context=set_Service_contex(llm_,embed_model_)
    print("service context setting complete")
    print("-------------------------------------------------")
    print("Setting up storage context...")
    storage_context=set_Storage_context()
    print("storage context setting complete")
    print("-------------------------------------------------")
    print("Building knowledge graph...")
    kg=build_kg(docs,service_context,storage_context)
    print("Knowledge graph building complegte")
    print("-------------------------------------------------")
    print("Ploting knowledge graph")
    plot_kg(kg)
    print("Ploting complete")
    print("-------------------------------------------------")
    print("Generating answer")
    que_engine=query_engine_(kg)
    mes_tem=meassage_template_(query)
    response=generate_respnose(que_engine,mes_tem)
    print(response.response.split("<|assistant|>")[-1].strip())
    print("Answer generated")
    print("-------------------------------------------------")
    print("END")



    


