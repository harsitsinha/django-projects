from django.shortcuts import render
from sympy import re
from .forms import CommentForm
from .models import Comment
# Create your views here.
movies = [
    {
        "id":1,
        "name":"American Beauty",
        "slug":"American-Beauty",
        "image":"https://upload.wikimedia.org/wikipedia/en/9/9a/American_Beauty_1999_film_poster.jpg"

    },
    {
        "id":2,
        "name":"Jumangi",
        "slug":"Jumangi",
        "image":"https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png"

    },
]
def home(request):
    return render(request,'forum/index.html',{
        'movies':movies,
    })



def movie_detail(request, slug):
    identified_movie = next(mov for mov in movies if mov['slug'] == slug)
    if request.method == 'POST':
        user_comment = CommentForm(request.POST)

        if user_comment.is_valid():
            model_comment =  Comment(username = user_comment.cleaned_data['username'], comment = user_comment.cleaned_data['comment'], movie = identified_movie['name'])
            model_comment.save()
        else:
            user_comment = CommentForm()

    comment = CommentForm()
    comment_list = Comment.objects.filter(movie=identified_movie["name"])
    return render(request, "forum/movie_details.html", {
      "movie": identified_movie,
      "comment" : comment,
      "comment_list" : comment_list,
    })