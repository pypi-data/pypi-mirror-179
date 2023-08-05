from SuperSimpleGameHacker.English import Write_Read_Memory, Inject_Dll



from SuperSimpleGameHacker.Portugues import Escrever_e_Ler_Memoria, Injectar_Dll



from pymem import *																										
from pymem.process import *																								



Processo = pymem.Pymem("Jogo.exe")



Process = pymem.Pymem("Jogo.exe")



Tipo, Type: "char ,short, int, float, long ,longlong, double"



Write_Read_Memory(Process, 0xAddress, [0xOffset, 0xOffset, 0xOffset], "Type", Write: True ou False, Value is for use if you will write or None is for use if you will not write, ".dll and .exe")

Inject_Dll(Process, Dll Path)


Escrever_e_Ler_Memoria(Processo, 0xEnderço, [0xOffset, 0xOffset, 0xOffset], "tipo", Valor é para usar se vai escrever ou Nada é para usar se não vai escrever", ".dll ou .exe")

Injectar_Dll(Processo, Caminho do Dll)