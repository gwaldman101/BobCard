from django.views import generic
from .models import Album
from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions

class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

def myview(request):
    # Build context for rendering QR codes.
    context = dict(
        my_options=QRCodeOptions(size='t', border=6, error_correction='L'),
    )

    # Render the view.
    return render(request, 'music/index.html', context=context)















'''
#from django.http import Http404
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
#from django.template import loader
from .models import Album, Song

# Create your views here.

def index(request):
    all_albums = Album.objects.all()

    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'

    #template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    #return HttpResponse("<h2>Details for Album ID: " + str(album_id) + "</h2>")

    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")


    album =  get_object_or_404(Album, pk=album_id)

    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album':album, 'error_message': "You did not select a valid song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album':album})
'''
