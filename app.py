import streamlit as st
from dotenv import load_dotenv

from backend.utils.streamlit import StreamHandler
from backend.writer import get_confession

load_dotenv()

st.set_page_config(
    page_title="Rozgrzeszenie Online",
    page_icon=":memo:",
    layout="wide",
    menu_items={
        "Get Help": "mailto:pawel+rozgrzeszenie@cejrowski.biz",
        "Report a bug": "mailto:pawel+rozgrzeszenie@cejrowski.biz",
    },
)
st.title('Automatyczna Spowiedź')

st.divider()

with st.form("confession_form"):
    st.write("Niech będzie pochwalony Jezus Chrystus. Na wieki wieków. Amen")
    st.write("W imię Ojca i Syna, i Ducha Świętego. Amen.")
    last_confession = st.text_input("Ostatni raz u spowiedzi świętej byłem:")
    sins = st.text_area("Obraziłem Pana Boga następującymi grzechami:")
    submit_button = st.form_submit_button("Wyślij Spowiedź")

    callback_handler = StreamHandler(container=st.empty())

    params = {
        "last_confession": last_confession,
        "sins": sins,
    }
    if submit_button:
        get_confession(
            params,
            callback_handler,
        )
