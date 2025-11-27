import csv
from datetime import datetime

# Estrutura de dados principal: Lista de dicionários
despesas = []

def limpar_tela():
    print("\n" + "="*40 + "\n")

def gerar_dados_teste():
    """
    Função auxiliar para preencher a lista com dados fictícios.
    Ajuda a testar os relatórios e gráficos sem precisar digitar tudo manualmente.
    """
    global despesas
    # Limpa a lista antes de adicionar para não duplicar se chamar duas vezes
    despesas = [
        {'data': '2024-10-05', 'categoria': 'Alimentação', 'valor': 450.00, 'descricao': 'Compras do Mês'},
        {'data': '2024-10-10', 'categoria': 'Transporte', 'valor': 25.90, 'descricao': 'Uber'},
        {'data': '2024-10-15', 'categoria': 'Lazer', 'valor': 120.00, 'descricao': 'Cinema e Jantar'},
        {'data': '2024-11-01', 'categoria': 'Alimentação', 'valor': 30.00, 'descricao': 'Padaria'},
        {'data': '2024-11-02', 'categoria': 'Educação', 'valor': 89.90, 'descricao': 'Livro Python'},
        {'data': '2024-11-05', 'categoria': 'Transporte', 'valor': 4.50, 'descricao': 'Ônibus'},
        {'data': '2024-11-20', 'categoria': 'Saúde', 'valor': 200.00, 'descricao': 'Consulta Médica'}
    ]
    print("✅ Dados de teste carregados com sucesso!")
    print(f"Foram adicionadas {len(despesas)} despesas.")

def adicionar_despesa():
    """
    Função para registrar uma nova despesa.
    Inclui tratamento de erros para valores e datas.
    """
    print("--- Adicionar Nova Despesa ---")
    try:
        descricao = input("Descrição (ex: Supermercado): ")
        categoria = input("Categoria (ex: Alimentação, Transporte): ")
        
        # Tratamento do valor (troca vírgula por ponto para evitar erro)
        valor_input = input("Valor (R$): ").replace(',', '.')
        valor = float(valor_input)
        
        # Tratamento da data
        data_input = input("Data (DD/MM/AAAA) ou deixe vazio para hoje: ")
        if data_input == "":
            data_formatada = datetime.now().strftime("%Y-%m-%d")
        else:
            data_obj = datetime.strptime(data_input, "%d/%m/%Y")
            data_formatada = data_obj.strftime("%Y-%m-%d")

        nova_despesa = {
            'data': data_formatada,
            'categoria': categoria,
            'valor': valor,
            'descricao': descricao
        }
        
        despesas.append(nova_despesa)
        print("✅ Despesa adicionada com sucesso!")
        
    except ValueError:
        print("❌ Erro: Certifique-se de digitar um valor numérico e a data no formato correto.")

def listar_despesas():
    """Lista todas as despesas registradas, ordenadas por data."""
    print("--- Lista de Despesas ---")
    if not despesas:
        print("Nenhuma despesa registrada.")
        return

    # Ordena a lista pela data (chave 'data')
    despesas_ordenadas = sorted(despesas, key=lambda x: x['data'])
    
    print(f"{'DATA':<12} | {'CATEGORIA':<15} | {'VALOR (R$)':<10} | {'DESCRIÇÃO'}")
    print("-" * 60)
    for item in despesas_ordenadas:
        # Converte a data do formato ISO (AAAA-MM-DD) para Brasileiro (DD/MM/AAAA)
        data_br = datetime.strptime(item['data'], "%Y-%m-%d").strftime("%d/%m/%Y")
        print(f"{data_br:<12} | {item['categoria']:<15} | {item['valor']:<10.2f} | {item['descricao']}")

def analisar_gastos():
    """
    Mostra estatísticas e um gráfico de barras simples em texto.
    """
    if not despesas:
        print("Sem dados para analisar.")
        return

    totais = {}
    total_geral = 0

    # Agrupa valores por categoria
    for item in despesas:
        cat = item['categoria']
        val = item['valor']
        totais[cat] = totais.get(cat, 0) + val
        total_geral += val

    print(f"--- Análise de Gastos (Total Geral: R$ {total_geral:.2f}) ---")
    
    # Identifica o maior gasto
    maior_categoria = max(totais, key=totais.get)
    print(f"🚨 Categoria com maior gasto: {maior_categoria} (R$ {totais[maior_categoria]:.2f})\n")

    print("--- Gráfico de Distribuição ---")
    for cat, valor in totais.items():
        # Regra de 3 simples para a porcentagem
        porcentagem = int((valor / total_geral) * 100) if total_geral > 0 else 0
        # Cria a barra visual (cada quadrado █ vale aprox. 2%)
        barra = "█" * (porcentagem // 2) 
        print(f"{cat:<15} R$ {valor:<8.2f} | {barra} ({porcentagem}%)")

def relatorio_mensal():
    """Filtra despesas por mês e ano específicos."""
    try:
        mes_ano = input("Digite o mês e ano para filtrar (MM/AAAA): ")
        mes, ano = mes_ano.split('/')
        
        # Filtra strings de data que começam com 'AAAA-MM'
        filtradas = [d for d in despesas if d['data'].startswith(f"{ano}-{mes}")]
        
        if not filtradas:
            print(f"Nenhuma despesa encontrada em {mes_ano}.")
        else:
            total_mes = sum(d['valor'] for d in filtradas)
            print(f"\n--- Relatório de {mes_ano} ---")
            for d in filtradas:
                print(f"{d['data']} - {d['descricao']}: R$ {d['valor']:.2f}")
            print(f"\n💰 Total gasto no mês: R$ {total_mes:.2f}")
            
    except ValueError:
        print("❌ Formato inválido. Use MM/AAAA (ex: 10/2024).")

def exportar_csv():
    """Salva os dados em um arquivo .csv compatível com Excel."""
    if not despesas:
        print("Nada para exportar.")
        return
    
    nome_arquivo = "relatorio_despesas.csv"
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            campos = ['data', 'categoria', 'valor', 'descricao']
            writer = csv.DictWriter(file, fieldnames=campos)
            
            writer.writeheader()
            for d in despesas:
                writer.writerow(d)
        print(f"✅ Dados exportados com sucesso para '{nome_arquivo}'.")
    except Exception as e:
        print(f"❌ Erro ao exportar: {e}")

def menu_principal():
    """Menu interativo para controle do fluxo do programa."""
    while True:
        limpar_tela()
        print("=== CONTROLE DE DESPESAS PESSOAIS ===")
        print("0. CARREGAR DADOS DE TESTE (Preencher automático)")
        print("1. Adicionar Despesa")
        print("2. Listar Todas as Despesas")
        print("3. Analisar Gastos (Gráfico)")
        print("4. Relatório Mensal")
        print("5. Exportar para CSV")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '0':
            gerar_dados_teste()
        elif opcao == '1':
            adicionar_despesa()
        elif opcao == '2':
            listar_despesas()
        elif opcao == '3':
            analisar_gastos()
        elif opcao == '4':
            relatorio_mensal()
        elif opcao == '5':
            exportar_csv()
        elif opcao == '6':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
