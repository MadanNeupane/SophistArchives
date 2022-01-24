from django.shortcuts import render

import video
from .models import Video

def index_page(request):
    videos = Video.objects.all()
    
    context = {
        'videos': videos
    }
    
    return render(request, 'index.html', context=context)
