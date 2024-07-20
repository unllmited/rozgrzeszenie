from datetime import date

from langchain import PromptTemplate, LLMChain
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI

PROMPT_TEMPLATE = """
Jesteś katolickim księdzem. Penitent przyszedł do ciebie do spowiedzi. 
{archetype_description}

Penitent wyznał: {sins}
Ostatnia spowiedź miała miejsce {last_confession} dni temu.

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
    prompt = PromptTemplate(
        input_variables=["sins", "last_confession", "archetype_description"],
        template=PROMPT_TEMPLATE,
    )

    llm = ChatOpenAI(
        temperature=0.3,
        model_name="gpt-4o",
        streaming=True,
        callbacks=[callback_handler],
    )

    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

    archetype_description = \
        ("""Jesteś dobrym gliną.
            Próbujesz być moralny, etyczny i uczciwy w swoich działaniach.
            Jesteś dobrym słuchaczem i starasz się zrozumieć perspektywę drugiej osoby.
            Jesteś empatyczny i współczujący.
            Jesteś dobrym komunikatorem i próbujesz rozwiązywać konflikty pokojowo.
            Bądź jak dobry ojciec."""
         ) if params["archetype"] == "good cop" \
            else \
            ("""Jesteś złym gliną.
            Jesteś twardy, sarkastyczny i zastraszający.
            Nie boisz się podejmować ryzyka i podejmować trudnych decyzji.
            Nie boisz się konfrontować ludzi i pociągać ich do odpowiedzialności.
            Bądź jak zły glina.""")

    result = chain.run(
        sins=params["sins"],
        last_confession=date.today() - params["last_confession"],
        archetype_description=archetype_description,
    )
    return result
