nome = input('Nome do aluno: ') # Insere o nome do aluno 
x = float(input('Nota final: ')) # Insere a nota final 
while True: # Enquanto o laço for verdadeiro 
 if x <= 10.0 and x >= 9.0: # Se a nota for entre 9 e 10 
 conceito = 'A' # A variável Conceito será letra A 
 elif x <= 8.9 and x >= 7.0: # Se a nota for entre 7 e 8.9 
 conceito = 'B' # A variável Conceito será letra B 
 elif x <= 6.9 and x >= 5.0: # Se a nota for entre 5 e 6.9 
 conceito = 'C' # A variável Conceito será letra C 
 elif x <= 4.9 and x >= 3.0: # Se a nota for entre 3 e 4.9 
 conceito = 'D' # A variável Conceito será letra D 
 elif x <= 2.9 and x >= 0.0: # Se a nota for entre 0 e 2.9 
 conceito = 'E' # A variável Conceito será letra E 
 else: # Caso o contrário 
 print('Você digitou nota inválida. Encerrando o programa...') 
# imprime a mensagem 
 break 
# Encerra o laço e finaliza o programa 
 print('O aluno {} tirou nota {} e se enquadra no conceito 
{}'.format(nome, x, conceito)) 
 break # (print) se a nota entre 0 e 10, imprime a frase e as variáveis: nome, x, conceito . 
 # (break) Encerra o laço e finaliza o programa.
