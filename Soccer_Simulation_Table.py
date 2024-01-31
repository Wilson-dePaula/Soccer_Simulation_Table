#imports
import random

#Class/functions
class Campeonato:

    dict_camp = {}

    def __init__(self, time_camp):
        self._arquivo_jogos = []
        self.times = []
        self.list_aux_times = []
        self._time = time_camp

    def salvar_times(self):
        with open('times.txt', 'a') as controle:
            controle.write(str(self._time) + '\n')
        self.dict_camp.update({self._time: 0})

    def gerar_jogo(self):
        arq = open('times.txt')
        self.times = arq.readlines()
        for time1 in self.times:
            self.list_aux_times = self.times.copy()
            self.list_aux_times.remove(time1)
            for time2 in self.list_aux_times:
                game = (time1.replace('\n', ''), random.randint(0,5), 'x', random.randint(0,5), time2.replace('\n', ''))
                self._arquivo_jogos.append(game)
                print(game)

    def classifica_camp(self):
        self.gerar_jogo()
        for jogo in self._arquivo_jogos:
            if jogo[1] > jogo[3]:
                self.dict_camp[jogo[0]] = self.dict_camp[jogo[0]] + 3
            elif jogo[1] < jogo[3]:
                self.dict_camp[jogo[4]] = self.dict_camp[jogo[4]] + 3
            else:
                self.dict_camp[jogo[0]] = self.dict_camp[jogo[0]] + 1
                self.dict_camp[jogo[4]] = self.dict_camp[jogo[4]] + 1
        print(self.dict_camp)


if __name__ == '__main__':
    while True:
        time = input('Digite o nome do seu time para entrar no campeonato')
        Campeonato(time).salvar_times()
        while True:
            check = input('Continuar adicionando jogadores?(S/N)')
            if check.upper() in ['S', 'N']:
                break
        if check.upper() == 'N':
            Campeonato(time).classifica_camp()
            break
