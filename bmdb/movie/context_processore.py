from .models import Category, Genera

def category(request):
    return {
    'categories': Category.objects.all(),
    'generas': Genera.objects.all()
    }
