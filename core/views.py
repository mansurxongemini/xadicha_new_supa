from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import NewsBlog, Biography, Book, ScientificArticle, VideoResource
from .models import ProjectAuthor
def home(request):
    latest_news = NewsBlog.objects.all()[:3]
    # Fetch data from the database
    biography = Biography.objects.last()
    
    author = ProjectAuthor.objects.last()

    context = {
        'biography': biography,
        'author': author,
        'latest_news': latest_news
    }
    return render(request, 'index.html', context)



    

def biography_view(request):
    """Renders the Biography page."""
    # Assuming there is only one biography entry. Use first() for safety.
    biography = Biography.objects.first()
    context = {
        'biography': biography
    }
    return render(request, 'biography.html', context)

def books_view(request):
    """Renders the Books page with search functionality."""
    query = request.GET.get('q', '')
    books = Book.objects.all()
    
    if query:
        books = books.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        )
    
    context = {
        'books': books,
        'search_query': query
    }
    return render(request, 'books.html', context)

def articles_view(request):
    """Renders the Scientific Articles page."""
    articles = ScientificArticle.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles.html', context)

def videos_view(request):
    """Renders the Videos page."""
    videos = VideoResource.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'videos.html', context)

def about_view(request):
    """Renders the About page with Author info and Scientific Articles."""
    author = ProjectAuthor.objects.last()
    articles = ScientificArticle.objects.all().order_by('-published_date')
    context = {
        'author': author,
        'articles': articles
    }
    return render(request, 'about.html', context)

def blog_list_view(request):
    """Renders the list of all blog posts."""
    blogs = NewsBlog.objects.all().order_by('-created_at')
    context = {'blogs': blogs}
    return render(request, 'blog_list.html', context)

def blog_detail_view(request, pk):
    """Renders a single blog post detail."""
    blog = get_object_or_404(NewsBlog, pk=pk)
    context = {'blog': blog}
    return render(request, 'blog_detail.html', context)
