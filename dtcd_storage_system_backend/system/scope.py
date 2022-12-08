from .models import ScopeModel
from .storage import Storage


class Scope(Storage):

    def __init__(self):
        super().__init__(model=ScopeModel)

