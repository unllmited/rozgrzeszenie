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

st.title('Automatyczna Spowiedź')

st.divider()

with st.form("confession_form"):
    st.subheader("Wstęp")
    st.write("Niech będzie pochwalony Jezus Chrystus. Na wieki wieków. Amen")
    st.write("W imię Ojca i Syna, i Ducha Świętego. Amen.")

    st.subheader("Ostatnia spowiedź")
    last_confession = st.date_input("Ostatni raz u spowiedzi świętej byłem:")

    st.subheader("Grzechy")
    sins = st.text_area("Obraziłem Pana Boga następującymi grzechami:")

    submit_button = st.form_submit_button("Wyślij spowiedź")

    archetypes = ["good cop", "bad cop"]

    if submit_button:
        c1, c2 = st.columns(2)
        with c1:
            callback_handler1 = StreamHandler(container=st.empty())
            good = get_confession(
                params={
                    "last_confession": last_confession,
                    "sins": sins,
                    "archetype": archetypes[0],
                },
                callback_handler=callback_handler1,
            )
        with c2:
            callback_handler2 = StreamHandler(container=st.empty())
            bad = get_confession(
                params={
                    "last_confession": last_confession,
                    "sins": sins,
                    "archetype": archetypes[1],
                },
                callback_handler=callback_handler2,
            )
