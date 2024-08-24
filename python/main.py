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



'''import app

print('\napp.env almacena el entorno de la aplicacion, desde donde se puede acceder a la definición de los modelos de la siguiente forma:')
Car = app.env['car_car']
print(Car)

print('\nEl método create recibe un diccionario de valores y retorna una instancia del modelo para el registro que acaba de crear:')
car = Car.create({'color': 'Rojo', 'brand': 'Hyundai'})
print(car)
print(car.seats_count)

seats = []
print(seats)
for i in range(1, 5):
  seats.append(app.env['car_seat'].create({'car_id': car.id}))
  print(seats)

print('\nSe puede acceder a las columnas de un modelo como atributos e incluso actualizarlas:')
car.seats_count = len(seats)
print(car.seats_count)

print('\nEl método records retorna todos los registros existentes para el modelo indicado como una lista de instancias:')
all_seats = app.env['car_seat'].records()
print(all_seats)

print('\nEl método read retorna los valores de todas las columnas de un registro como un diccionario:')
for seat in all_seats:
  print(seat.read())

print('\nEl método browse retorna el regsitro del modelo según el ID recibido - también puede recibir lista de IDs, en cuyo caso retorna una lista de registros:')
car_again = Car.browse(all_seats[0].car_id.id)
print(car_again)
print(car.read() == car_again.read())
del car_again

print('\nEl método update recibe un diccionario de valores y actualiza las columnas del registro con los nuevos valores:')
print(car.read())
car.update({'color': 'Azul', 'open_ceiling': True})
print(car.read())

print('\nEl método delete elimina el registro en base de datos:')
for seat in all_seats:
  seat.delete()
car.delete()
print(Car.records())
print(app.env['car_seat'].records())'''