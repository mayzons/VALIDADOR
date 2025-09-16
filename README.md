# Validador de Estrutura de Arquivos - Python

Este projeto é uma automação simples em Python que valida se todos os arquivos de uma pasta possuem a **mesma estrutura de colunas** que um arquivo modelo. Ideal para quem trabalha com
relatórios CSV, TXT ou Excel de fornecedores, parceiros ou equipes internas e quer economizar tempo evitando conferências manuais.

---

## **Como funciona**

1. Você fornece um **arquivo modelo** (CSV, TXT ou Excel) com a estrutura correta.  

---
2. O script percorre todos os arquivos da pasta e verifica:  
   - Se possuem as mesmas colunas que o arquivo modelo.  
   - Quais arquivos estão inconsistentes.  
   - Quais arquivos não puderam ser lidos (erros).  

---

## **Benefícios**

- Economiza horas de conferência manual.  
- Reduz erros humanos.  
- Padroniza os dados antes de consolidar ou criar dashboards.  
- Pode ser adaptado facilmente para diferentes pastas ou estruturas.

---

## **Requisitos**

- Python 3.8+  
- Bibliotecas:
```bash
pip install RE
