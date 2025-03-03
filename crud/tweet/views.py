from django.shortcuts import render
from .models import Tweet
from .forms import tweetForm
from django.shortcuts import get_object_or_404

# home view
def index(request):
    return render(request ,'index.html')

# list of tweets view
def Tweet_list(request):
    tweet=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

# create tweet
def create_form(request):
    if request.method='POST':
        form=tweetForm(request.POST, request.FILES)
        pass
    else:
        form=tweetForm()
        return render(request,'tweet_form.html'{'form':form})
