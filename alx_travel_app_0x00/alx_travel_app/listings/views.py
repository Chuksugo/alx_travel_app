from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def test_view(request):
    return Response({"message": "Hello from listings!"})
