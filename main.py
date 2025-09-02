# --- FarmTech Solutions: Sistema de Gerenciamento Agrícola ---
# Versão 1.0 - Modelo Inicial

# --- BANCO DE DADOS EM MEMÓRIA (usando um vetor/lista) ---
# Cada item na lista será um dicionário representando uma área de plantio.
# Usar um dicionário facilita a organização dos dados de cada plantio.
dados_plantio = []

# --- FUNÇÕES AUXILIARES ---

def mostrar_menu():
    """Exibe o menu principal de opções para o usuário."""
    print("\n--- MENU: FarmTech Solutions ---")
    print("1. Entrada de dados (Cadastrar nova área de plantio)")
    print("2. Saída de dados (Listar áreas cadastradas)")
    print("3. Atualização de dados (Modificar uma área)")
    print("4. Deleção de dados (Remover uma área)")
    print("5. Sair do programa")
    print("---------------------------------")

def adicionar_dados():
    """Coleta os dados de uma nova área de plantio e a adiciona ao nosso 'banco de dados'."""
    print("\n[+] Cadastro de Nova Área de Plantio")
    
    # TODO: Definam as duas culturas que o grupo irá trabalhar.
    # Exemplo: Soja e Milho. Valide se o usuário digitou uma delas.
    cultura = input("Digite o tipo de cultura (ex: Soja, Milho): ")
    
    print(f"\n--- Inserindo dados para a cultura: {cultura} ---")
    
    # TODO: Decidam qual figura geométrica usar para cada cultura.
    # Exemplo para uma área retangular:
    try:
        comprimento = float(input("Digite o comprimento do terreno (em metros): "))
        largura = float(input("Digite a largura do terreno (em metros): "))
        # Exemplo de cálculo de área
        area_calculada = comprimento * largura 
    except ValueError:
        print("Erro: Valor inválido. Por favor, insira apenas números.")
        return # Interrompe a função se o valor for inválido

    # TODO: Adicionem os dados necessários para o cálculo de insumos.
    # Exemplo: Quantidade de ruas da lavoura.
    try:
        ruas_lavoura = int(input("Digite a quantidade de ruas da lavoura: "))
        # Exemplo de cálculo de insumos
        # Pulverizar 500 mL/metro. Quantos litros serão necessários?
        # Supondo que o trator percorre o comprimento de cada rua.
        litros_insumo = (ruas_lavoura * comprimento * 500) / 1000 # Convertendo mL para Litros
    except ValueError:
        print("Erro: Valor inválido para ruas. Por favor, insira um número inteiro.")
        return

    # Organiza os dados em um dicionário
    novo_plantio = {
        "id": len(dados_plantio) + 1, # Um ID simples para facilitar a identificação
        "cultura": cultura,
        "area_m2": round(area_calculada, 2),
        "litros_insumo_necessarios": round(litros_insumo, 2)
    }
    
    # Adiciona o novo dicionário à nossa lista (vetor)
    dados_plantio.append(novo_plantio)
    
    print("\n✅ Área de plantio cadastrada com sucesso!")
    print(f"   ID: {novo_plantio['id']}, Cultura: {novo_plantio['cultura']}, Área: {novo_plantio['area_m2']} m², Insumo: {novo_plantio['litros_insumo_necessarios']} L")

def listar_dados():
    """Exibe todos os registros de plantio cadastrados."""
    print("\n[i] Listagem de Áreas Cadastradas")
    
    if not dados_plantio:
        print("   Nenhuma área de plantio cadastrada ainda.")
        return
        
    for plantio in dados_plantio:
        print("---------------------------------")
        print(f"  ID do Registro: {plantio['id']}")
        print(f"  Cultura: {plantio['cultura']}")
        print(f"  Área Total: {plantio['area_m2']} m²")
        print(f"  Insumo Necessário: {plantio['litros_insumo_necessarios']} Litros")
    print("---------------------------------")

def encontrar_indice_por_id(id_procurado):
    """Função para encontrar o índice de um registro na lista pelo seu ID."""
    for i, plantio in enumerate(dados_plantio):
        if plantio['id'] == id_procurado:
            return i # Retorna a posição (índice) na lista
    return None # Retorna None se não encontrar

def atualizar_dados():
    """Permite ao usuário modificar os dados de um registro existente."""
    print("\n[>] Atualização de Dados")
    listar_dados() # Mostra os dados para o usuário saber qual ID atualizar
    
    if not dados_plantio:
        return

    try:
        id_alvo = int(input("Digite o ID do registro que deseja atualizar: "))
        
        indice_do_registro = encontrar_indice_por_id(id_alvo)
        
        if indice_do_registro is None:
            print(f"❌ Erro: Registro com ID {id_alvo} não encontrado.")
            return
            
        print(f"\nAtualizando dados para o registro ID {id_alvo}. Deixe em branco para não alterar.")
        
        # Pega os dados atuais para mostrar ao usuário
        registro_atual = dados_plantio[indice_do_registro]

        # Pede os novos dados
        nova_cultura = input(f"Novo tipo de cultura ({registro_atual['cultura']}): ")
        nova_area = input(f"Nova área em m² ({registro_atual['area_m2']}): ")
        novo_insumo = input(f"Novo volume de insumo em Litros ({registro_atual['litros_insumo_necessarios']}): ")

        # Atualiza apenas os campos que foram preenchidos
        if nova_cultura:
            dados_plantio[indice_do_registro]['cultura'] = nova_cultura
        if nova_area:
            dados_plantio[indice_do_registro]['area_m2'] = float(nova_area)
        if novo_insumo:
            dados_plantio[indice_do_registro]['litros_insumo_necessarios'] = float(novo_insumo)

        print("\n✅ Registro atualizado com sucesso!")

    except ValueError:
        print("❌ Erro: O ID deve ser um número.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

def deletar_dados():
    """Remove um registro de plantio da lista."""
    print("\n[x] Deleção de Dados")
    listar_dados() # Mostra os dados para o usuário saber qual ID deletar
    
    if not dados_plantio:
        return
        
    try:
        id_alvo = int(input("Digite o ID do registro que deseja DELETAR: "))
        
        indice_do_registro = encontrar_indice_por_id(id_alvo)

        if indice_do_registro is None:
            print(f"❌ Erro: Registro com ID {id_alvo} não encontrado.")
            return
            
        # Confirmação de segurança
        confirmacao = input(f"Tem certeza que deseja deletar o registro {id_alvo}? (s/n): ").lower()
        
        if confirmacao == 's':
            dados_plantio.pop(indice_do_registro)
            print("✅ Registro deletado com sucesso!")
        else:
            print("Operação cancelada.")
            
    except ValueError:
        print("❌ Erro: O ID deve ser um número.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

# --- PROGRAMA PRINCIPAL ---

def main():
    """Função principal que executa o loop do programa."""
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_dados()
        elif opcao == '2':
            listar_dados()
        elif opcao == '3':
            atualizar_dados()
        elif opcao == '4':
            deletar_dados()
        elif opcao == '5':
            print("Saindo do programa... Obrigado por usar a FarmTech Solutions!")
            break # Encerra o loop while
        else:
            print("❌ Opção inválida. Por favor, escolha um número de 1 a 5.")

# Garante que o programa só vai rodar quando o arquivo for executado diretamente
if __name__ == "__main__":
    main()