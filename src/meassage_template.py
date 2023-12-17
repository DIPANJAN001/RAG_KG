def meassage_template_(que):
    message_template =f"""<|system|>Please check if the following pieces of context has any mention of the  keywords provided in the Question.If not then don't know the answer, just say that you don't know.Stop there.Please donot try to make up an answer.</s>
    <|user|>
    Question: {que}
    Helpful Answer:
    </s>"""
    return message_template
#