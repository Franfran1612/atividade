class Ave:
    def __init__(self, nome, altura, data_nascimento, cor_de_pena,
                 tamanho_da_ave, falando=True, voando=False):
        self.nome = nome
        self.altura = altura
        self._data_nascimento = data_nascimento
        self.cor_de_pena = cor_de_pena
        self.__tamanho_da_ave = tamanho_da_ave
        self._falando = falando
        self.voando = voando

        # /n é pra quebra linha

    def get_data_nascimento(self):
        return self._data_nascimento
    def get_tamanho_da_ave(self):
        return self.__tamanho_da_ave
    def get_falando(self):
        return self.__falando

    def set_voar(self, status):
        if self.voando and status:
            print("Esta voando e continua voando")
        elif self.voando and not status:
            print("Esta voando e não esta parado")
        elif not self.voando and status:
            print("Não esta voando mais esta parado")
        else:
            print("Não esta voando mais vai começar a voar")
            return self.voando

    def set_falar(self, status):
        if self._falando and status:
            print("Esta falando ")
        elif self._falando and not status:
            print("esta falando e vai parar de falar")
        else:
            print(" Não esta falando ")
            return self._falando

    def apresentar(self):
        print(f'Nome: {self.nome}\n'
              f' Altura: {self.altura}\n',
              f'Data de nascimento: {self.data_nascimento}\n',
              f'Cor da pena: {self.cor_de_pena}\n',
              f'Tamanho da Ave: {self.tamanho_da_ave } \n')


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
        print(f'\n Nome: {self.nome}',
              f' \n Altura: {self.altura}\n',
              f'Data de nascimento: {self.get_data_nascimento()}\n',
              f'Cor da pena: {self.cor_de_pena}\n',
              f'Tamanho da Ave: {self.get_tamanho_da_ave() }\n')

    def cantar(self):
        if self.canta:
            print("Este passaro canta")
        else:
            print("Este não passaro canta")

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
