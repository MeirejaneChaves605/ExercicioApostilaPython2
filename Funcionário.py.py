class Funcionario:
    """
    Classe base para representar um funcionário.
    """
    def __init__(self, nome, salario_base):
        """
        Inicializa um objeto Funcionario.

        Args:
            nome (str): O nome do funcionário.
            salario_base (float): O salário base do funcionário.
        """
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        """
        Calcula e retorna o salário do funcionário.

        Returns:
            float: O salário base do funcionário.
        """
        return self.salario_base

    def exibir_dados(self):
        """
        Exibe o nome e o salário do funcionário.
        """
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.calcular_salario():.2f}")


class FuncionarioComissionado(Funcionario):
    """
    Subclasse para representar um funcionário comissionado.
    """
    def __init__(self, nome, salario_base, comissao):
        """
        Inicializa um objeto FuncionarioComissionado.

        Args:
            nome (str): O nome do funcionário.
            salario_base (float): O salário base do funcionário.
            comissao (float): O valor da comissão.
        """
        super().__init__(nome, salario_base)
        self.comissao = comissao

    def calcular_salario(self):
        """
        Calcula e retorna o salário total do funcionário (salário base + comissão).

        Returns:
            float: A soma do salário base e da comissão.
        """
        return self.salario_base + self.comissao

    def exibir_dados(self):
        """
        Exibe o nome, salário e comissão do funcionário comissionado.
        """
        print(f"Nome: {self.nome}")
        print(f"Salário base: R${self.salario_base:.2f}")
        print(f"Comissão: R${self.comissao:.2f}")
        print(f"Salário total: R${self.calcular_salario():.2f}")

# ---
# Instanciando e mostrando os dados dos funcionários

# Instância de um funcionário regular
print("--- Dados do Funcionário Regular ---")
funcionario_regular = Funcionario("João Silva", 3000.00)
funcionario_regular.exibir_dados()

print("\n") # Adiciona uma linha em branco para melhor separação

# Instância de um funcionário comissionado
print("--- Dados do Funcionário Comissionado ---")
funcionario_comissionado = FuncionarioComissionado("Maria Oliveira", 2500.00, 500.00)
funcionario_comissionado.exibir_dados()

   