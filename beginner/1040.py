N1,N2,N3,N4 = map(float,input().split(" "))

media = ( (2*N1) + (3*N2) + (4*N3) + (1*N4) )/10

print("Media: {:.1f}".format(media))
if(media >= 7):
    print("Aluno aprovado.")
elif(media < 5):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())

    print("Nota do exame: {:.1f}".format(nota_exame))
    nova_media = (nota_exame+media)/2.0

    if(nova_media >= 5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: {:.1f}".format(nova_media))    