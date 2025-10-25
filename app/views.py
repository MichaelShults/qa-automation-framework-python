from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from .models import Foo
from .database import db



class FooView(ModelView):
    datamodel = SQLAInterface(Foo)
    list_columns = ["field"]


