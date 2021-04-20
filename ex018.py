from math import radians, sin, cos, tan

ang = int(input("Insira o ângulo: "))

print(f'Seja o ângulo de {ang}º.\n'
      f'SENO = {sin(radians(ang)):.2f}.\n'
      f'COSSENO = {cos(radians(ang)):.2f}.\n'
      f'TANGENTE = {tan(radians(ang)):.2f}.')
