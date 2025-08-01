# 📝 Corretor ENEM com IA

Sistema simples e eficiente para correção de redações do ENEM usando Google Gemini AI.

![Demo](https://img.shields.io/badge/Status-Funcionando-brightgreen)
![Licença](https://img.shields.io/badge/Licença-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)

## ⚡ Características

- 🤖 **IA Avançada**: Google Gemini 2.0 Flash
- 📊 **Análise Completa**: 5 competências oficiais do ENEM
- 💬 **Feedback Pedagógico**: Sugestões específicas e construtivas
- ⚡ **Rápido**: Resultado em 3-5 segundos
- 🎯 **Preciso**: Seguindo critérios oficiais do ENEM
- 🎨 **Interface Moderna**: Design profissional e intuitivo

## 🚀 Demonstração

O sistema fornece:
- **Nota final** de 0-1000 pontos
- **Avaliação detalhada** por competência (C1 a C5)
- **Pontos fortes** identificados automaticamente
- **Áreas de melhoria** específicas
- **Feedback pedagógico** completo e construtivo

## 📦 Instalação Rápida

### 1. Clone o repositório
```bash
git clone https://github.com/the-go-getter11/corretor-enem-ia.git
cd corretor-enem-ia
```

### 2. Instale dependências
```bash
pip install -r requirements.txt
```

### 3. Configure a API key
```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite .env e adicione sua GEMINI_API_KEY
# GEMINI_API_KEY=sua_chave_aqui
```

### 4. Execute o sistema
```bash
streamlit run app.py
```

## 🔑 Obter Chave API do Google

1. Acesse [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada
5. Cole no arquivo `.env`

**A API do Gemini é gratuita** com limites generosos para uso educacional.

## 📋 Competências Avaliadas

O sistema analisa as **5 competências oficiais do ENEM**:

- **C1**: Domínio da escrita formal (0-200 pontos)
- **C2**: Compreensão do tema (0-200 pontos)  
- **C3**: Argumentação (0-200 pontos)
- **C4**: Coesão e coerência (0-200 pontos)
- **C5**: Proposta de intervenção (0-200 pontos)

**Nota final**: Soma das 5 competências (0-1000 pontos)

## 🎓 Para Professores

### Vantagens Pedagógicas:
- ✅ **Feedback Específico**: Orientações detalhadas para cada competência
- 📈 **Identificação de Padrões**: Pontos fortes e fracos automaticamente
- ⏰ **Economia de Tempo**: Análise em segundos vs. horas manuais
- 📊 **Consistência**: Critérios padronizados sempre aplicados
- 💡 **Sugestões Práticas**: Orientações concretas de melhoria

### Como Usar em Sala:
1. **Triagem Inicial**: Identifique redações que precisam de atenção
2. **Feedback Rápido**: Forneça retorno imediato aos alunos
3. **Orientação Pedagógica**: Use as sugestões para planos de aula
4. **Acompanhamento**: Compare evoluções ao longo do tempo

## 💡 Exemplo de Uso

```
1. Copie uma redação completa
2. Cole na interface do sistema
3. Clique em "Analisar Redação com IA"
4. Receba análise detalhada em 3-5 segundos
5. Use o feedback para orientação pedagógica
```

## 🔧 Estrutura do Projeto

```
corretor-enem-ia/
├── app.py              # Interface Streamlit principal
├── requirements.txt    # Dependências Python
├── .env.example       # Exemplo de configuração
├── .env              # Suas configurações (não versionado)
├── .gitignore        # Arquivos ignorados pelo Git
└── README.md         # Documentação (este arquivo)
```

## 🛠️ Tecnologias Utilizadas

- **Frontend**: Streamlit (interface web moderna)
- **IA**: Google Gemini 2.0 Flash (análise de texto)
- **Linguagem**: Python 3.8+
- **Deployment**: Local (pode ser facilmente hospedado)

## 📈 Roadmap

- [ ] **Deploy online** para acesso direto via navegador
- [ ] **Histórico de análises** para acompanhar progresso
- [ ] **Exportação de relatórios** em PDF
- [ ] **Análise em lote** para múltiplas redações
- [ ] **Banco de dados** para armazenar resultados
- [ ] **API REST** para integração com outros sistemas

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/the-go-getter11/corretor-enem-ia/issues)
- **Documentação**: Este README
- **Contato**: Abra uma issue para dúvidas técnicas

## 🙏 Agradecimentos

- **Google Gemini**: Pela API de IA gratuita e eficiente
- **Streamlit**: Pela plataforma de desenvolvimento rápido
- **Comunidade Python**: Pelas bibliotecas excelentes

---

⭐ **Se este projeto te ajudou, deixe uma estrela no GitHub!**

🎓 **Desenvolvido para apoiar educadores na correção pedagógica de redações do ENEM**
