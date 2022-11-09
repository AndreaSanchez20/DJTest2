from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from bookstore.models import Book

@api_view(['GET'])
def getRoutes(request):

#routes is made up of a list of dictionaries which will be converted to JS lists
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/projects/users/token'},
        {'POST': '/api/projects/users/token/refresh'},
    ]

    return Response(routes)
    #safe turns data into JSON data. 

@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    #pass serialized data. books data converted from python to json
    serializer= BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(id=pk)
    #pass serialized data. books data converted from python to json
    serializer= BookSerializer(book, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def bookVote(request,pk):
    book = Book.objects.get(id=pk)
    data = request.data
    print('DATA: ', data)

    serializer = BookSerializer(book, many=False)

    return Response(serializer.data)