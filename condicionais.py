nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Parabéns, você foi aprovado!")
elif nota >= 5:
    print("Você está de recuperação. Estude mais para melhorar sua nota.")
else:
    print("Infelizmente, você foi reprovado. Tente novamente no próximo semestre.")