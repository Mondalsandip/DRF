from django.shortcuts import render
from .models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import   ReviewOrReadOnly


   
class StreamPlatformAV(APIView):
    permission_classes = [ReviewOrReadOnly]
    
    
    def get(self,request):
        stream=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(stream, many=True,context={'request': request})
        self.check_object_permissions(request, stream)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
class StreamPlatformDetailsAV(APIView):
    permission_classes = [ReviewOrReadOnly]

    def get(self,request,pk):
        try:
            stream=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'message':'Resource doesnot exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer=StreamPlatformSerializer(stream)
        self.check_object_permissions(request, stream)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    def put(self, request,pk):
        try:
            stream=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'message':'Resource doesnot Exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer=StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        stream=StreamPlatform.objects.get(pk=pk)
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class WatchListAV(APIView):
    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
            
class WatchDetailsAV(APIView):
    def get(self, request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Message':'Doesnt exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'message':'Movie does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
 


















# Create your views here.
# def movie_list(request):
#     movies=Movie.objects.all()
#     print(movies.values())
#     data={'movies': list(movies.values())}
#     print(data)
#     return JsonResponse(data)

# def movie_details(request,pk):
#     movie=Movie.objects.get(pk=pk)
#     print('movie: ',movie)



# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method =='GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies, many=True)
#         print('ser: ',  dir(serializer)  )
#         return Response(serializer.data)
#     if request.method == 'POST':
#         print('request  :', request)
#         print('request-data  :', request.data)
#         print('request-data  :', type(request.data))
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        


# @api_view(['GET','PUT','DELETE','PATCH'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Message':'Movie doesnt exists'}, status=status.HTTP_404_NOT_FOUND)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response({'message':'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    


    
    
    