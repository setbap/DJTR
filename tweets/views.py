from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweets
# Create your views here.


def home_view(req, *args, **kwargs):
    # return HttpResponse("this is me new")
    return render(req, 'pages/home.html', context={}, status=200)


def tweet_detail_view(req, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        tweet = Tweets.objects.get(id=tweet_id)
        data["content"] = tweet.content
    except:
        status = 404
        data["message"] = "not found"

    return JsonResponse(data, status=status)


def tweet_list_view(req, *args, **kwargs):

    status = 200
    tweets = Tweets.objects.all()
    data = {
        "res": [{"id": o.id, "content": o.content} for o in tweets]
    }

    return JsonResponse(data, status=status)
