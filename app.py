import streamlit as st
import json
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# Configuração da página
st.set_page_config(
    page_title="Corretor ENEM - Análise com IA",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para design profissional
st.markdown("""
<style>
    /* Importar fonte Google */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Variáveis CSS */
    :root {
        --primary-color: #2E86AB;
        --secondary-color: #A23B72;
        --accent-color: #F18F01;
        --success-color: #28A745;
        --warning-color: #FFC107;
        --danger-color: #DC3545;
        --light-bg: #F8F9FA;
        --card-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    /* Reset básico */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header principal */
    .main-header {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: var(--card-shadow);
    }
    
    .main-header h1 {
        margin: 0;
        font-weight: 600;
        font-size: 2.5rem;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-size: 1.1rem;
    }
    
    /* Cards de competência */
    .competencia-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: var(--card-shadow);
        margin-bottom: 1rem;
        border-left: 4px solid var(--primary-color);
        transition: transform 0.2s ease;
    }
    
    .competencia-card:hover {
        transform: translateY(-2px);
    }
    
    .competencia-titulo {
        font-weight: 600;
        color: var(--primary-color);
        margin-bottom: 0.5rem;
    }
    
    .competencia-score {
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .score-excelente { color: var(--success-color); }
    .score-bom { color: var(--warning-color); }
    .score-ruim { color: var(--danger-color); }
    
    /* Área de texto personalizada */
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #E1E5E9;
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        line-height: 1.6;
    }
    
    .stTextArea textarea:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 2px rgba(46, 134, 171, 0.1);
    }
    
    /* Botões personalizados */
    .stButton button {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 2rem;
        font-weight: 500;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(46, 134, 171, 0.3);
    }
    
    /* Métricas */
    .metric-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: var(--card-shadow);
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    
    .metric-label {
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    /* Feedback área */
    .feedback-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: var(--card-shadow);
        border-left: 4px solid var(--accent-color);
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown("""
<div class="main-header">
    <h1>📝 Corretor ENEM com IA</h1>
    <p>Análise profissional de redações com Inteligência Artificial</p>
</div>
""", unsafe_allow_html=True)

# Sidebar com informações
with st.sidebar:
    st.markdown("### 👩‍🏫 Painel do Professor")
    st.markdown("---")
    
    st.markdown("**🤖 Sobre a IA:**")
    st.info("✨ Google Gemini 2.0 Flash")
    st.info("🎯 Especialista em ENEM")
    st.info("💬 Feedback pedagógico detalhado")
    
    st.markdown("---")
    st.markdown("**📋 Critérios Avaliados:**")
    st.markdown("""
    - **C1**: Domínio da escrita formal (0-200)
    - **C2**: Compreensão do tema (0-200)  
    - **C3**: Argumentação (0-200)
    - **C4**: Coesão e coerência (0-200)
    - **C5**: Proposta de intervenção (0-200)
    """)
    
    st.markdown("---")
    st.markdown("**🎓 Vantagens:**")
    st.markdown("""
    - 🔍 Análise detalhada por competência
    - 📝 Feedback específico e pedagógico
    - 💡 Sugestões de melhoria
    - ⚡ Resultado em poucos segundos
    - 🎯 Baseado nos critérios oficiais
    """)
    
    st.markdown("---")
    st.markdown("**ℹ️ Como usar:**")
    st.markdown("""
    1. Configure sua chave API do Google
    2. Cole a redação na caixa de texto
    3. Clique em "Analisar Redação"
    4. Receba feedback detalhado
    """)

# Área principal de análise
st.markdown("### ✨ Análise de Redação com Inteligência Artificial")
st.markdown("*Correção detalhada seguindo os critérios oficiais do ENEM*")

col1, col2 = st.columns([2, 1])

with col1:
    txt = st.text_area(
        "📝 Cole a redação do aluno aqui:",
        height=400,
        placeholder="Digite ou cole a redação completa aqui...\n\nA IA Gemini analisará:\n• Cada competência individualmente\n• Fornecerá feedback específico\n• Sugerirá melhorias concretas\n• Destacará pontos fortes\n\nPara melhores resultados, inclua a redação completa com introdução, desenvolvimento e conclusão."
    )

with col2:
    st.markdown("### 🎯 Status da Análise")
    
    # Verificar configuração
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        st.success("✅ API Gemini configurada")
    else:
        st.error("❌ Configure GEMINI_API_KEY no .env")
        st.info("💡 Copie .env.example para .env e adicione sua chave")
    
    st.markdown("---")
    st.markdown("**📊 O que você receberá:**")
    st.markdown("""
    - 🔢 Nota de 0-1000 pontos
    - 📈 Avaliação por competência
    - ✅ Pontos fortes identificados
    - 📝 Áreas para melhorar
    - 💬 Feedback pedagógico completo
    """)

# Botão de análise
if st.button("✨ Analisar Redação com IA", use_container_width=True):
    if not txt.strip():
        st.error("❌ Por favor, insira uma redação para análise.")
    elif not api_key:
        st.error("❌ Configure a GEMINI_API_KEY no arquivo .env")
        st.info("💡 Veja as instruções na barra lateral")
    else:
        with st.spinner("🤖 IA analisando redação detalhadamente... (3-5 segundos)"):
            try:
                # Criar cliente Gemini
                client = genai.Client(api_key=api_key)
                
                # Schema para resposta estruturada
                response_schema = {
                    'type': 'object',
                    'properties': {
                        'c1': {'type': 'integer', 'description': 'Competência 1: Domínio da escrita formal (0-200)'},
                        'c2': {'type': 'integer', 'description': 'Competência 2: Compreensão do tema (0-200)'},
                        'c3': {'type': 'integer', 'description': 'Competência 3: Argumentação (0-200)'},
                        'c4': {'type': 'integer', 'description': 'Competência 4: Coesão/coerência (0-200)'},
                        'c5': {'type': 'integer', 'description': 'Competência 5: Proposta de intervenção (0-200)'},
                        'nota_total': {'type': 'integer', 'description': 'Soma das 5 competências'},
                        'feedback': {'type': 'string', 'description': 'Feedback detalhado e pedagógico'},
                        'pontos_fortes': {'type': 'string', 'description': 'Principais pontos fortes da redação'},
                        'areas_melhoria': {'type': 'string', 'description': 'Áreas que precisam de melhoria'}
                    },
                    'required': ['c1', 'c2', 'c3', 'c4', 'c5', 'nota_total', 'feedback', 'pontos_fortes', 'areas_melhoria']
                }
                
                # Prompt otimizado para análise pedagógica
                system_prompt = """Você é um especialista em correção de redações do ENEM com 20 anos de experiência pedagógica. 

Avalie a redação seguindo rigorosamente os critérios oficiais do ENEM:

• C1 - Domínio da escrita formal (0-200): ortografia, gramática, sintaxe, adequação ao registro
• C2 - Compreensão do tema (0-200): desenvolvimento adequado do tema proposto  
• C3 - Argumentação (0-200): seleção, organização e interpretação de argumentos
• C4 - Coesão e coerência (0-200): articulação entre parágrafos e sequenciação de ideias
• C5 - Proposta de intervenção (0-200): proposta detalhada, viável e respeitando direitos humanos

Forneça feedback pedagógico construtivo e específico. Seja preciso nas notas e didático nas explicações.
Destaque tanto pontos fortes quanto áreas específicas para melhoria."""

                user_prompt = f"Avalie esta redação do ENEM seguindo os critérios oficiais:\n\n{txt}"
                
                # Chamada para Gemini
                response = client.models.generate_content(
                    model='gemini-2.0-flash-001',
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        response_mime_type='application/json',
                        response_schema=response_schema,
                        temperature=0.1  # Mais determinístico para avaliações consistentes
                    )
                )
                
                # Parse da resposta
                data = json.loads(response.text)
                
                # Exibir resultados
                st.markdown("---")
                st.markdown("### 🎯 Análise Concluída!")
                
                # Métricas principais
                col_nota1, col_nota2, col_nota3 = st.columns(3)
                
                with col_nota1:
                    nota_total = data['nota_total']
                    cor_classe = "excelente" if nota_total >= 800 else "bom" if nota_total >= 600 else "ruim"
                    st.markdown(f"""
                    <div class="metric-container">
                        <div class="metric-value score-{cor_classe}">{nota_total}</div>
                        <div class="metric-label">Nota Final</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_nota2:
                    media = nota_total / 5
                    st.markdown(f"""
                    <div class="metric-container">
                        <div class="metric-value">{media:.1f}</div>
                        <div class="metric-label">Média por Competência</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_nota3:
                    percentual = (nota_total / 1000) * 100
                    st.markdown(f"""
                    <div class="metric-container">
                        <div class="metric-value">{percentual:.1f}%</div>
                        <div class="metric-label">Aproveitamento</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Competências detalhadas
                st.markdown("### 📊 Detalhamento por Competência")
                
                competencias = [
                    ("C1", "Domínio da Escrita Formal", data['c1'], "📝"),
                    ("C2", "Compreensão do Tema", data['c2'], "🎯"),
                    ("C3", "Argumentação", data['c3'], "💭"),
                    ("C4", "Coesão e Coerência", data['c4'], "🔗"),
                    ("C5", "Proposta de Intervenção", data['c5'], "💡")
                ]
                
                col_comp1, col_comp2 = st.columns(2)
                
                for i, (codigo, nome, valor, emoji) in enumerate(competencias):
                    col = col_comp1 if i % 2 == 0 else col_comp2
                    
                    with col:
                        cor_score = "excelente" if valor >= 160 else "bom" if valor >= 120 else "ruim"
                        progresso = (valor / 200) * 100
                        
                        st.markdown(f"""
                        <div class="competencia-card">
                            <div class="competencia-titulo">{emoji} {codigo} - {nome}</div>
                            <div class="competencia-score score-{cor_score}">{valor}/200</div>
                            <div style="background: #e0e0e0; border-radius: 10px; height: 8px; margin: 10px 0;">
                                <div style="background: {'#28A745' if valor >= 160 else '#FFC107' if valor >= 120 else '#DC3545'}; 
                                            width: {progresso}%; height: 100%; border-radius: 10px;"></div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Feedback pedagógico
                col_feedback1, col_feedback2 = st.columns(2)
                
                with col_feedback1:
                    st.markdown(f"""
                    <div class="feedback-card">
                        <h4>✅ Pontos Fortes</h4>
                        <p>{data.get('pontos_fortes', 'Análise em andamento...')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_feedback2:
                    st.markdown(f"""
                    <div class="feedback-card" style="border-left-color: var(--warning-color);">
                        <h4>📈 Áreas de Melhoria</h4>
                        <p>{data.get('areas_melhoria', 'Análise em andamento...')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Feedback geral
                st.markdown("### 💬 Feedback Pedagógico Detalhado")
                st.markdown(f"""
                <div class="feedback-card">
                    {data['feedback']}
                </div>
                """, unsafe_allow_html=True)
                
                # Dados técnicos (expandível)
                with st.expander("🔍 Ver dados técnicos da análise"):
                    st.json(data)
                    
            except Exception as e:
                st.error(f"❌ Erro na análise: {str(e)}")
                if "API_KEY" in str(e):
                    st.info("💡 Verifique se a GEMINI_API_KEY está configurada corretamente")
                else:
                    st.info("💡 Tente novamente em alguns segundos")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6c757d; padding: 2rem 0;">
    <p>📚 Corretor ENEM com IA - Ferramenta pedagógica para professores</p>
    <p>🤖 Powered by Google Gemini 2.0 | ✨ Análise profissional e detalhada</p>
</div>
""", unsafe_allow_html=True)
