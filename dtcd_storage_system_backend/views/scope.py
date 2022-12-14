import json

from rest.views import APIView
from rest.response import SuccessResponse, status
from rest.permissions import AllowAny

from dtcd_storage_system_backend.system.scope import Scope


class ScopeView(APIView):
    """
    Endpoint for Storage System Scope
    It is a persistent backend extension of a front end Storage System with a similar functionality.
    A storage is divided by applicationName and scopeName.
    """
    permission_classes = (AllowAny, )
    http_method_names = ['get', 'post']

    def post(self, request):
        """
        Add record to a storage
        :param request: JSON with "applicationName", "scopeName" and a record in `"key": key, "value": value` format
        :return: status of operation (200 or 500)
        """
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
        """
        Get record from a storage
        :param request: JSON with "applicationName", "scopeName" and "key" name.
        :return: JSON "value"
        """
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
