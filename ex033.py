while True:
    try:
        numbers = input('Digite três números: ').strip().replace(',', '').split()
        if type(int(numbers[0])) != int:
            continue
        else:
            print(f'O maior número é {sorted(numbers, reverse=True)[0]}.\n'
                  f'O menor número é {sorted(numbers)[0]}.')
            break
    except ValueError:
        continue
