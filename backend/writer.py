from langchain import PromptTemplate, LLMChain
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI

PROMPT_TEMPLATE = """
You are a catholic priest. A penitent has come to you for confession. 
{archetype_description}

Penitent confessed: {sins}
Last confession was: {last_confession}

Bądź kreatywny w pokucie, nie dawaj samego ojcze nasz i zdrowaś Mario.

Pokuta powinna polegać na karze, która przesyca grzech i skupia się na jego jeszcze większym popełnianiu,
tak żeby spowiadany miał dosyć tego co uczynił, czyli np. 
* jeśli ktoś zjadł czekoladę w Wielki Post, to niech przez tydzień je tylko czekoladę, aż do pożygania
* jeżeli ktoś uprawiał seks pozamałżeński, to niech przez miesiąc uprawia seks 5 razy dziennie
* jeżeli zapaliłeś fajkę to masz ich wypalić 10 na raz, żeby aż ci to zbrzydło

Odpowiedz w języku polskim.

Zacznij od słów: "Mój drogi synu, za twoje grzechy..."
"""


def get_confession(
    params: dict,
    callback_handler: StreamlitCallbackHandler,
) -> str:
    summary_prompt_template = PromptTemplate(
        input_variables=["sins", "last_confession", "archetype_description"],
        template=PROMPT_TEMPLATE,
    )

    llm = ChatOpenAI(
        temperature=0.1,
        model_name="gpt-4o",
        streaming=True,
        callbacks=[callback_handler],
    )

    chain = LLMChain(llm=llm, prompt=summary_prompt_template, verbose=True)

    archetype_description = ("You are a good cop type of individual."
                             "You try to be moral, ethical, and honest in your actions."
                             "You are a good listener and try to understand the other person's perspective."
                             "You are empathetic and compassionate."
                             "You are a good communicator and try to resolve conflicts peacefully."
                             "Be like a good father"
                             "") if params["archetype"] == "good cop" else ("You are a bad cop."
                                                                            "You are tough, sarcastic and intimidating."
                                                                            "You are not afraid to take risks and "
                                                                            "make tough decisions."
                                                                            "You are not afraid to confront people "
                                                                            "and hold them accountable."
                                                                            "Be like a bad cop")

    result = chain.run(
        sins=params["sins"],
        last_confession=params["last_confession"],
        archetype_description=archetype_description,
    )
    return result
