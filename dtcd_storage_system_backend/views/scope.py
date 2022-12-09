import json

from rest.views import APIView
from rest.response import SuccessResponse, status
from rest.permissions import AllowAny

from dtcd_storage_system_backend.system.scope import Scope


class ScopeView(APIView):
    permission_classes = (AllowAny, )
    http_method_names = ['get', 'post']

    def post(self, request):
        application_name = request.data.get("applicationName")
        scope_name = request.data.get("scopeName")
        # record = {"key": key, "value": value}
        record = request.data.get("record")
        scope = Scope(application_name, scope_name)
        scope.add_record(record)

        return SuccessResponse(
            http_status=status.HTTP_200_OK
        )

    def get(self, request):

        application_name = request.GET.get("applicationName")
        scope_name = request.GET.get("scopeName")
        key = request.GET.get("key")
        scope = Scope(application_name, scope_name)
        record = scope.get_record({"key": key})

        return SuccessResponse({
            "value": record.value
        },
                    http_status=status.HTTP_200_OK
        )
