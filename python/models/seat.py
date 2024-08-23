from app import models, columns
from . import car

class Seat(models.Model):
  _table = 'car_seat' # nombre de la tabla en base de datos
  _description = 'Asiento' # nombre del modelo en lenguaje humano

  # columnas de la tabla (la columna ID es implícita)
  _columns = {
    'material': columns.VarChar('Material', default='Cuero'),
    'headrest': columns.Boolean('Respado para cabeza', default=True),
    'car_id': columns.Relation('Auto', car.Car)
  }