class CalculadoraIMC:
    """
    Classe responsável exclusivamente pela regra de negócio (Lógica).
    Não deve conter nenhum código de interface visual (print, input, tkinter).
    """

    def _tratar_entrada(self, valor):
        """
        Método auxiliar (privado) para converter entrada em float.
        Aceita tanto ponto quanto vírgula como separador decimal.
        """
        if isinstance(valor, (int, float)):
            return float(valor)
        
        # Se for string, tenta limpar e converter
        if isinstance(valor, str):
            valor_limpo = valor.replace(',', '.').strip()
            try:
                return float(valor_limpo)
            except ValueError:
                raise ValueError("O valor informado não é um número válido.")
        
        raise ValueError("Tipo de dado inválido.")

    def calcular_indice(self, peso, altura):
        """Calcula a matemática pura do IMC."""
        peso_float = self._tratar_entrada(peso)
        altura_float = self._tratar_entrada(altura)

        if altura_float <= 0 or peso_float <= 0:
            raise ValueError("Peso e altura devem ser maiores que zero.")

        # Fórmula: peso / (altura * altura)
        imc = peso_float / (altura_float ** 2)
        return round(imc, 2)

    def classificar_imc(self, imc_valor):
        """Retorna a string de classificação baseada na tabela oficial."""
        if imc_valor < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc_valor < 24.9:
            return "Peso Normal"
        elif 25.0 <= imc_valor < 29.9:
            return "Sobrepeso"
        elif 30.0 <= imc_valor < 34.9:
            return "Obesidade Grau 1"
        elif 35.0 <= imc_valor < 39.9:
            return "Obesidade Grau 2"
        else:
            return "Obesidade Grau 3 (Mórbida)"

    def processar_dados(self, peso_input, altura_input):
        """
        Método 'Fachada' (Facade) para a interface.
        Recebe os dados brutos e retorna um dicionário com tudo pronto.
        """
        try:
            imc = self.calcular_indice(peso_input, altura_input)
            classificacao = self.classificar_imc(imc)
            
            return {
                "sucesso": True,
                "imc": imc,
                "texto": classificacao,
                "mensagem": f"Seu IMC é {imc} ({classificacao})"
            }
        except ValueError as e:
            # Em caso de erro, retorna o erro tratado para a interface exibir
            return {
                "sucesso": False,
                "erro": str(e)
            }

# Área de teste manual (só roda se você executar este arquivo diretamente)
if __name__ == "__main__":
    calc = CalculadoraIMC()
    print("Teste 1 (Dados normais):", calc.processar_dados("70", "1.75"))
    print("Teste 2 (Com vírgula):", calc.processar_dados("80,5", "1,80"))
    print("Teste 3 (Erro):", calc.processar_dados("texto", "1.75"))