import logging
from util import logcfg
import random
from pprint import pprint

palos = ["oros", "copas", "espadas", "bastos"]
valores = [x for x in range(1, 13) if x <= 7 or x >= 10]
cartas = [(p, v) for p in palos for v in valores]

N_VECES = 3
N_Tiradas = 3


# res = {23: 10600,24 :1000}
# exp = {23: 1 , 25:1 }
# return {23:10601 , 24:10000, 25:1}
def suma_res_experimento(res, experimento):
    for k in experimento.keys():
        antiguo = res.get(k, 0)
        res[k] = antiguo + experimento[k]
    return res


def tirada_cartas():
    tirada = random.sample(cartas, 2)
    res_tirada = 0
    for carta in tirada:
        res_tirada += carta[1]
    return res_tirada


def suma_res_tiradas(res, tir):
    antiguo = res.get(tir, 0)
    res[tir] = antiguo + 1
    return res


def experimento_cartas():
    res_experimento = {}
    for _ in range(N_Tiradas):
        res_tir = tirada_cartas()
        res_experimento = suma_res_tiradas(res_experimento, res_tir)
        return res_experimento


def main():
    resultado_prov = {}
    for _ in range(N_VECES):
        resEXP = experimento_cartas()
        resultado = suma_res_experimento(resultado_prov, resEXP)
    pprint(resultado_prov)


if __name__ == "__main__":
    main()
