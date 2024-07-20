import random

import streamlit as st
from dotenv import load_dotenv

from backend.utils.streamlit import StreamHandler
from backend.writer import get_confession

load_dotenv()

st.set_page_config(
    page_title="Rozgrzeszenie Online",
    page_icon=":cross:",
    layout="wide",
    menu_items={
        "Get Help": "mailto:pawel+rozgrzeszenie@cejrowski.biz",
        "Report a bug": "mailto:pawel+rozgrzeszenie@cejrowski.biz",
    },
)

st.title('Twoja spowiedź online')

with st.form("confession_form"):
    st.write("Niech będzie pochwalony.")
    last_confession = st.date_input("Ostatni raz u spowiedzi świętej byłem:")

    sins = st.text_area("Obraziłem Pana Boga następującymi grzechami:")

    submit_button = st.form_submit_button("Za te i za wszystkie inne moje grzechy proszę o rozgrzeszenie.")

    archetypes = ["good cop", "bad cop"]

    if submit_button:
        chosen_archetype = archetypes[random.randint(0, 1)]
        st.toast("Spowiada ksiądz skurwiel 😈" if chosen_archetype == "bad cop" else "Spowiada Cię anielska dusza 👼")
        callback_handler = StreamHandler(container=st.empty())
        get_confession(
            params={
                "last_confession": last_confession,
                "sins": sins,
                "archetype": chosen_archetype,
            },
            callback_handler=callback_handler,
        )

with st.expander(""):
    st.text(
        "Ta strona nie ma charakteru oficjalnej spowiedzi. Jej intencją nie jest również obrażanie uczuć religijnych."
        )
