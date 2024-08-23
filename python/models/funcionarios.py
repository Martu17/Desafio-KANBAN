from app import models, columns

class Funcionarios(models.Model):
  _table = 'funcionarios' # nombre de la tabla en base de datos
  _description = 'Funcionarios' # nombre del modelo en lenguaje humano

  # columnas de la tabla (la columna ID es implícita)
  _columns = {
    'cedula': columns.Integer('Cedula'),
    'nombre': columns.VarChar('Nombre'),
    'cargo': columns.VarChar('Cargo'),
    'sueldo': columns.Integer('Sueldo'),
    'fecha_ingreso': columns.VarChar('Fecha Ingreso')
  }
