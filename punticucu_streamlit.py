import streamlit as st

# ✅ Dati persistenti
if 'giocatori' not in st.session_state:
    st.session_state.giocatori = []

st.title("🍕 Segnapunti CUCÙ")

# Colonna sinistra: Aggiungi
col1, col2 = st.columns(2)

with col1:
    st.subheader("➕ Aggiungi giocatore")
    nome = st.text_input("Nome:", key="nome_input")
    vite = st.number_input("Vite:", min_value=0, value=3, step=1, key="vite_input")
    
    if st.button("Aggiungi giocatore"):
        if nome:
            st.session_state.giocatori.append({"nome": nome, "vite": vite})
            st.success(f"✅ {nome} aggiunto!")
            st.rerun()  # Ricarica pagina

# Elenco giocatori
st.subheader("👥 GIOCATORI")
if not st.session_state.giocatori:
    st.info("👆 Aggiungi il primo giocatore!")
else:
    for i, g in enumerate(st.session_state.giocatori):
        stato = "💀 **MORTO**" if g["vite"] == 0 else f"**Vivo** ({g['vite']} vite)"
        st.write(f"{i+1}. **{g['nome']}** - {stato}")
    
    # Modifica specifica
    st.subheader("⚙️ Modifica")
    scelta = st.selectbox("Scegli giocatore:", [""] + [g["nome"] for g in st.session_state.giocatori])
    
    if scelta:
        idx = next(i for i, g in enumerate(st.session_state.giocatori) if g["nome"] == scelta)
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button(f"➖ Togli vita a {scelta}", key=f"togli_{idx}"):
                if st.session_state.giocatori[idx]["vite"] > 0:
                    st.session_state.giocatori[idx]["vite"] -= 1
                    st.rerun()
        
        with col_b:
            if st.button(f"❤️ Aggiungi vita a {scelta}", key=f"add_{idx}"):
                st.session_state.giocatori[idx]["vite"] += 1
                st.rerun()

# Debug
with st.expander("🐛 Debug"):
    st.write("Dati:", st.session_state.giocatori)
