def leiadinheiro(txt):
    while True:
        num = str(input(txt)).strip().replace(',', '.')
        if num.isalnum() or num == '':
            print(f'\033[31mERRO! "{num}" é um preço inválido\033[0m')
        else:
            return float( num )
