import json
from typing import List, Dict, Any
from .columns import Column

def load_database():
  database = json.load(open('app\database.json'))
  for model in database:
    database[model].sort(key=lambda record: record['id'])
  return database

def update_database(new: dict):
  with open('app\database.json', 'w') as database:
    json.dump(new, database)

class Model:
  _table: str
  _description: str
  _columns: Dict[str, Column] = {}

  _prevent_setattr_db_update = False

  id: int = False

  def __int__(self) -> int:
    return self.id or -1

  def __repr__(self) -> str:
    return '%s(%s)'%(self._table, self.id)

  def __getattribute__(self, name: str):
    value = super().__getattribute__(name)
    if name != '_columns' and name in self._columns.keys():
      return self._columns[name].return_parsed_value(value)
    return value

  def __setattr__(self, name: str, value: Any):
    if name in self._columns.keys():
      self._columns[name].validate_value(value)
      if self.id and not self._prevent_setattr_db_update:
        db = load_database()
        i = db[self._table].index(self.read())
        db[self._table][i][name] = value
        update_database(db)
    return super().__setattr__(name, value)

  def __delattr__(self, name: str):
    if name in self._columns.keys():
      raise Exception('deletion of column not allowed')
    return super().__delattr__(name)

  @classmethod
  def create(self, values: Dict[str, Any]={}):
    db = load_database()
    record = self()
    for colname, coldefinition in self._columns.items():
      if colname in values.keys():
        value = values[colname]
      else:
        value = coldefinition.default
      setattr(self, colname, value)
    record.id = db[self._table][-1]['id']+1 if db[self._table] else 1
    db[self._table].append(record.read())
    update_database(db)
    return record

  def read(self, columns: List[str]=[]):
    return {colname:self._columns[colname]._type(getattr(self, colname)) if self._columns.get(colname) else getattr(self, colname) for colname in (columns or list(self._columns.keys()))+['id']}

  def update(self, values: Dict[str, Any]={}):
    if self.id:
      self._prevent_setattr_db_update = True
      db = load_database()
      i = db[self._table].index(self.read())
      for name, value in values.items():
        self._columns[name].validate_value(value)
        db[self._table][i][name] = value
        setattr(self, name, value)
      update_database(db)
      self._prevent_setattr_db_update = False

  def delete(self):
    db = load_database()
    db[self._table].remove(self.read())
    update_database(db)
    self.id = False
    for colname, coldefinition in self._columns.items():
      setattr(self, colname, None)

  @classmethod
  def browse(self, recids: int | List[int] = []):
    if not recids:
      return self
    db = load_database()
    if not isinstance(recids, list):
      recids = [recids]
    records = []
    for data in list(filter(lambda record: record['id'] in recids, db[self._table])):
      record = self()
      record._prevent_setattr_db_update = True
      for colname, value in data.items():
        setattr(record, colname, value)
      record._prevent_setattr_db_update = False
      records.append(record)
    if len(records) == 0:
      return None
    elif len(records) == 1:
      return records[0]
    else:
      return records

  @classmethod
  def records(self):
    db = load_database()
    records = []
    for data in db[self._table]:
      record = self()
      record._prevent_setattr_db_update = True
      for colname, value in data.items():
        setattr(record, colname, value)
      record._prevent_setattr_db_update = False
      records.append(record)
    return records
