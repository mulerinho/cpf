# Exercício de validação de CPF

sair = ''
lista = []
def entrada():
	# Validando dados de entrada

	entrada_confirmada = True
	while entrada_confirmada:
		try:
			entrada = input('Digite os nove primeiros digitos do seu CPF sem pontos ou virgula.\nOu (q) para Sair ')
			if(entrada == 'q'):
				print('Fim')
				return 'q'
			converte_int = int(entrada)
			return converte_int
	
		except(ValueError, TypeError):
			print('Dados invalidos, digite apenas números inteiros.')
		



# Função de validação do primeiro dígito

def primeiro_digito(valor):
	# calculo do primeiro dígito
	entada_lista = str(retorno)
	index = 0
	multiplicador = 10
	for i in entada_lista:
		num = int(entada_lista[index])
		num = num * multiplicador
		lista.append(num)
		index += 1
		multiplicador -= 1
	total = sum(lista)
	verificador =  total * 10 % 11
	digito = 0 if verificador > 9 else verificador
	return digito
	    

	
	

					
# Calculando os verificadores

while sair != 'q':
		
	retorno = entrada()
	digito1 = primeiro_digito(retorno)
	print(f'Retorno do primeiro dígito: {digito1}')
	

		
	sair = retorno

	
	
	
	

	