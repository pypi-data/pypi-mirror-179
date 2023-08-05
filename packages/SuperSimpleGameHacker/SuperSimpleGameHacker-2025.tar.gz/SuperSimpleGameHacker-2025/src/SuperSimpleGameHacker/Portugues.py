from concurrent.futures import process
from pymem import *
from struct import calcsize 

"""

from MemoryApi import Escrever_e_Ler_Memoria
char ,short, int, float, long ,longlong, double
Escrever_e_Ler_Memoria(pymem, 0xAddress, [0xOffset, 0xOffset, 0xOffset], "tipo", Escrever True ou False, valor ou "Nada", "Nome_do_dll")

"""

def Gerar_Ponto_De_Enderco(Base, compensacoes, Nome_do_pymem, Corrigir):
	checar_o_sistema = calcsize("P")*8
	
	if checar_o_sistema == 32:
		if Corrigir == "Nada":
		    enderco = Nome_do_pymem.read_longlong(Base)
		    for compensar in compensacoes:
		        if compensar != compensacoes[-1]:
		            enderco = Nome_do_pymem.read_longlong(enderco + compensar)
		    enderco = enderco + compensacoes[-1]
		    return enderco
	else:
		if Corrigir:
			enderco = Nome_do_pymem.read_longlong(Base + Corrigir)
			for compensar in compensacoes:
				if compensar != compensacoes[-1]:
					enderco = nome_do_pymem.read_longlong(enderco + compensar)
			enderco = enderco + compensacoes[-1]
			return enderco



def Escrever_e_Ler_Memoria(nome_do_pymem, enderco, compensacoes, tipo, escrever, valor, nome_do_dll):
	Base = module_from_name(nome_do_pymem.process_handle, nome_do_dll).lpBaseOfDll
	checar_o_sistema = calcsize("P")*8

	if escrever == False:
		if valor == "Nada":
			if checar_o_sistema == 32:
				if tipo == "char":
					ValorAntigo_Char = nome_do_pymem.read_char(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"))
					return ValorAntigo_Char


				elif tipo == "short":
					ValorAntigo_Short = nome_do_pymem.read_short(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"))
					return ValorAntigo_Short


				elif tipo == "int":
					ValorAntigo_Int = nome_do_pymem.read_int(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"))
					return ValorAntigo_Int


				elif tipo == "float":
					ValorAntigo_Float = nome_do_pymem.read_float(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"))
					return ValorAntigo_Float


				elif tipo == "long":
					ValorAntigo_Long = nome_do_pymem.read_long(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"))
					return ValorAntigo_Long


				elif tipo == "longlong":
					ValorAntigo_LongLong = nome_do_pymem.read_longlong(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"))
					return ValorAntigo_LongLong


				elif tipo == "double":
					ValorAntigo_Double = nome_do_pymem.read_Double(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"))
					return ValorAntigo_Double



			else:
				if tipo == "char":
					ValorAntigo_Char = nome_do_pymem.read_char(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco))
					return ValorAntigo_Char


				elif tipo == "short":
					ValorAntigo_Short = nome_do_pymem.read_short(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco))
					return ValorAntigo_Short


				elif tipo == "int":
					ValorAntigo_Int = nome_do_pymem.read_int(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco))
					return ValorAntigo_Int


				elif tipo == "float":
					ValorAntigo_Float = nome_do_pymem.read_float(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco))
					return ValorAntigo_Float


				elif tipo == "long":
					ValorAntigo_Long = nome_do_pymem.read_long(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco))
					return ValorAntigo_Long


				elif tipo == "longlong":
					ValorAntigo_LongLong = nome_do_pymem.read_longlong(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco))
					return ValorAntigo_LongLong


				elif tipo == "double":
					ValorAntigo_Double = nome_do_pymem.read_Double(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco))
					return ValorAntigo_Double



	else:
		if valor:
			if checar_o_sistema == 32:
				if tipo == "char":
					nome_do_pymem.write_char(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"), valor)

				elif tipo == "short":
					nome_do_pymem.write_short(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"), valor)


				elif tipo == "int":
					nome_do_pymem.write_int(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"), valor)


				elif tipo == "float":
					nome_do_pymem.write_float(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"), valor)


				elif tipo == "long":
					nome_do_pymem.write_long(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"), valor)


				elif tipo == "longlong":
					nome_do_pymem.write_long(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"), valor)


				elif tipo == "double":
					nome_do_pymem.write_double(Gerar_Ponto_De_Enderco(Base + enderco, compensacoes, nome_do_pymem, "Nada"), valor)



			else:
				if tipo == "char":
					nome_do_pymem.write_char(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco), valor)

				elif tipo == "short":
					nome_do_pymem.write_short(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco), valor)


				elif tipo == "int":
					nome_do_pymem.write_int(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco), valor)


				elif tipo == "float":
					nome_do_pymem.write_float(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco), valor)


				elif tipo == "long":
					nome_do_pymem.write_long(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco), valor)


				elif tipo == "longlong":
					nome_do_pymem.write_long(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco), valor)


				elif tipo == "double":
					nome_do_pymem.write_double(Gerar_Ponto_De_Enderco(Base, compensacoes, nome_do_pymem, enderco), valor)

def Injetar_Dll(nome_do_pymem, caminho_do_dll):
	caminho_do_dll_bytes = bytes(caminho_do_dll, "UTF-8")
	process.inject_dll(nome_do_pymem.process_handle, caminho_do_dll_bytes)
