import app
import csv

Funcionarios = app.env['funcionarios']
funcionarios = []

# Leer los datos de funcionarios del archivo .csv y los guarda en el database.json
with open('/Users/martu/Desafio-KANBAN/python/datos/Funcionarios.csv', mode='r', newline='') as file:
    datos_funcionarios = csv.reader(file, delimiter=',')
    for row in datos_funcionarios:
        funcionario = Funcionarios.create({
            'cedula': int(row[0]),
            'nombre': row[1],
            'cargo': row[2],
            'sueldo': int(row[3]),
            'fecha_ingreso': row[4]
        })
        funcionarios.append(funcionario)

# Imprime los funcionarios creados
print(funcionarios)

Detalle = app.env['detalle_recibos']
detalle_recibos = []
# Leer los datos del detalle de los recibos del archivo .csv y los guarda en el database.json
with open('/Users/martu/Desafio-KANBAN/python/datos/Detalle recibos.csv', mode='r', newline='') as file:
    datos_detalle = csv.reader(file, delimiter=',')
    for row in datos_detalle:
        detalle = Detalle.create({
            'tipo_concepto': row[0],
            'cantidad': row[1],
            'monto': int(row[2])
        })
        detalle_id = detalle.id
        detalle_recibos.append(detalle)
    

# Imprime los funcionarios creados
print(detalle_recibos)

Recibos = app.env['recibos']
recibos = []
# Leer los datos de recibos del archivo .csv y los guarda en el database.json
with open('/Users/martu/Desafio-KANBAN/python/datos/Recibos.csv', mode='r', newline='') as file:
    datos_recibos = csv.reader(file, delimiter=',')
    for row in datos_recibos:
        recibo = Recibos.create({
            'anio_mes': row[0],
            'tipo_recibo': row[1],
            'cedula_funcionario': int(row[2]),
            'nombre_empleador': row[3],
            'detalle_recibo_id': row[4]
        })
        recibos.append(recibo)

# Imprime los funcionarios creados
print(recibos)

# Eliminar un recibo de sueldo de un funcionario a partir de su cedula

print("Ingrese la cedula del funcionario para eliminar su recibo")
cedula_eliminar = int(input())

for recibo in Recibos.records():
  if cedula_eliminar == recibo.cedula_funcionario:
    recibo.delete()
print(f"Se han eliminado los recibos para la cedula {cedula_eliminar}")

# Modificar el nombre y cargo de un funcionario a partir de su cédula
print("Ingrese la cedula del funcionario que desea modificar")
cedula_modificar = int(input())

funcionario_a_modificar = None

for funcionario in Funcionarios.records():
  if cedula_modificar == funcionario.cedula:
    funcionario_a_modificar = funcionario
    
if funcionario_a_modificar:
  print("Ingrese el nuevo nombre del funcionario")
  nuevo_nombre = input()
  
  print("Ingrese el nuevo cargo del funcionario")
  nuevo_cargo = input()
  
  funcionario_a_modificar.update({'nombre':nuevo_nombre, 'cargo':nuevo_cargo})
  
  print(f"Se han actualizado los datos del funcionario con cedula {cedula_modificar}")