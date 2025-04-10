"""
Estruturas Lógicas: and (e), or(ou), not(não), is (é)

Operadores unarios:
    - not, is
Operadores binarios
    - and, or
    
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleanop é invertido, ou seja se for True, vira False , se for False vira True
"""

ativo = False
logado = False

if ativo and logado:
    print("Bem vindo ao nosso sistema")
elif not ativo and not logado:
    print("""
          Você precisa ativar sua conta,
          Você precisa estar logado
          """)

elif ativo is False:
    print("Você precisa ativar sua conta")
elif not logado:
    print("Você precisa estar logado")