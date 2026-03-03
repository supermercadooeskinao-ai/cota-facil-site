import streamlit as st

# 1. Configuração Inicial da Página
st.set_page_config(
    page_title="COTA FÁCIL - Gestão Inteligente de Compras",
    page_icon="🛒",
    layout="wide"
)

# 2. Estilização CSS de Alto Impacto
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
        min-height: 220px;
    }
    .price-card {
        background-color: #262730;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #25D366;
        text-align: center;
    }
    .price-tag {
        font-size: 36px;
        font-weight: bold;
        color: #25D366;
    }
    .step-box {
        background-color: #161b22;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #30363d;
    }
    .highlight { color: #25D366; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Seção Principal (Hero Section)
col1, col2 = st.columns([1.5, 1])

with col1:
    st.title("🛒 COTA FÁCIL")
    st.header("Domine suas compras e proteja sua margem de lucro.")
    st.write("""
        Pare de perder tempo com planilhas confusas e erros manuais. 
        O **COTA FÁCIL** automatiza a análise de fornecedores para que você 
        garanta sempre o menor preço com um clique.
    """)
    
    # Link do WhatsApp (Lembre-se de colocar seu número real abaixo)
    seu_numero = "5511999999999" 
    msg = "Olá! Vi o site do Cota Fácil e quero minha licença agora."
    link_wa = f"https://wa.me/{seu_numero}?text={msg.replace(' ', '%20')}"

    st.markdown(f'''
        <a href="{link_wa}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 20px; text-align: center; border-radius: 12px; font-weight: bold; font-size: 22px; box-shadow: 0px 4px 15px rgba(37, 211, 102, 0.3);">
                🚀 QUERO MINHA LICENÇA AGORA
            </div>
        </a>
        ''', unsafe_allow_html=True)

with col2:
    # Representação visual do App
    st.image("https://cdn-icons-png.flaticon.com/512/3225/3225194.png", width=250)

st.divider()

# 4. Diferenciais do Produto
st.subheader("Por que o COTA FÁCIL é indispensável?")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""<div class="card">
        <h3>⚡ Análise Instantânea</h3>
        <p>Compare múltiplos fornecedores simultaneamente. O sistema identifica o menor preço unitário e total automaticamente.</p>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown("""<div class="card">
        <h3>📊 Precisão Matemática</h3>
        <p>Cálculos automáticos de <b>Preço x Quantidade</b>. Elimine erros humanos que geram prejuízos no final do mês.</p>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown("""<div class="card">
        <h3>🌐 Acesso Cloud</h3>
        <p>100% online. Acesse do celular ou computador sem instalar nada. Seus dados protegidos por ID exclusivo.</p>
    </div>""", unsafe_allow_html=True)

st.divider()

# 5. Seção de Investimento (Preço)
st.header("💎 Investimento")
col_p1, col_p2 = st.columns([1, 1.5])

with col_p1:
    st.markdown(f"""
        <div class="price-card">
            <h4>Plano Profissional</h4>
            <div class="price-tag">R$ 49,90<span style="font-size: 16px; color: white;"> /mês</span></div>
            <p style="margin-top: 10px;">Ativação imediata via WhatsApp</p>
            <hr style="border-color: #444;">
            <ul style="text-align: left; font-size: 14px;">
                <li>✅ Comparativo ilimitado</li>
                <li>✅ Suporte prioritário</li>
                <li>✅ Atualizações de sistema</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col_p2:
    st.write("### O sistema que se paga sozinho.")
    st.write("""
        Imagine economizar apenas 2% em cada compra por causa de uma análise bem feita. 
        Em um mês, o **COTA FÁCIL** não terá custado nada — ele terá gerado lucro para você.
        
        Nossa plataforma utiliza a mesma tecnologia de processamento de dados que grandes empresas usam, 
        mas de uma forma simples e acessível para o seu negócio.
    """)

st.divider()

# 6. FAQ - Perguntas Frequentes
st.header("💬 Perguntas Frequentes")
with st.expander("Como recebo meu ID de acesso?"):
    st.write("Assim que o pagamento for confirmado, enviamos seu ID único que libera o sistema instantaneamente na nossa Planilha Mestra.")

with st.expander("O que acontece se eu não renovar?"):
    st.write("O sistema verifica o status da sua licença a cada 30 dias. Caso não haja renovação, o acesso é bloqueado automaticamente até a próxima ativação.")

with st.expander("É seguro colocar meus dados de fornecedores?"):
    st.write("Sim. Cada usuário opera em uma instância isolada e os dados inseridos são processados apenas para gerar o seu relatório de compra.")

# 7. Rodapé
st.divider()
st.markdown("<center>© 2026 COTA FÁCIL | Desenvolvido para transformar compras em economia.</center>", unsafe_allow_html=True)
