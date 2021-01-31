from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from core.models import Message

class CrushAPIView(APIView):
    '''
    Congrats, Now I know that you read my texts :).  
    '''


    def get(self, request, *args, **kwargs):
        try:
            msg = "Congrats, Now I know that you read my texts :)"
            obj = Message(msg = msg)
            obj.save()
            return Response({
                    'status': True,
                    'msg': msg}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False,
                             'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)      