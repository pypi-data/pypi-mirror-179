from concurrent.futures import process
from pymem import *
from struct import calcsize 

def Generate_address_point(Base, offsets, name_pymem, Fix):
	Check_system = calcsize("P")*8
	
	if Check_system == 32:
		if Fix == "None":
		    address = name_pymem.read_longlong(Base)
		    for offset in offsets:
		        if offset != offsets[-1]:
		            address = name_pymem.read_longlong(address + offset)
		    address = address + offsets[-1]
		    return address
	else:
		if Fix:
			address = name_pymem.read_longlong(Base + Fix)
			for offset in offsets:
				if offset != offsets[-1]:
					address = name_pymem.read_longlong(address + offset)
			address = address + offsets[-1]
			return address



def Write_Read_Memory(name_pymem, address, offsets, type, write, value, nome_do_dll):
	Base = module_from_name(name_pymem.process_handle, nome_do_dll).lpBaseOfDll
	Check_system = calcsize("P")*8

	if write == False:
		if value == "None":
			if Check_system == 32:
				if type == "char":
					ValueOld_Char = name_pymem.read_char(Generate_address_point(Base + address, offsets, name_pymem, "None"))
					return ValueOld_Char


				elif type == "short":
					ValueOld_Short = name_pymem.read_short(Generate_address_point(Base + address, offsets, name_pymem, "None"))
					return ValueOld_Short


				elif type == "int":
					ValueOld_Int = name_pymem.read_int(Generate_address_point(Base + address, offsets, name_pymem, "None"))
					return ValueOld_Int


				elif type == "float":
					ValueOld_Float = name_pymem.read_float(Generate_address_point(Base + address, offsets, name_pymem, "None"))
					return ValueOld_Float


				elif type == "long":
					ValueOld_Long = name_pymem.read_long(Generate_address_point(Base + address, offsets, name_pymem, "None"))
					return ValueOld_Long


				elif type == "longlong":
					ValueOld_LongLong = name_pymem.read_longlong(Generate_address_point(Base + address, offsets, name_pymem, "None"))
					return ValueOld_LongLong


				elif type == "double":
					ValueOld_Double = name_pymem.read_Double(Generate_address_point(Base + address, offsets, name_pymem, "None"))
					return ValueOld_Double



			else:
				if type == "char":
					ValueOld_Char = name_pymem.read_char(Generate_address_point(Base, offsets, name_pymem, address))
					return ValueOld_Char


				elif type == "short":
					ValueOld_Short = name_pymem.read_short(Generate_address_point(Base, offsets, name_pymem, address))
					return ValueOld_Short


				elif type == "int":
					ValueOld_Int = name_pymem.read_int(Generate_address_point(Base, offsets, name_pymem, address))
					return ValueOld_Int


				elif type == "float":
					ValueOld_Float = name_pymem.read_float(Generate_address_point(Base, offsets, name_pymem, address))
					return ValueOld_Float


				elif type == "long":
					ValueOld_Long = name_pymem.read_long(Generate_address_point(Base, offsets, name_pymem, address))
					return ValueOld_Long


				elif type == "longlong":
					ValueOld_LongLong = name_pymem.read_longlong(Generate_address_point(Base, offsets, name_pymem, address))
					return ValueOld_LongLong


				elif type == "double":
					ValueOld_Double = name_pymem.read_Double(Generate_address_point(Base, offsets, name_pymem, address))
					return ValueOld_Double



	else:
		if value:
			if Check_system == 32:
				if type == "char":
					name_pymem.write_char(Generate_address_point(Base + address, offsets, name_pymem, "None"), value)

				elif type == "short":
					name_pymem.write_short(Generate_address_point(Base + address, offsets, name_pymem, "None"), value)


				elif type == "int":
					name_pymem.write_int(Generate_address_point(Base + address, offsets, name_pymem, "None"), value)


				elif type == "float":
					name_pymem.write_float(Generate_address_point(Base + address, offsets, name_pymem, "None"), value)


				elif type == "long":
					name_pymem.write_long(Generate_address_point(Base + address, offsets, name_pymem, "None"), value)


				elif type == "longlong":
					name_pymem.write_long(Generate_address_point(Base + address, offsets, name_pymem, "None"), value)


				elif type == "double":
					name_pymem.write_double(Generate_address_point(Base + address, offsets, name_pymem, "None"), value)



			else:
				if type == "char":
					name_pymem.write_char(Generate_address_point(Base, offsets, name_pymem, address), value)

				elif type == "short":
					name_pymem.write_short(Generate_address_point(Base, offsets, name_pymem, address), value)


				elif type == "int":
					name_pymem.write_int(Generate_address_point(Base, offsets, name_pymem, address), value)


				elif type == "float":
					name_pymem.write_float(Generate_address_point(Base, offsets, name_pymem, address), value)


				elif type == "long":
					name_pymem.write_long(Generate_address_point(Base, offsets, name_pymem, address), value)


				elif type == "longlong":
					name_pymem.write_long(Generate_address_point(Base, offsets, name_pymem, address), value)


				elif type == "double":
					name_pymem.write_double(Generate_address_point(Base, offsets, name_pymem, address), value)

def Inject_Dll(name_pymem, dll_path):
	dll_path_bytes = bytes(dll_path, "UTF-8")
	process.inject_dll(name_pymem.process_handle, dll_path_bytes)