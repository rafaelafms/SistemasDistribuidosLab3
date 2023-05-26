# Servidor dicionario usando RPyC
import rpyc
from rpyc.utils.server import ThreadedServer
import json

class Acao(rpyc.Service):
	def on_connect(self, conx):
		print("Conexao estabelecida.")
		self.dicionario = {}
	def on_disconnect(self, conx):
		print("Conexao encerrada.")
	def exposed_salvar(self, dicionario):
		with open("entrada.json", "w") as outfile:
			json.dump(dicionario, outfile)
		return 'Dicionario salvo'
	def exposed_ler(self, chave, dicionario):
		if chave in dicionario:
			valor = dicionario[chave]
			return valor
		return '[]'
	def exposed_escrever (self, chave, valor, dicionario):
		if chave in dicionario:
			dicionario[chave].append(valor)
			dicionario[chave].sort()
			return 'Valor acrescentado a chave ja existente!'
		else:
			dicionario[chave] = valor.split()
			return 'A nova chave e seu valor foram acrescentados!' 
	def exposed_remover(self, chave, dicionario):
		if chave in dicionario:
			del dicionario[chave]
			return 'Chave excluida com sucesso!'
		else:
			return 'Chave inexistente!'

acao = ThreadedServer(Acao, port=10000, protocol_config={'allow_public_attrs': True, 'sync_request_timeout': 10})
acao.start()
