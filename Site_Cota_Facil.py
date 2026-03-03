import streamlit as st

st.set_page_config(page_title="COTA FÁCIL - Gestão de Compras", page_icon="🛒")

# Correção do parâmetro para evitar o TypeError
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #25D366;
        color: white;
        height: 3em;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True) # O segredo está aqui!

st.title("🛒 COTA FÁCIL")
st.subheader("Sua cotação inteligente em poucos segundos.")

st.write("Automatize a análise de preços de fornecedores e pare de perder margem de lucro.")

# Link do WhatsApp (Ajuste o número)
seu_numero = "5511999999999"
msg = "Olá! Vi o site do Cota Fácil e quero minha licença."
link_wa = f"https://wa.me/{seu_numero}?text={msg.replace(' ', '%20')}"

# Botão que abre em nova aba
st.markdown(f'''
    <a href="{link_wa}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold;">
            🚀 QUERO MINHA LICENÇA AGORA
        </div>
    </a>
    ''', unsafe_allow_html=True)
