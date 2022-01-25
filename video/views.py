from django.shortcuts import render
from .models import Video
from django.db.models import Q

def index_page(request):
    title = 'Home'
    data = []
    limited_videos = []
    
    search_query = request.GET.get('search')

    if search_query:
        data = Video.objects.filter(
            Q(video_title__icontains=search_query)).distinct().order_by('video_posted_on')
        if len(data) > 0:
            limited_videos = data[:3]
        title = f'Search results for {search_query}'

    context = {
        'data': data,
        'videos': limited_videos,
        'title': title,
        'search_query': search_query
    }
    
    return render(request, 'index.html', context=context)
