from stages import Lead
from repo import LeadRepo
from typing import List

class CRMApp:
    def __init__(self):
        self.repo = LeadRepo()

    def _get_all_leads(self) -> List[Lead]:
        return self.repo.load_leads()

    def add_lead(self):
        print("\n=== ADICIONAR NOVO LEAD ===")
        name = input("Nome: ")
        company = input("Empresa: ")
        email = input("Email: ")

        # Cria um novo objeto Lead
        new_lead = Lead(name, company, email)

        self.repo.create(new_lead)
        print("\nLead adicionado com sucesso!\n")

    def list_leads(self):
        leads = self._get_all_leads()

        if not leads:
            print("Nenhum lead encontrado.\n")
            return

        print("\n=== LISTA DE LEADS ===")
        for i, lead in enumerate(leads, start=1):
            # Acessando os atributos do objeto Lead
            print(f"{i}. Nome: {lead.name}")
            print(f" Empresa: {lead.company}")
            print(f" Email: {lead.email}")
            print(f" Estágio: {lead.stage}")
            print(f" Criado em: {lead.created}\n")

    def search_leads(self):
        leads = self._get_all_leads()

        if not leads:
            print("Nenhum lead cadastrado para buscar.\n")
            return

        term = input("Digite o nome, empresa ou email para buscar: ").strip().lower()

        # Lista de Leads que correspondem ao termo
        found = [
            lead for lead in leads
            if term in lead.name.lower() or
               term in lead.company.lower() or
               term in lead.email.lower()
        ]

        if not found:
            print(f"Nenhum lead encontrado para: '{term}'.\n")
            return

        print(f"\n=== RESULTADOS DA BUSCA ({len(found)}) ===")
        for i, lead in enumerate(found, start=1):
            print(f"{i}. Nome: {lead.name}")
            print(f" Empresa: {lead.company}")
            print(f" Email: {lead.email}")
            print(f" Estágio: {lead.stage}")
            print(f" Criado em: {lead.created}\n")

    def print_menu(self):
        print("\n=== Mini CRM de Leads (POO) ===")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Procurar lead")
        print("[0] Sair")

    def main(self):
        while True:
            self.print_menu()
            op = input("Escolha: ")

            if op == "1":
                self.add_lead()
            elif op == "2":
                self.list_leads()
            elif op == "3":
                self.search_leads()
            elif op == "0":
                print(" Até mais!")
                break
            else:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    app = CRMApp()
    app.main()