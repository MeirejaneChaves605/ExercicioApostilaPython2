
    class Funcionario:
    """
    Classe base para representar um funcionário.
    """
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self) -> float:
        """
        Calcula o salário total do funcionário.
        Para a classe base, retorna o salário base.
        """
        return self.salario_base

    def exibir_dados(self):
        """
        Exibe os dados básicos do funcionário.
        """
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.calcular_salario():.2f}")


class FuncionarioComissionado(Funcionario):
    """
    Subclasse que representa um funcionário comissionado.
    Herda de Funcionario e adiciona o conceito de comissão.
    """
    def __init__(self, nome: str, salario_base: float, comissao: float):
        # Chama o construtor da classe base (Funcionario)
        super().__init__(nome, salario_base)
        self.comissao = comissao

    def calcular_salario(self) -> float:
        """
        Sobrescreve o método da classe base para incluir a comissão.
        """
        return self.salario_base + self.comissao

    def exibir_dados(self):
        """
        Sobrescreve o método da classe base para exibir a comissão.
        """
        # Chama o método exibir_dados da classe base para reutilizar o código
        super().exibir_dados()
        print(f"Comissão: R${self.comissao:.2f}")


# --- Exemplo de Uso ---
# Instanciando um funcionário regular
print("--- Dados do Funcionário Regular ---")
funcionario_regular = Funcionario("João Silva", 3000.00)
funcionario_regular.exibir_dados()
print("-" * 35)

# Instanciando um funcionário comissionado
print("--- Dados do Funcionário Comissionado ---")
funcionario_comissionado = FuncionarioComissionado("Maria Oliveira", 2500.00, 500.00)
funcionario_comissionado.exibir_dados()
print("-" * 35)