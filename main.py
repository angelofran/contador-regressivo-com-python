from time import sleep

while True:
    try:
        início = int(input('Início da contagem: '))
        fim = int(input('Fim da contagem: '))
        passo = int(input('Passo da contagem: '))
        if início > fim:
            for c in range(início, fim-1, -(passo)):
                print(f'\033[32m{c}\033[m » ', end='', flush=True)
                sleep(1)
            print('\033[31mFim\033[m')
        else:
            for c in range(início, fim+1, passo):
                print(f'\033[32m{c}\033[m » ', end='', flush=True)
                sleep(1)
            print('Fim')

        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'N':
            break
    except (ValueError, TypeError):
        print('\033[31mPor favor, preencha todos os campos correctamente!Naõ tente reinicializar o programa enquanto ele estiver rodando\033[m')
print('\033[36m««Programa Finalizado»»\033[m')
