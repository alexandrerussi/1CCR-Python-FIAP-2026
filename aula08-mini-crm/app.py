from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    company = input("Empresa: ")
    stage = input("Etapa de venda: ")

    # regex
    if not name or not email or not company or "@" not in email:
        print("Nome ou e-mail inválido")
        return

    print(model_lead(name, email, company, stage))

    control.create_lead(model_lead(name, email, company, stage))


    print("Lead adicionado")

def list_leads():
    leads = control.read_leads()
    if not leads:
        print("Nenhum lead ainda")
        return

    # print("\n# | Nome          | E-mail           | Empresa")
    print(f"# | {"Nome":<15} | {"E-mail":<15} | Empresa")
    for i, lead in enumerate(leads):
        print(f"{i:02d}| {lead["name"]:<15} | {lead["email"]:<15} | {lead["company"]}")


def main():
    while True:
        # print menu
        print("\nMini CRM de Leads")
        print("[1] Adicionar um lead")
        print("[2] Listar leads")
        print("[0] Sair")

        opt = input("Escolha uma opção: ").strip()

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
