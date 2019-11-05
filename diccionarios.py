#diccionarios {'llave' : 'valor'}
alumno={'num_cta':'201647757473',
        'nombre': ('José', 'Perez', 'García'),
        'semestre': '1',
        'promedio':'0.0',
        'materias':['CyP','Álgebra','Cálculo','Geometría','IntroICO'],
        'regular':True ,
        'lagrimas_por_examen': 5,
        'dirección':{
                'calle':'Rancho Sequito',
                'colonia':'Impulsora Popular Avícola',
                'número':1000,
                'cp': 17570,
                'del_mun':'Nezahualcoyotl',
                'estado': {
                    'nombre': 'Estado de México',
                    'corto':'EdoMex',
                    'id':15
                    }
                }
        }
print(alumno['materias'][1].upper())
alumno['lagrimas_por_examen'] = 10
print(alumno)
alumno['cursa_inglés']= True
print(alumno)
"""
print(alumno['nombre'])
print(alumno)
print(alumno['nombre'][1])
print(alumno['dirección']['cp'])
print(alumno['dirección']['estado']['corto'])
print(alumno['materias'][3::])
print(alumno['dirección']['estado']['nombre'][10::].upper())

mi_lista=[['a','b'],['c',10],['d',True]]
diccionario = dict(mi_lista)
print(diccionario)
"""
# Son mutables
alumno['cursa_inglés']= True
print(alumno)

# funcion key()
llaves = alumno.keys()
print(llaves)
for llave in llaves:
    print("-------")
    print(llave)
    print('...........')
    print(alumno[llave])
    print("++++++++")
#~funcion values
    for val in alumno.values():
        print('......')
        print(val)
        print('+++++++++')

# funcion items ()
for elem in alumno.items():
    print('.....')
    print(elem)
    print('+++++++')
    
