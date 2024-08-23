from app import models, columns

class Car(models.Model):
  _table = 'car_car' # nombre de la tabla en base de datos
  _description = 'Auto' # nombre del modelo en lenguaje humano

  # columnas de la tabla (la columna ID es implícita)
  _columns = {
    'brand': columns.VarChar('Marca'),
    'color': columns.VarChar('Color'),
    'open_ceiling': columns.Boolean('Techo abierto'),
    'seats_count': columns.Integer('# asientos', minval=1, default=2)
  }
