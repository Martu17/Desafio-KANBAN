import app

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
print(app.env['car_seat'].records())