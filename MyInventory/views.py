from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from datetime import datetime,timedelta, timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print("MY TOKEN :",token)
        print('in myinv')
        return Response({
            'msg': 'suc____________________k',
            'token': token.key,
            'userId': user.pk,
            'email': user.email,
            'role':user.roleId.roleName
        })
