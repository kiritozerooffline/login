from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

'''def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
                form.save()
                author = form.cleaned_data.get('author')
                comment = form.cleaned_data.get('comment')
                return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
        return render(request, 'postlist.html', {'form': form})'''

def postlist(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'mysite/templates/postlist.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mysite/template/post_detail', {'post': post})