import math

culturas = [] 
areas = [] 
insumos = [] 

def calcular_area_cafe(): 
    print("\n[CÁLCULO DE ÁREA - CAFÉ - Retângulo]") 
    comprimento = float(input("Digite o comprimento da plantação (m): ")) 
    largura = float(input("Digite a largura da plantação (m): ")) 
    return comprimento * largura 

def calcular_area_milho(): 
    print("\n[CÁLCULO DE ÁREA - MILHO - Círculo]") 
    raio = float(input("Digite o raio da área plantada (m): ")) 
    return math.pi * raio ** 2 

def adicionar_dados(): 
    print("\n[ENTRADA DE DADOS]") 
    tipo = input("Digite a cultura (café ou milho): ").strip().lower() 

    if tipo == "café": 
        area = calcular_area_cafe() 
    elif tipo == "milho": 
        area = calcular_area_milho() 
    else: 
        print("Cultura inválida!") 
        return 
    
    produto = input("Digite o nome do insumo (ex: fosfato): ") 
    qtd_por_metro = float(input("Quantidade aplicada por metro quadrado (mL): ")) 
    total = area * qtd_por_metro 
    culturas.append(tipo) 
    areas.append(area) 
    insumos.append({ "produto": produto, "qtd_por_m2": qtd_por_metro, "total": total}) 
    print("Dados adicionados com sucesso!") 

def exibir_dados(): 
    print("\n[SAÍDA DE DADOS]") 
    if not culturas: 
        print("Nenhum dado cadastrado.") 
    else: 
        print(culturas)
        for i in range(len(culturas)): 
            print(f"\nRegistro #{i}") 
            print(f"Cultura: {culturas[i]}") 
            print(f"Área: {areas[i]:.2f} m²") 
            print(f"Insumo: {insumos[i]['produto']}") 
            print(f"Qtd por m²: {insumos[i]['qtd_por_m2']} mL") 
            print(f"Total necessário: {insumos[i]['total']:.2f} mL") 

def atualizar_dados(): 
    print("\n[ATUALIZAÇÃO DE DADOS]") 
    indice = int(input("Digite o índice do registro a atualizar: ")) 
    if 0 <= indice < len(culturas): 
        novo_produto = input("Digite o novo insumo: ") 
        nova_qtd = float(input("Digite a nova quantidade por m² (mL): ")) 
        novo_total = areas[indice] * nova_qtd 
        insumos[indice] = {"produto": novo_produto, "qtd_por_m2": nova_qtd, "total": novo_total} 
        print("Registro atualizado com sucesso.") 
    else: 
        print("Índice inválido.") 

def deletar_dados(): 
    print("\n[DELEÇÃO DE DADOS]") 
    indice = int(input("Digite o índice do registro a deletar: ")) 
    if 0 <= indice < len(culturas): 
        culturas.pop(indice) 
        areas.pop(indice) 
        insumos.pop(indice) 
        print("Registro deletado com sucesso.") 
    else: 
        print("Índice inválido.") 

def menu(): 
    while True: 
        print("\n--- MENU FARMTECH ---") 
        print("1 - Inserir novo registro") 
        print("2 - Exibir registros") 
        print("3 - Atualizar registro") 
        print("4 - Deletar registro") 
        print("5 - Sair") 
        opcao = input("Escolha uma opção: ") 

        if opcao == "1": 
            adicionar_dados() 
        elif opcao == "2": 
            exibir_dados() 
        elif opcao == "3": 
            atualizar_dados() 
        elif opcao == "4": 
            deletar_dados() 
        elif opcao == "5": 
            print("Saindo do programa...") 
            break 
        else: 
            print("Opção inválida.") 
menu() 