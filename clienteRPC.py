# Cliente dicionario usando RPyC
import rpyc
import json

def lerDicionario():
	with open("entrada.json","r") as openfile:
		atual = json.load(openfile)
	return atual

def escreverDicionario(dicionario):
	with open("entrada.json", "w") as outfile:
		json.dump(dicionario, outfile)
	return 

dic = rpyc.connect('localhost', 10000, config={'allow_public_attrs': True, 'sync_request_timeout': 10})
while True:
	acao = input("Digite uma acao('ler', 'escrever', 'remover', 'salvar' ou 'fim' para terminar): ")
	if acao == 'fim':
		dic.close()
		break
	dicionario = lerDicionario()
	if acao == 'ler':
		chave = input("Digite a chave: ")
		resultado = dic.root.ler(chave, dicionario)
	elif acao == 'escrever':
		chave = input("Digite a chave: ")
		valor = input("Digite o valor: ")
		resultado = dic.root.escrever(chave, valor, dicionario)
		escreverDicionario(dicionario)
	elif acao == 'remover':
		chave = input("Digite a chave: ")
		resultado = dic.root.remover(chave, dicionario)
		escreverDicionario(dicionario)
	elif acao == 'salvar':
		escreverDicionario(dicionario)
		resultado = 'Dicionario salvo!'
	else:
		resultado = 'Acao invalida!'
	print(resultado)
