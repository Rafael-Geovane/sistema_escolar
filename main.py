class Aluno:
    def __init__(self, nome, idade, curso):
        self.__nome = nome
        self.__idade = idade
        self.__curso = curso
        self.__matriculado = False
        self.__nota1 = 0.0
        self.__nota2 = 0.0

    # Getters e setters 
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        if not nome.strip():
            print("Nome inválido.")
            return False
        self.__nome = nome.strip()
        return True

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        if idade < 0:
            print("Idade inválida.")
            return False
        self.__idade = idade
        return True

    def getCurso(self):
        return self.__curso

    def setCurso(self, curso):
        if not curso.strip():
            print("Curso inválido.")
            return False
        self.__curso = curso.strip()
        return True

    def getMatriculado(self):
        return self.__matriculado

    def setMatriculado(self, matriculado):
        self.__matriculado = matriculado

    def getNota1(self):
        return self.__nota1

    def setNota1(self, nota):
        if nota < 0 or nota > 10:
            print("Nota 1 inválida.")
            return False
        self.__nota1 = nota
        return True

    def getNota2(self):
        return self.__nota2

    def setNota2(self, nota):
        if nota < 0 or nota > 10:
            print("Nota 2 inválida.")
            return False
        self.__nota2 = nota
        return True

    # Métodos do sistema escolar
    def matricular(self):
        if self.__matriculado:
            print("Aluno já está matriculado.")
            return False
        self.__matriculado = True
        print("Aluno matriculado com sucesso!")
        return True

    def cancelarMatricula(self):
        if not self.__matriculado:
            print("Aluno já está com matrícula inativa.")
            return False
        self.__matriculado = False
        print("Matrícula cancelada.")
        return True

    def verificarMaioridade(self):
        if self.__idade >= 18:
            return "Aluno é maior de idade e pode participar de cursos noturnos."
        return "Aluno é menor de idade."

    def cadastrarNotas(self, n1, n2):
        if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
            print("Notas inválidas: informe valores entre 0 e 10.")
            return False
        self.__nota1 = n1
        self.__nota2 = n2
        print("Notas cadastradas com sucesso!")
        return True

    def calcularMedia(self):
        if self.__nota1 == 0 and self.__nota2 == 0:
            print("Notas ainda não cadastradas.")
            return None
        return (self.__nota1 + self.__nota2) / 2

    def verificarAprovacao(self):
        media = self.calcularMedia()
        if media is None:
            print("Notas não cadastradas.")
            return "Notas não cadastradas"
        if media >= 7:
            print("Aprovado")
            return "Aprovado"
        print("Reprovado")
        return "Reprovado"

    def exibirInformacoes(self):
        print("\n========== SISTEMA ESCOLAR ==========")
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")
        print(f"Curso: {self.__curso}")
        print(f"Matrícula: {'Ativa' if self.__matriculado else 'Inativa'}")
        print(f"Nota 1: {self.__nota1:.1f}")
        print(f"Nota 2: {self.__nota2:.1f}")
        if self.__nota1 == 0 and self.__nota2 == 0:
            print("Média: Notas ainda não cadastradas")
        else:
            print(f"Média: {(self.__nota1 + self.__nota2) / 2:.1f}")
        print("=====================================")


""" AREA DE TESTES DO CODIGO """

# teste 1 (criar 3 alunos)
print("\nTESTE 1 - Criando os alunos")
maria = Aluno("Maria Souza", 20, "Sistemas de Informação")
joao = Aluno("João Silva", 16, "Desenvolvimento de Sistemas")
pedro = Aluno("Pedro Lima", 19, "Informática")
print("Verificando se começaram sem matrícula e sem notas")
assert maria.getMatriculado() == False
assert joao.getMatriculado() == False
assert pedro.getNota1() == 0
assert pedro.getNota2() == 0
print("Mostrando os alunos criados")
maria.exibirInformacoes()
joao.exibirInformacoes()
pedro.exibirInformacoes()

# teste 2 (matricular aluno)
print("\nTESTE 2 - Realizando matrícula")
print("Matriculando Maria")
assert maria.matricular() == True
assert maria.getMatriculado() == True
maria.exibirInformacoes()

# teste 3 (tentar matricular novamente)
print("\nTESTE 3 - Tentando repetir a matrícula")
print("Tentando matricular Maria novamente")
assert maria.matricular() == False
assert maria.getMatriculado() == True
maria.exibirInformacoes()

# teste 4 (verificar maioridade)
print("\nTESTE 4 - Verificando maioridade")
print("Verificando Maria, que tem 20 anos")
print(maria.verificarMaioridade())
assert "maior de idade" in maria.verificarMaioridade()
print("Verificando João, que tem 16 anos")
print(joao.verificarMaioridade())
assert "menor de idade" in joao.verificarMaioridade()

# teste 5 (cadastrar notas)
print("\nTESTE 5 - Cadastrando notas")
print("Cadastrando notas 8 e 9 para Maria")
assert maria.cadastrarNotas(8, 9) == True
assert maria.getNota1() == 8
assert maria.getNota2() == 9
maria.exibirInformacoes()

# teste 6 (calcular média)
print("\nTESTE 6 - Calculando média")
print("Calculando a média da Maria")
print(f"Média: {maria.calcularMedia():.1f}")
assert maria.calcularMedia() == 8.5

# teste 7 (verificar aprovação)
print("\nTESTE 7 - Verificando aprovação")
print("Verificando a aprovação de Maria")
assert maria.verificarAprovacao() == "Aprovado"

# teste 8 (alterar dados com setters)
print("\nTESTE 8 - Alterando dados do aluno")
print("Alterando o nome de Maria Souza para Maria Oliveira")
assert maria.setNome("Maria Oliveira") == True
assert maria.getNome() == "Maria Oliveira"
print("Alterando o curso de Maria")
assert maria.setCurso("Análise de Sistemas") == True
assert maria.getCurso() == "Análise de Sistemas"
maria.exibirInformacoes()

# teste 9 (verificar reprovação)
print("\nTESTE 9 - Verificando aluno reprovado")
print("Matriculando João e cadastrando notas 5 e 6")
assert joao.matricular() == True
assert joao.cadastrarNotas(5, 6) == True
assert joao.calcularMedia() == 5.5
assert joao.verificarAprovacao() == "Reprovado"
joao.exibirInformacoes()

# teste 10 (tentar cadastrar notas inválidas)
print("\nTESTE 10 - Tentando cadastrar notas inválidas")
print("Tentando cadastrar -1 e 11 para Maria")
assert maria.cadastrarNotas(-1, 11) == False
assert maria.getNota1() == 8
assert maria.getNota2() == 9
maria.exibirInformacoes()

# teste 11 (consultar aluno sem notas)
print("\nTESTE 11 - Consultando aluno sem notas")
print("Consultando a média e a aprovação de Pedro")
assert pedro.calcularMedia() is None
assert pedro.verificarAprovacao() == "Notas não cadastradas"
pedro.exibirInformacoes()

# teste 12 (cancelar matrícula)
print("\nTESTE 12 - Cancelando matrícula")
print("Cancelando a matrícula de Maria")
assert maria.cancelarMatricula() == True
assert maria.getMatriculado() == False
print("Tentando cancelar novamente")
assert maria.cancelarMatricula() == False
maria.exibirInformacoes()

print("\nTODOS OS 12 TESTES FORAM CONCLUIDOS COM SUCESSO!")
