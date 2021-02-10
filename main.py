from funcs import *
import os

print()
print(sta_if.ifconfig)
# Lê a lista de arquivos no diretorio
print('\nlistando arquivos')
a = os.listdir()
# Inicia Variaveis
print('iniciando variaveis')
users = {}
porta = 'cercomp'
# Inicializa as urls
print('primeiro get')
urls = 'erro'

# Checa se o arquivo 'users' existe, caso não exista ele cria e adiciona 'none', se existe ele le o conteudo e salda na variavel users
print('lendo arquivos')
if not ('users' in a):
    with open('users', 'w') as f:
        f.write('{"none":"none"}')
else:
    with open('users', 'r') as f:
        users = Porta(json.loads(f.read()))

print('--------------------------')
print('Lido do arquivo interno ')
print(users)
print('--------------------------')

cont = 0

while True:

    tag = do_read()# Chama a função que le tag
    if tag in users.tags():
        print('Porta aberta')
        
    cont = cont + 1
    if cont == 10:
        cont = 0
        if sta_if.isconnected():
            cont = 0
            if (urls != 'erro'):
                code = get_code(urls['get_code'])

                if code == 'none':
                    pass
                elif code == 'update':
                    u = get_users(urls['get_usuarios'])
                    if u == 'erro':
                        print('Erro no metodo get_user()')
                    else:
                        users = Porta(u)
                        print('------------------------')
                        print(users)
                        print('------------------------')
                        with open('users', 'w') as g:
                            g.write(json.dumps(u))

                elif code == 'create':
                    pass
                elif code == 'reboot':
                    pass
                elif code == 'erro':
                    print('Erro no metodo get_code()')
                else:
                    print('Algo deu errado')
            else:
                print('Erro no metodo get_url()')
                urls = get_url()
        else:
            do_connect()

    utime.sleep_ms(500)
