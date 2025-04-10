# Strings

# Em Python um dado é considerado do tipo string sempre que estiver:
#     - entre aspas simples -> 'uma string', '123', 'a', 'True', '42.3'
#     - entre aspas duplas -> "uma string", "123", "a", "True", "42.3"
#     - entre tres aspas simples -> '''uma string''', '''123''', '''a''', '''True''', '''42.3'''
#     - entre tres aspas duplas -> """uma string""", """123""", """a""", """True""", """42.3"""

# print(type('ola'))
# print(type("123"))
# print(type('''True'''))
# print(type("""42.8"""))

# o '\n' serve para quebrar a linha
# nome = "Joao \nSiqueira"
# print(nome)

# # Quando utilizado tres aspas, sejam simples ou duplas é possivel escrever em multiplas linhas
# texto = """
# Consectetur qui amet tempor enim non nisi excepteur deserunt anim eu. 
# Cillum excepteur mollit quis est incididunt. 
# Sit officia et laborum qui aliquip est consequat ut aute. 
# Commodo ad adipisicing nulla anim consequat ut officia qui. 
# Dolor minim ad dolore tempor esse.
# """
# print(texto)
# produto = "Bola"
# preco = 2.95

# print(f"{produto}\t{preco}")

nome:str = 'Joao da Silva'
texto = "Sit,officia,et,laborum,qui,aliquip,est,consequat,ut,aute."
print(nome.upper())
print(nome.lower())
print(nome.capitalize())
print(nome.split())
print(texto.split(','))
print(nome[0:9])
print(nome.split()[1])

email = "joao@email.com"
print(email.replace("email.com","gmail.com"))