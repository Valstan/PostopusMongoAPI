from bson import json_util
from flask_restful import Resource, abort
import json
from utils.get_mongo_base import nagrada_base


class Field(Resource):

    def get(self, collection_name, table_name, field_name):
        collection = nagrada_base[collection_name]
        table = collection.find_one({'title': table_name})
        if not table:
            abort(404, message=f"Нет коллекции - {str(collection_name)} или нет таблицы - {str(table_name)}")
        try:
            return json.dumps(table[field_name], sort_keys=True, indent=4, default=json_util.default)
        except Exception as exc:
            return f"В таблице - {str(table_name)} нет поля {str(field_name)}, ошибка - {exc}"
