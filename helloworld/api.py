from rest_framework.response import Response
from helloworld.serializers import UserInfoSerializer
from helloworld.utils import AuthenticatedAPIView
from .models import UserInfo


class UserInfoApiView(AuthenticatedAPIView):
    """
    Endpoint for the User info.
    /helloworld/v1/users_info

    Supports:
        HTTP GET: returns a list of all the users info.
    """
    def get(self, request):
        """
        returns the get_active_exams_for_user
        """
        users_info = UserInfo.get_all_users_info()
        result = []
        for user_info in users_info:
            # convert the django orm objects
            # into the serialized form.
            user_info_data = UserInfoSerializer(user_info).data

            result.append(user_info_data)

        return Response(result)
