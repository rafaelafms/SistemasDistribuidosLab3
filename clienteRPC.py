# Cliente de calculadora usando RPyC
import rpyc

dic = rpyc.connect('localhost', 10000)
while True:
	acao = input("Digite uma acao('ler', 'escrever', 'remover' ou 'fim' para terminar): ")
	if acao == 'fim':
		dic.close()
		break
	chave = input("Digite a chave: ")
	if acao == 'ler':
		resultado = dic.root.ler(chave)
	elif acao == 'escrever':
		valor = input("Digite o valor: ")
		resultado = dic.root.escrever(chave, valor)
	elif acao == 'remover':
		resultado = dic.root.remover(chave)
	print(resultado)