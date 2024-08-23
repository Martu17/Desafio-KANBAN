from app import models, columns

class Detalle(models.Model):
  _table = 'detalle_recibos' # nombre de la tabla en base de datos
  _description = 'Detalles de los recibos' # nombre del modelo en lenguaje humano

  # columnas de la tabla (la columna ID es implícita)
  _columns = {
    'id': columns.Integer('Id'),
    'tipo_concepto': columns.VarChar('Tipo de concepto'),
    'cantidad': columns.VarChar('Cantidad'),
    'monto': columns.Integer('Monto')
  }