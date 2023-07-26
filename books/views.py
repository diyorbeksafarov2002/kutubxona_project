from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from  .serializers import BookSerializer
from .models import Book


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):
    def get(self,request):
        # Retrieve all books from the database
        books = Book.objects.all()

        # Serialize the books data
        serializer = BookSerializer(books, many=True)

        # Return the serialized data as the response
        return Response(serializer.data)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer_data = BookSerializer(book).data
        data = {
            'status':'Muvafiqqiyatli',
            'book':serializer_data
        }
        return Response(data)


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer






# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)


        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookCreateListApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


