from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import APIView

from imageclassification.ml_model import predictClassLabel

# Create your views here.

#later on create a class named api and override all the get, put, post, patch method and make functions in the class

class BirdStatusAPIView(APIView):
    
    def get(self, request):
        birds_object = BirdsStatus.objects.all()
        serializer = BirdsStatusSerializer(birds_object, many=True)
        return Response({'message': serializer.data})
    
    def post(self, request):
        serializer = BirdsStatusSerializer(data=request.data)
    
    
    
        if not serializer.is_valid():
            return Response({'status':400,'error':serializer.errors})
        serializer.save()
        print("Saved Data sucessfully") 
        return Response({'status':200,'payload':serializer.data})
    
    
    def patch(self, request):
        pass
    
    
    def delete(self, request):
        pass
    
    
    def put(Self, request):
        pass
    

class BirdsDetailAPIView(APIView):
    
    def get(self, request):
        birds_objects = BirdsDetail.objects.all()
        serializer = BirdsDetailSerializer(birds_objects, many=True)
        return Response({'message': serializer.data})
    
    def post(self, request):
        serializer = BirdsDetailSerializer(data=request.data)
        if not serializer.is_valid():
            
            print("Not a valid serializer")
            return Response({'status': 400, 'error': serializer.errors})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data})
    
    def patch(self, request):
        pass
    
    def delete(self, request):
        pass
    
    def put(self, request):
        pass


class NodeDeviceAPIView(APIView):
    
    def get(self, request):
        return Response({'message': "Connection Established Successfully"})
    
    def post(self, request):
        try:
            image = request.FILES['image']
            
            if image:
                predicted_class_label = predictClassLabel(image)
                bird_detail = get_object_or_404(BirdsDetail, scientific_name=predicted_class_label)
                # Fetch status details
                status_detail = get_object_or_404(BirdsStatus, status_code=bird_detail.status_code.status_code)
                status_code=status_detail.status_code
                status_name=status_detail.status_name
                data = {
                    'status_code':status_code,
                    'status_name':status_name,
                    'common_name': bird_detail.common_name,
                    'scientific_name': bird_detail.scientific_name,
                    'birds_description': bird_detail.birds_description
                }
                
                return Response(data)

            # Use the following code to filter and fetch individual node data from the database
            # Also to fetch individual sightings, filtering out the sightings for individual birds
            #
            # serializer = NodeDeviceSerializer(data=request.data)
            # if not serializer.is_valid():
            #     print("Not a valid serializer")
            #     return Response({'status': 400, 'error': serializer.errors})
            # serializer.save()

            return Response({'status': 400, 'message': 'Invalid File Provided'})
        
        except Exception as e:
            # Handle specific exceptions if needed, or log the general exception
            print(f"An error occurred: {str(e)}")
            return Response({'status': 500, 'error': 'Internal Server Error'})

        
    







# @api_view(['GET'])
# def testFun(request):
#     birds_object = Birds.objects.all()
#     serializer = BirdsSerializer(birds_object, many=True)
#     return Response({'message': serializer.data})

# @api_view(['POST'])
# def post_bird_image(request):
#     data = request.data
#     serializer = BirdsSerializer(data=request.data)
    
    
    
#     if not serializer.is_valid():
#          return Response({'status':400,'error':serializer.errors})
#     serializer.save()
    
#     return Response({'status':200,'payload':serializer.data})

# @api_view(['PUT'])
# def update_bird_image(request, id):
#     try:
#         bird_obj = Birds.objects.get(id=id)
#         serializer = BirdsSerializer(bird_obj, data = request.data, partial=True)
#         if not serializer.is_valid():
#             return Response({'status':400,'error':serializer.errors})
     
#         serializer.save()
    
#         return Response({'status':200,'payload':serializer.data})
#     except Exception as e:
         
#          return Response({'status':403,'message':"Invalid ID"})
        
    
# @api_view(['DELETE'])
# def delete_bird_image(request, id):
#     try:
#         bird_obj = Birds.objects.get(id=id)  
#         bird_obj.delete()
#         return Response({'status':000,'message':"Deleted sucessfully"})
#     except Exception as e:
         
#          return Response({'status':403,'message':"Invalid ID"})   
    