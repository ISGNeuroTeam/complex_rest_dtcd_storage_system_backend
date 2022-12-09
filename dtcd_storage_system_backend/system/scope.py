from .models import ScopeModel
from .storage import Storage


class Scope(Storage):

    def __init__(self, application_name, scope_name):
        super().__init__(application_name=application_name, extra={"scope_name": scope_name}, model=ScopeModel)

