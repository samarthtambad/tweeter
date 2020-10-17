import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect

from .forms import TweetForm
from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/home.html", context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    print("post data is", request.POST)
    next_url = request.POST.get("next") or None
    print("next_url", next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url:
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})

def tweet_list_view(request, ):
    """
    REST API VIEW
    return json response with a list of all tweets
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 999)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detailed_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    return json response with tweet corresponding to given tweet_id
    """
    data = {
        "id": tweet_id,
        # "image_path": obj.image,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)
