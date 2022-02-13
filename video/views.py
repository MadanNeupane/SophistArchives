from django.shortcuts import render
from .models import Video
from django.db.models import Q

def index_page(request):
    title = 'Home'
    data = []
    limited_videos = []
    search_query_length = 0
    # recently_watched = []

    search_query = request.GET.get('search')
    if search_query != None:
        search_query_length = len(search_query)

    if search_query_length > 2:
        data = Video.objects.filter(
            Q(video_title__icontains=search_query)).distinct().order_by('video_posted_on')
        if len(data) > 0:
            limited_videos = data[:3]
        title = f'Search results for {search_query}'

    context = {
        'data': data,
        'videos': limited_videos,
        'title': title,
        'search_query': search_query,
        'search_query_length': search_query_length,
        # 'recently_watched': recently_watched
    }
    
    return render(request, 'index.html', context=context)


    # search_query = request.GET.get('search')
    # query = Q()

    # if search_query:
    #     search_strings = search_query.split('-')
    #     q_filter = Q(video_title__icontains=search_strings[0])
    #     for search_string in search_strings[1:]:
    #         q_filter |= Q(video_title__icontains=search_string)
