import streamlit as st

st.set_page_config(page_title="COTA FÁCIL - Gestão de Compras", page_icon="🛒", layout="wide")

# CSS Customizado para um visual moderno
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMarkdown { color: #ffffff; }
    .card {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #25D366;
        margin-bottom: 20px;
    }
    .price-tag {
        font-size: 24px;
        font-weight: bold;
        color: #25D366;
    }
    </style>
    """, unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([2, 1])

with col1:
    st.title("🛒 COTA FÁCIL")
    st.header("Domine suas compras e proteja sua margem de lucro.")
    st.write("A ferramenta inteligente para quem não tem tempo a perder com planilhas confusas.")

with col2:
    # Espaço para uma imagem ou logo
    st.image("https://cdn-icons-png.flaticon.com/512/3225/3225194.png", width=150)

st.divider()

# Seção de Benefícios em Colunas (Cards)
st.subheader("Por que o COTA FÁCIL é indispensável?")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""<div class="card">
        <h3>⚡ Rapidez</h3>
        <p>Análise instantânea do menor preço entre múltiplos fornecedores.</p>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown("""<div class="card">
        <h3>📊 Precisão</h3>
        <p>Cálculo automático de Preço x Quantidade sem erros manuais.</p>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown("""<div class="card">
        <h3>🔐 Segurança</h3>
        <p>Acesso exclusivo via ID para garantir a privacidade dos seus dados.</p>
    </div>""", unsafe_allow_html=True)

st.divider()

# Chamada para Ação Final
st.markdown("<center><h2>Pronto para profissionalizar suas cotações?</h2></center>", unsafe_allow_html=True)

# Link do WhatsApp
link_wa = "https://wa.me/5511999999999?text=Quero%20minha%20licença%20do%20Cota%20Facil"

st.markdown(f'''
    <a href="{link_wa}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #25D366; color: white; padding: 20px; text-align: center; border-radius: 50px; font-weight: bold; font-size: 22px; transition: 0.3s;">
            🚀 QUERO MINHA LICENÇA AGORA
        </div>
    </a>
    ''', unsafe_allow_html=True)

st.caption("<center>Ativação imediata após confirmação de pagamento.</center>", unsafe_allow_html=True)
