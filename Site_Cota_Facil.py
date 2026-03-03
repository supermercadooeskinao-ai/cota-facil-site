# --- SEÇÃO: COMO FUNCIONA ---
st.divider()
st.header("🎯 Três passos para otimizar suas compras")
col_step1, col_step2, col_step3 = st.columns(3)

with col_step1:
    st.write("### 1. Ativação")
    st.write("Após a assinatura, seu ID é liberado na hora.")

with col_step2:
    st.write("### 2. Input")
    st.write("Insira os dados da cotação no painel intuitivo.")

with col_step3:
    st.write("### 3. Economia")
    st.write("Visualize o melhor fornecedor e feche o pedido.")

# --- SEÇÃO: FAQ ---
st.divider()
st.header("💬 Perguntas Comuns")
with st.expander("O sistema funciona em qualquer dispositivo?"):
    st.write("Sim! O COTA FÁCIL é 100% online e otimizado para navegadores mobile e desktop.")

with st.expander("Como funciona o bloqueio de acesso?"):
    st.write("Sua licença é válida por 30 dias. O sistema verifica automaticamente o status na Planilha Mestra para garantir sua segurança.")

# --- FOOTER ---
st.divider()
st.markdown("<center>© 2026 COTA FÁCIL - Todos os direitos reservados</center>", unsafe_allow_html=True)

