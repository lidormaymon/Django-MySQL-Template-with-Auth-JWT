from .seralizer import ProductSerializer
from .models import  Product
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_staff':user.is_staff
        # Add other user details you want to include
    }
    return Response(user_data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        #Adding custom data to token
        token['username'] = user.username
        token['email'] = user.email
        token['staff'] = user.is_staff 
        token['last_login'] = str(user.last_login)
        token['super_user'] = user.is_superuser
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['date_joined'] = str(user.date_joined)
        return token

class MyTokenObtainPairView11(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register(request):
    user = User.objects.create_user(username= request.data["username"],password=request.data['password'],email = request.data["email"], is_staff=0,is_superuser=0)
    return Response({"reg":"success"})



class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            response.data['message'] = 'Login successful.'
        else:
            response.data['message'] = 'Invalid login credentials.'
        return response

# # <---------------------------------------------------------------Products Entry Points --------------------------------------->
# class ProductViewSet(APIView):
#     def get(self, request, pk=None):
#         if pk is not None:
#             my_model = Product.objects.get(pk=pk)
#             serializer = ProductSerializer(my_model)
#         else:
#             my_model = Product.objects.all()
#             serializer = ProductSerializer(my_model, many=True)
    
#         return Response(serializer.data)


#     def post(self, request):
#         serializer = ProductSerializer(data=request.data, context={'user': request.user})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#     def put(self, request, pk):
#         my_model = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(my_model, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

#     def delete(self, request, pk):
#         my_model = Product.objects.get(pk=pk)
#         my_model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


# # <------------------------------- IMAGES -------------------------------------------->

# //////////// image upload / display
# return all images to client (without serialize)
@api_view(['GET'])
def getImages(request):
    res=[] #create an empty list
    for img in Product.objects.all(): #run on every row in the table...
        res.append({

               "image":str( img.image)
                }) #append row by to row to res list
    return Response(res) #return array as json response


# upload image method (with serialize)
class APIViews(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthenticated,) 
    def post(self, request, *args, **kwargs):
        api_serializer = ProductSerializer(data=request.data)
       
        if api_serializer.is_valid():
            api_serializer.save()
            return Response(api_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', api_serializer.errors)
            return Response(api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# //////////// end      image upload / display
