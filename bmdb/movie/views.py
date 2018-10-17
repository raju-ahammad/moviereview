from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie, Category, Genera, Actor, Director, Writter, Comment
from .forms import CommentForm


class HomepageView(ListView):

    model          = Movie
    template_name  = 'home.html'
    ordering       = '-time'
    context_object_name = 'movie_list'
    paginate_by  = 8

    def get_context_data(self,**kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['mostViewed'] = Movie.objects.order_by('-view')[0];
        context['time'] = Movie.objects.order_by('-time')[0];
        context['toprated'] = Movie.objects.order_by('-ratings')[0];
        #print(context.movie.actors)
        return context


class DetailPageView(DetailView):
    model          = Movie
    template_name  = 'detail.html'

    def get_object(self):
        object = super(DetailPageView, self).get_object()
        object.view += 1
        object.save()
        return object

    def post(self, request, *args, **kwargs):
        view = CommentView.as_view()
        return view(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailPageView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post = self.get_object())
        context['form'] = CommentForm
        return context





class CategoryView(ListView):
    model    = Movie
    template_name = 'category.html'
    context_object_name = 'category_list'
    paginate_by = 8

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Movie.objects.filter(category=self.category)

    def get_context_data(self,**kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class MovieGeneraView(ListView):
    model    = Movie
    template_name = 'genera.html'
    context_object_name = 'genera_list'
    paginate_by = 8

    def get_queryset(self):
        self.genera = get_object_or_404(Genera, pk=self.kwargs['pk'])
        return Movie.objects.filter(genera=self.genera)

    def get_context_data(self,**kwargs):
        context = super(MovieGeneraView, self).get_context_data(**kwargs)
        context['genera'] = self.genera
        return context


class ActorView(ListView):
    model    = Movie
    template_name = 'actor.html'
    context_object_name = 'actor_list'
    paginate_by = 8

    def get_queryset(self):
        self.actors = get_object_or_404(Actor, pk=self.kwargs['pk'])
        return Movie.objects.filter(actors=self.actors)

    def get_context_data(self,**kwargs):
        context = super(ActorView, self).get_context_data(**kwargs)
        context['actors'] = self.actors
        return context


class DirectorView(ListView):
    template_name = 'director.html'
    context_object_name = 'directors'
    paginate_by = 8

    def get_queryset(self):
        self.director = get_object_or_404(Director, pk=self.kwargs['pk'])
        return Movie.objects.filter(director=self.director)

    def get_context_data(self,**kwargs):
        context = super(DirectorView, self).get_context_data(**kwargs)
        context['director'] = self.director
        return context


""" Comment section View"""
class CommentView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'detail.html'
    def form_valid(self, form):
        models_name = Comment()
        models_name.content = self.request.POST['content']
        models_name.author = self.request.user
        models_name.post = Movie.objects.get(pk=self.kwargs['pk'])
        models_name.save()
        return redirect(self.get_success_url(id = self.kwargs['pk']))

    def get_success_url(self, **kwargs):
        if  kwargs != None:
            return reverse_lazy('detail', kwargs = {'pk': kwargs['id']})
        else:
            return reverse_lazy('detail', args = (self.object.id,))






class CatView(ListView):
    model = Category
    template_name = 'cat.html'
    context_object_name = 'cat_list'




class AboutPage(TemplateView):
    template_name = 'about.html'
