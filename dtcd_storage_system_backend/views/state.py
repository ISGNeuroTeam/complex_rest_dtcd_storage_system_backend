from rest.views import APIView
from rest.response import SuccessResponse, status
from rest.permissions import AllowAny

from dtcd_storage_system_backend.system.state import State


class StateView(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post']

    def post(self, request):
        application_name = request.data.get("applicationName")
        workspace_id = request.data.get("workspaceID")
        state_body = request.data.get("state")

        state = State(application_name)
        state_id = state.save(workspace_id, state_body)

        return SuccessResponse(
            {"stateID": state_id},
            http_status=status.HTTP_200_OK
        )

    def get(self, request):
        application_name = request.GET.get("applicationName")
        state_id = request.GET.get("stateID")

        state = State(application_name)
        state_body = state.load(state_id)

        return SuccessResponse({
            "state": state_body
        },
            http_status=status.HTTP_200_OK
        )
