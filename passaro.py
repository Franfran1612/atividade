class Ave:
    def __init__(self, nome, altura, data_nascimento, cor_de_pena,
                 tamanho_da_ave, falando=True, voando=False):
        self.nome = nome
        self.altura = altura
        self.data_nascimento = data_nascimento
        self.cor_de_pena = cor_de_pena
        self.tamanho_da_ave = tamanho_da_ave
        self.falando = falando
        self.voando = voando
        # /n é pra quebra linha

    def apresentar(self):
        print(f'Nome: {self.nome}\n'
              f' Altura: {self.altura}\n',
              f'Data de nascimento: {self.data_nascimento}\n',
              f'Cor da pena: {self.cor_de_pena}\n',
              f'Tamanho da Ave: {self.tamanho_da_ave } \n')


def falar(self):
    if self.falando:
        print("Essa ave consegue falar")
    else:
        print(" Não consigo  falar")


def voar(self):
    if self.voando:
        print("Esta ave consegue voar")
    else:
        print("Não consigo voar")


class Passaro(Ave):
    # toda vez que usar uma class tem que ter o int
    # em frente do self fica o atributos
    def __init__(self, nome, altura, data_nascimento, cor_de_pena, tamanho_da_ave , falando=True,
                 voando=False):
        super().__init__(nome, altura, data_nascimento, cor_de_pena, tamanho_da_ave , falando, voando)
        self.canta = True
        self.espalha_sementes = True
        self.caca = False

    def apresentar(self):
        print(f'Nome: {self.nome}\n'
              f' Altura: {self.altura}\n',
              f'Data de nascimento: {self.data_nascimento}\n',
              f'Cor da pena: {self.cor_de_pena}\n',
              f'Tamanho da Ave: {self.tamanho_da_ave }\n')

    def cantar(self):
        if self.canta:
            print("Este passaro canta")
        else:
            print(" Este não passaro canta")

    def espalhar(self):
        if self.espalha_sementes:
            print(f'Este passaro espalha sementes')
        else:
            print("Este passaro não espalha semente")

    def cacar(self):
        if self.caca:
            print(f'Este passaro caça ')

        else:
            print("Este passaro não caça ")


a1 = Passaro("loro", "10cm", "16/12/2020",
             "Verde", "30cm" , )
a1.apresentar()
a1.cacar()
a1.espalhar()
a1.cantar()



print("-" * 20)
