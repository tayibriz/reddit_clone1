from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Community
from .serializers import CommunitySerializer
from rest_framework.permissions import IsAuthenticated   
from django.contrib.auth.models import User 
    
    
class CommunityView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid():
            privacy = serializer.validated_data.get('privacy')
            
            # Set participants based on privacy setting
            if privacy == 'restricted':
                participant_ids = request.data.get('participants', [])
                participants = list(User.objects.filter(id__in=participant_ids))
            elif privacy == 'public':
                participants = [request.user]
            else:
                participants = []

            serializer.save(user=request.user, participants=participants)
            
            # Calculate and update the number of participants
            community = serializer.instance
            community.participants_count = len(participants)
            community.save()
            response_data = serializer.data
            response_data['id'] = community.id
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


