def cria_conta(numero, titular, saldo, limite):
    conta={"numere":numero,"titular":titular,"saldo":saldo,"limite":limite}
    return conta 
    conta00=cria_conta(1234,"marcus",50.0,100.0)
    conta01=cria_conta(4321,"vinicius", 50.0,100.0)
def saldo(conta):
    print("contanumero:{}".format(conta["numero"]))
    print("titular: "+conta["titular"])
    print("saldo: {}".format(conta["saldo"]))
def deposito(conta,valor):
    conta +=valor
