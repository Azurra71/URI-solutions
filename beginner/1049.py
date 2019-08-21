vertebrado = input()
classe = input()
alimentacao = input()

animal_dict ={
    "vertebrado":{"ave":{"carnivoro":"aguia","onivoro":"pomba"},"mamifero":{"onivoro":"homem","herbivoro":"vaca"}},
    "invertebrado":{"inseto":{"hematofago":"pulga","herbivoro":"lagarta"},"anelideo":{"hematofago":"sanguessuga","onivoro":"minhoca"}}
}

print(animal_dict[vertebrado][classe][alimentacao])