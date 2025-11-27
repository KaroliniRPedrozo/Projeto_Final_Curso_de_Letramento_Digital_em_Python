

# 💰 Controle de Despesas Pessoais - Projeto Final

Este repositório contém o projeto final desenvolvido para o **Curso de Letramento Digital em Python**.

O objetivo foi criar uma aplicação de linha de comando (CLI) que permite registrar, categorizar e analisar despesas pessoais, aplicando conceitos fundamentais de programação e análise de dados.

## 📋 Funcionalidades

O sistema atende a todos os requisitos propostos no enunciado:

  * **Adicionar Despesas:** Registro com descrição, categoria, valor e data (com preenchimento automático da data atual caso vazio).
  * **Listagem Completa:** Visualização de todas as despesas ordenadas cronologicamente.
  * **Análise de Gastos:**
      * Cálculo do total gasto por categoria.
      * Identificação automática da categoria com maior gasto.
      * **Visualização Gráfica:** Gráfico de barras simples feito com caracteres de texto (Feature de Criatividade).
  * **Relatório Mensal:** Filtro de despesas por mês e ano específicos.
  * **Exportação de Dados:** Salva todos os registros em um arquivo `.csv` compatível com Excel/Planilhas.
  * **Gerador de Dados de Teste:** Funcionalidade extra para preencher o sistema com dados fictícios automaticamente para fins de teste.

## 🛠️ Tecnologias e Conceitos Aplicados

Conforme solicitado na ementa do curso:

  * **Estruturas de Dados:** Uso de **Listas** e **Dicionários** para armazenar os registros em memória.
  * **Funções:** Modularização do código para manter a organização e a legibilidade.
  * **Manipulação de Datas:** Utilização da biblioteca `datetime` para operações e formatação de datas.
  * **Tratamento de Erros:** Blocos `try/except` para prevenir falhas ao digitar valores não numéricos ou datas inválidas.
  * **Manipulação de Arquivos:** Uso da biblioteca `csv` para persistência de dados.

## 🚀 Como Executar o Projeto

### Pré-requisitos

  * Python 3.x instalado.

### Passo a Passo

1.  Baixe o arquivo `projeto_despesas.py`.
2.  Abra o terminal ou prompt de comando na pasta do arquivo.
3.  Execute o comando:
    ```bash
    python projeto_despesas.py
    ```
4.  Utilize o menu interativo para navegar.
      * *Dica:* Use a **Opção 0** logo no início para carregar dados de exemplo e testar os gráficos rapidamente.

## 📂 Estrutura do Código

```python
despesas = []  # Lista principal de dicionários

# Funções Principais
def adicionar_despesa(): ...
def listar_despesas(): ...
def analisar_gastos(): ... # Contém a lógica do gráfico em texto
def relatorio_mensal(): ...
def exportar_csv(): ...

# Utilitários
def gerar_dados_teste(): ... # Preenche lista para testes rápidos
def menu_principal(): ...    # Loop principal do programa
```

## ✒️ Autor

Desenvolvido como requisito para aprovação no Curso de Letramento Digital em Python.
