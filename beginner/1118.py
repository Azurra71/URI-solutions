def grading_system():
    notas = []
    while(len(notas) < 2):
        nota = float(input())
        if(0 <= nota <= 10):
            notas.append(nota)
        else:
            print("nota invalida")
    media=(float(notas[0])+float(notas[1]))*0.5
    print("media = {:.2f}".format(media))

grading_system()
op=0
while(op != 2):
    print("novo calculo (1-sim 2-nao)")
    op = int(input())
    if(op==1):
        grading_system()
