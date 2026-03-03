import streamlit as st

st.set_page_config(page_title="COTA FÁCIL - Gestão de Compras", page_icon="🛒")

# Estilo para o botão de WhatsApp ficar destacado
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #25D366;
        color: white;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_url=True)

st.title("🛒 COTA FÁCIL")
st.subheader("Pare de perder dinheiro em cotações manuais.")

# Texto Persuasivo
st.write("A ferramenta que automatiza sua análise de preços e garante a melhor compra em segundos.")

with st.expander("Veja os benefícios"):
    st.write("* **Análise de Menor Preço:** Identificação instantânea.")
    st.write("* **Cálculo de Quantidade:** Valor total automático (Preço x Qtd).")
    st.write("* **Acesso Seguro:** Controle por ID de licença.")

# Link do WhatsApp com mensagem personalizada
# Substitua o '55...' pelo seu número com DDD
msg = "Olá! Vi o site do Cota Fácil e quero minha licença agora."
link_wa = f"https://wa.me/5511999999999?text={msg.replace(' ', '%20')}"

if st.button("🚀 QUERO MINHA LICENÇA AGORA"):
    st.markdown(f'<meta http-equiv="refresh" content="0;URL={link_wa}">', unsafe_url=True)