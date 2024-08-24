from typing import Any, Dict
import inspect

from .models import Model, load_database, update_database
import models

class Environment:
  _models: Dict[str, Model] = {}

  def __init__(self) -> None:
    db = load_database()
    for i, module_ in inspect.getmembers(models, predicate=inspect.ismodule):
       for i, model_ in inspect.getmembers(module_, predicate=inspect.isclass):
        self._models[model_._table] = model_
        if not db.get(model_._table):
          db[model_._table] = []
    update_database(db)

  def __getitem__(self, name: str) -> Any:
    return self._models[name]
