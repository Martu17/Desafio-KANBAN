from app import models, columns

class Recibos(models.Model):
  _table = 'recibos' # nombre de la tabla en base de datos
  _description = 'Recibos de sueldo' # nombre del modelo en lenguaje humano

  # columnas de la tabla (la columna ID es implícita)
  _columns = {
    'anio_mes': columns.VarChar('Año/Mes'),
    'tipo_recibo': columns.VarChar('Tipo de recibo'),
    'cedula_funcionario': columns.Integer('Cedula del funcionario'),
    'nombre_empleador': columns.VarChar('Nombre del empleador'),
    'detalle_recibo_id': columns.Integer('Detalle recibo Id')
  }