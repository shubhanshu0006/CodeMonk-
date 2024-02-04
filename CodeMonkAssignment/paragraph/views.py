
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Paragraph, Word
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated

class StoreParagraphsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        data = request.data

        if 'paragraphs' not in data:
            return Response({'error': 'Missing paragraphs in the request'}, status=status.HTTP_400_BAD_REQUEST)

        paragraphs = data['paragraphs']

        for paragraph_content in paragraphs:
            paragraph = Paragraph.objects.create(content=paragraph_content.lower())

            words = paragraph.content.split()  # Use the lowercased paragraph content
            for word_content in words:
                Word.objects.create(content=word_content, paragraph=paragraph)

        return Response({'message': 'Paragraphs and words stored successfully'}, status=status.HTTP_201_CREATED)

class SearchParagraphsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        word_to_search = request.query_params.get('word', '').lower()

        if not word_to_search:
            return Response({'error': 'Word parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)

        
        paragraphs = Paragraph.objects.annotate(word_count=Count('words')).filter(words__content__iexact=word_to_search).order_by('-word_count')[:10]
        if not paragraphs:
            return Response({'message': 'Word not found in any paragraphs'})

        result = [{'paragraph_id': paragraph.id} for paragraph in paragraphs]
        return Response(result)
