
PRECOS = {
    "cabelo": 20.0,
    "barba": 10.0,
    "bigode": 5.0
}

fila_espera = []      
atendidos = []       
estatisticas = {      
    "cabelo": {"qtd": 0, "faturamento": 0},
    "barba": {"qtd": 0, "faturamento": 0},
    "bigode": {"qtd": 0, "faturamento": 0}
}

def sim_nao(pergunta):
    while True:
        resp = input(pergunta).strip().upper()
        if resp in ["S", "N"]:
            return resp
        print("Digite S ou N")


while True:
    print("\n" + "="*40)
    print("BARBEARIA SELSO & LUAN")
    print("="*40)
    print("1 - Cadastrar cliente")
    print("2 - Ver fila de espera")
    print("3 - Atender próximo cliente")
    print("4 - Relatório de gestão")
    print("0 - Sair")
    
    try:
        opcao = int(input("Opção: "))
    except ValueError:
        print("Opção inválida!")
        continue
    
    if opcao == 1:
        print("\n--- NOVO CLIENTE ---")
        nome = input("Nome: ").strip().upper()
        if not nome:
            print("Nome inválido!")
            continue
        
        print(f"\nPreços - Cabelo: R${PRECOS['cabelo']:.2f} | Barba: R${PRECOS['barba']:.2f} | Bigode: R${PRECOS['bigode']:.2f}")
        
        cliente = {
            "nome": nome,
            "cabelo": sim_nao("Cortar cabelo? (S/N): "),
            "barba": sim_nao("Cortar barba? (S/N): "),
            "bigode": sim_nao("Cortar bigode? (S/N): ")
        }
        
       
        total = 0
        if cliente["cabelo"] == "S":
            total += PRECOS["cabelo"]
        if cliente["barba"] == "S":
            total += PRECOS["barba"]
        if cliente["bigode"] == "S":
            total += PRECOS["bigode"]
        
        cliente["total"] = total
        fila_espera.append(cliente)
        print(f"{nome} adicionado à fila. Total: R${total:.2f}")
    

    elif opcao == 2:
        print("\n--- FILA DE ESPERA ---")
        if not fila_espera:
            print("Fila vazia!")
        else:
            for i, c in enumerate(fila_espera, 1):
                servicos = []
                if c["cabelo"] == "S": servicos.append("Cabelo")
                if c["barba"] == "S": servicos.append("Barba")
                if c["bigode"] == "S": servicos.append("Bigode")
                print(f"{i}º - {c['nome']} | Serviços: {', '.join(servicos)} | R${c['total']:.2f}")
    
   
    elif opcao == 3:
        print("\n--- REALIZAR ATENDIMENTO ---")
        if not fila_espera:
            print("Não há clientes na fila!")
            continue
        
        
        cliente = fila_espera.pop(0)
        
     
        servicos = []
        if cliente["cabelo"] == "S": servicos.append("Cabelo")
        if cliente["barba"] == "S": servicos.append("Barba")
        if cliente["bigode"] == "S": servicos.append("Bigode")
        
        print(f"Cliente: {cliente['nome']}")
        print(f"Serviços: {', '.join(servicos)}")
        print(f"Valor a pagar: R${cliente['total']:.2f}")
        
        
        atendidos.append(cliente)
        if cliente["cabelo"] == "S":
            estatisticas["cabelo"]["qtd"] += 1
            estatisticas["cabelo"]["faturamento"] += PRECOS["cabelo"]
        if cliente["barba"] == "S":
            estatisticas["barba"]["qtd"] += 1
            estatisticas["barba"]["faturamento"] += PRECOS["barba"]
        if cliente["bigode"] == "S":
            estatisticas["bigode"]["qtd"] += 1
            estatisticas["bigode"]["faturamento"] += PRECOS["bigode"]
        
        print("Atendimento finalizado!")
    
    elif opcao == 4:
        print("\n--- RELATÓRIO DE GESTÃO ---")
        print(f"Total de clientes atendidos: {len(atendidos)}")
        print("\nDetalhamento por serviço:")
        for servico, dados in estatisticas.items():
            if dados["qtd"] > 0:
                print(f"  {servico.capitalize()}: {dados['qtd']} unidade(s) | R${dados['faturamento']:.2f}")
        
        faturamento_total = sum(d["faturamento"] for d in estatisticas.values())
        print(f"\n💰 Faturamento total: R${faturamento_total:.2f}")
    
    # Sair
    elif opcao == 0:
        print("Obrigado! Volte sempre!")
        break
    
    else:
        print("Opção inválida!")