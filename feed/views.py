from django.shortcuts import render, redirect
from .models import Message, Comment, Like
from django.contrib.auth.decorators import login_required

@login_required
def feed_view(request):
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'feed/feed.html', {'messages': messages})

@login_required
def post_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(user=request.user, content=content)
    return redirect('feed')

@login_required
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    if message.user == request.user:
        message.delete()
    return redirect('feed')

@login_required
def post_comment(request, message_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        message = Message.objects.get(id=message_id)
        Comment.objects.create(user=request.user, message=message, content=content)
    return redirect('feed')

@login_required
def like_message(request, message_id):
    message = Message.objects.get(id=message_id)
    Like.objects.get_or_create(user=request.user, message=message)
    return redirect('feed')

@login_required
def like_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    Like.objects.get_or_create(user=request.user, comment=comment)
    return redirect('feed')
