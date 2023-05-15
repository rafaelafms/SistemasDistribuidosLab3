# Servidor de calculadora usando RPyC
import rpyc
from rpyc.utils.server import ThreadedServer
import json

class Acao(rpyc.Service):
	def on_connect(self, conx):
		print("Conexao estabelecida.")
		self.dicionario = {}
		with open("entrada.json","r") as openfile:
			self.dicionario = json.load(openfile)
	def on_disconnect(self, conx):
		print("Conexao encerrada.")
		with open("entrada.json", "w") as outfile:
			json.dump(self.dicionario, outfile)
	def exposed_ler(self, chave):
		if chave in self.dicionario:
			valor = self.dicionario[chave]
			return valor
		return '[]'
	def exposed_escrever (self, chave, valor):
		if chave in self.dicionario:
			self.dicionario[chave].append(valor)
			self.dicionario[chave].sort()
			return 'Valor acrescentado a chave ja existente!'
		else:
			self.dicionario[chave] = (valor).split()
			return 'A nova chave e seu valor foram acrescentados!'
		print(self.dicionario)
	def exposed_remover(self, chave):
		if chave in self.dicionario:
			del self.dicionario[chave]
			return 'Chave excluida com sucesso!'
		else:
			return 'Chave inexistente!'

acao = ThreadedServer(Acao, port=10000)
acao.start()