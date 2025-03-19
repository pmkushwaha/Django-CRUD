from django.shortcuts import render
from .models import Tweet
from .forms import tweetForm
from django.shortcuts import get_object_or_404,redirect

# home view
def index(request):
    return render(request ,'index.html')

# list of tweets view
def Tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

# create tweet
def tweet_create(request):
    # if form have post method
    if request.method=='POST':
        form=tweetForm(request.POST, request.FILES)
        if form .is_valid():
            tweet=form.save(commit=False)  #"commit=False is use to not save data in DB for certain time"
            tweet.User=request.user
            tweet.save()
            return redirect("tweet_list")
    # if empty form         
    else:
        form=tweetForm()
    return render(request,'tweet_form.html',{'form':form})

# To Edit the tweet 

def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)  #to get the details of the user 
    if request.method=="POST":
        tweet=tweetForm(request.POST,request.FILES,instance=tweet)
        if tweet.is_valid():
            tweet=form.save(commit=False)
            # to get the user
            tweet.user=request.user
            tweet.save()  #final save
            return redirect("tweet_list")
    else:
        form=tweetForm(instance=tweet)
    return render(request,"tweet_form.html",{'form':form})

#  to delete
def  tweet_delete(request ,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request,"tweet_confirm_delete.html",{'tweet':tweet})
