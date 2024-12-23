import streamlit as st

#Side Bar Direktory
Dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
Nabung = st.Page("./fitur/nabung.py", title="Nabung")
penarikan = st.Page("./fitur/penarikan.py", title="penarikan")



pg = st.navigation(
    {
        "Menu Utama": [Dashboard],
        "Transaksi": [Nabung, penarikan],
    }
)

# menjalankan Navigasi
pg.run()

if 'jumlah' not in st.session_state:
    st.session_state['jumlah'] = []
