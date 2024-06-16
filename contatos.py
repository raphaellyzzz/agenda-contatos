class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"o contato {nome} foi removido com sucesso")
                return
        print("o contato não foi encontrado")

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                print(f"nome: {contato.nome}, número: {contato.numero}")
                return
        print("o contato não foi encontrado")

    def listar_contatos(self):
        if not self.contatos:
            print("agenda vazia.")
            return
        print("lista de contatos:")
        for contato in self.contatos:
            print(f"nome: {contato.nome}, número: {contato.numero}")

def main():
    agenda = Agenda()

    while True:
        print("\nselecione uma opção:")
        print("1. adicionar contato")
        print("2. remover contato")
        print("3. buscar contato")
        print("4. listar contatos")
        print("5. sair")

        opcao = input("opção: ")
        if opcao == "1":
            nome = input("nome do contato:")
            numero = input("número do contato:")
            contato = Contato(nome, numero)
            agenda.adicionar_contato(contato)

        elif opcao == "2":
            nome = input("nome do contato a ser removido:")
            agenda.remover_contato(nome)

        elif opcao == "3":
            nome = input("nome do contato a buscar:")
            agenda.buscar_contato(nome)

        elif opcao == "4":
            agenda.listar_contatos()

        elif opcao == "5":
            print("saindo do programa")
            break

        else:
            print("opção inválida.")

if __name__ == "__main__":
    main()