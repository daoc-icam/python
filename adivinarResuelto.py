#imports
from random import randint
from datetime import datetime

#functions
def main(start=1, stop=100):
    logFile = open('log.txt', 'a')
    rndNum = randint(start, stop)
    counter = 0
    log(logFile, f'Inicia: {datetime.now()} Rnd: {rndNum}\n')
    done = False
    while done == False:
        usrNum = getUserInput(start, stop)
        counter += 1
        log(logFile, f'Intento: {counter} Num: {usrNum}\n')
        if usrNum == rndNum:
            print('Ganó !!!')
            done = True
        elif usrNum > rndNum:
            print('Muy alto')
        else:
            print('Muy bajo')
    logFile.close()

def getUserInput(start, stop):
    numOk = False
    while numOk == False:
        try:
            num = input(f'Ingrese un número entre {start} y {stop}: ')
            num = int(num)
            if num < start or num > stop:
                raise Exception
            numOk = True
        except:
            print('NO ingresó lo solicitado')
    return num

def log(logFile, message):
    logFile.write(message)

#launch
if __name__ == '__main__':
    main(1, 5)