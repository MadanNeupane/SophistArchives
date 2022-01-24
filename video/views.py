from django.shortcuts import render

import video
from .models import Video

def index_page(request):
    videos = Video.objects.all()
    
    context = {
        'title': 'Home Page',
        'videos': videos
    }
    
    return render(request, 'index.html', context=context)
