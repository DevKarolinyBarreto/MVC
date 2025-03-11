class Funcionario:
    def __init__(self, nome, cargo):
        self.__nome = nome
        self.__cargo = cargo

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def salario_base(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses")

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, 'Gerente')
        self.__salario = salario

    def salario_base(self):
        return self.__salario * 1.20

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, 'Desenvolvedor')
        self.__salario = salario

    def salario_base(self):
        return self.__salario * 1.10

class Estagiario(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, 'Estagiario')
        self.__salario = salario

    def salario_base(self):
        return self.__salario
class View:
    @staticmethod
    def exibir_funcionario(funcionario):
        print(f'O funcionário {funcionario.get_nome()} com o cargo {funcionario.get_cargo()} tem um salário de {funcionario.salario_base()}')

    @staticmethod
    def obter_dados_funcionario():
        nome = input('Insira um funcionário: ')
        salario = float(input('Insira o salário do funcionário: '))
        cargo = input('Insira o cargo do funcionário (Gerente, Desenvolvedor, Estagiario): ')
        return nome, salario, cargo

    @staticmethod
    def continuar():
        return input('Deseja inserir outro funcionário? (s/n): ').lower() == 's'

    @staticmethod
    def exibir_menu():
        print("\nMenu:")
        print("1. Adicionar funcionário")
        print("2. Exibir funcionários")
        print("3. Sair")
        return input("\nEscolha uma opção: ")

    @staticmethod
    def obter_nome_funcionario():
        return input('Insira o nome do funcionário para editar o salário: ')

    @staticmethod
    def obter_novo_salario():
        return float(input('Insira o novo salário do funcionário: '))
class Controller:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, nome, salario, cargo):
        if cargo.lower() == 'gerente':
            funcionario = Gerente(nome, salario)
        elif cargo.lower() == 'desenvolvedor':
            funcionario = Desenvolvedor(nome, salario)
        elif cargo.lower() == 'estagiario':
            funcionario = Estagiario(nome, salario)
        else:
            print('Cargo não reconhecido. Tente novamente.')
            return
        self.funcionarios.append(funcionario)

    def editar_salario(self, nome, novo_salario):
        for funcionario in self.funcionarios:
            if funcionario.get_nome() == nome:
                funcionario.set_salario(novo_salario)
                print(f'Salário de {nome} atualizado para {novo_salario}')
                return
        print(f'Funcionário {nome} não encontrado.')

    def exibir_funcionarios(self):
        for funcionario in self.funcionarios:
            View.exibir_funcionario(funcionario)

    def menu(self):
        while True:
            opcao = View.exibir_menu()
            if opcao == '1':
                nome, salario, cargo = View.obter_dados_funcionario()
                self.adicionar_funcionario(nome, salario, cargo)
            elif opcao == '2':
                nome = View.obter_nome_funcionario()
                novo_salario = View.obter_novo_salario()
                self.editar_salario(nome, novo_salario)
            elif opcao == '3':
                self.exibir_funcionarios()
            elif opcao == '4':
                print('Aff, saindo do programa...\nAff saiu...')
                break
            else:
                print('Opção inválida. Tente novamente.')

def main():
    print('\nSeja bem-vindo ao programa!')
    controller = Controller()
    controller.menu()

if __name__ == "__main__":
    main()



