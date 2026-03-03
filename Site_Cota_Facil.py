import streamlit as st

# 1. Configuração Inicial da Página
st.set_page_config(
    page_title="COTA FÁCIL - Gestão Inteligente de Compras",
    page_icon="🛒",
    layout="wide"
)

# 2. Estilização CSS Profissional
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMarkdown { color: #ffffff; }
    .card {
        background-color: #1e2130;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #25D366;
        margin-bottom: 20px;
        min-height: 200px;
    }
    .step-box {
        background-color: #262730;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #444;
    }
    .highlight { color: #25D366; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho (Hero Section)
col1, col2 = st.columns([2, 1])

with col1:
    st.title("🛒 COTA FÁCIL")
    st.header("Transforme cotações complexas em decisões lucrativas.")
    st.write("""
        Pare de perder tempo e dinheiro com planilhas manuais. 
        O **COTA FÁCIL** é a solução definitiva para quem busca agilidade e 
        precisão na hora de negociar com fornecedores.
    """)
    
    # Link do WhatsApp Personalizado
    seu_numero = "5511999999999" # COLOQUE SEU NÚMERO AQUI
    msg = "Olá! Vi o site do Cota Fácil e quero minha licença agora."
    link_wa = f"https://wa.me/{seu_numero}?text={msg.replace(' ', '%20')}"

    st.markdown(f'''
        <a href="{link_wa}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 18px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 20px;">
                🚀 QUERO MINHA LICENÇA AGORA
            </div>
        </a>
        ''', unsafe_allow_html=True)

with col2:
    # Espaço para Imagem Ilustrativa do App
    st.image("https://cdn-icons-png.flaticon.com/512/3225/3225194.png", width=200)

st.divider()

# 4. Seção de Diferenciais (Cards)
st.subheader("Por que o COTA FÁCIL é a escolha certa?")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""<div class="card">
        <h3>⚡ Análise Instantânea</h3>
        <p>Identifique o menor preço entre múltiplos fornecedores em segundos. O sistema destaca a melhor opção automaticamente.</p>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown("""<div class="card">
        <h3>📊 Precisão Total</h3>
        <p>Cálculo automático de <b>Preço x Quantidade</b>. Chega de erros manuais que destroem sua margem de lucro.</p>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown("""<div class="card">
        <h3>🔐 Segurança SaaS</h3>
        <p>Acesso exclusivo via ID de licença. Seus dados e cotações protegidos em uma infraestrutura moderna.</p>
    </div>""", unsafe_allow_html=True)

st.divider()

# 5. Seção "Como Funciona"
st.header("🎯 Como funciona o sistema?")
s1, s2, s3 = st.columns(3)

with s1:
    st.markdown('<div class="step-box"><h4>1. Ativação</h4><p>Após a assinatura, seu ID é liberado via Planilha Mestra.</p></div>', unsafe_allow_html=True)

with s2:
    st.markdown('<div class="step-box"><h4>2. Preenchimento</h4><p>Insira os valores dos fornecedores e as quantidades desejadas.</p></div>', unsafe_allow_html=True)

with s3:
    st.markdown('<div class="step-box"><h4>3. Resultado</h4><p>O app gera o comparativo final e você fecha a melhor compra.</p></div>', unsafe_allow_html=True)

st.divider()

# 6. FAQ - Perguntas Frequentes
st.header("💬 Dúvidas Frequentes")

with st.expander("O COTA FÁCIL funciona no celular?"):
    st.write("Sim! Desenvolvido em Python/Streamlit, o sistema é 100% responsivo e funciona em qualquer navegador.")

with st.expander("Como é feito o pagamento e liberação?"):
    st.write("O modelo é de assinatura mensal. Após o pagamento, ativamos seu acesso imediatamente no servidor.")

with st.expander("Meus dados estão seguros?"):
    st.write("Sim. Cada usuário possui um ambiente de acesso protegido por ID único, garantindo privacidade total.")

# 7. Rodapé Final
st.divider()
st.markdown("<center>© 2026 COTA FÁCIL | Desenvolvido para eficiência máxima.</center>", unsafe_allow_html=True)
