from langchain import PromptTemplate, LLMChain
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI

PROMPT_TEMPLATE = """
You are a catholic priest. A penitent has come to you for confession. 
Be nice and moral, and a bit sarcasstic and funny.

Penitent confessed: {sins}. Last confession was: {last_confession}
"""


def get_confession(
    params: dict,
    callback_handler: StreamlitCallbackHandler,
) -> str:
    summary_prompt_template = PromptTemplate(
        input_variables=["sins", "last_confession"],
        template=PROMPT_TEMPLATE,
    )

    llm = ChatOpenAI(
        temperature=0.0,
        model_name="gpt-4o",
        streaming=True,
        callbacks=[callback_handler],
    )

    chain = LLMChain(llm=llm, prompt=summary_prompt_template, verbose=True)

    result = chain.run(
        sins=params["sins"],
        last_confession=params["last_confession"]
    )
    return result
