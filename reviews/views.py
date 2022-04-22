from multiprocessing import context
from tkinter.tix import Form
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView

from .forms import ReviewForm
from .models import Review
# from .models import Review       Modelform removes need for this import

# Create your views here.

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()


#         return render(request, "reviews/review.html", {
#             "form": form
#     })

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
        
#         return render(request, "reviews/review.html", {
#             "form": form
#     })

# class ReviewView(FormView):     # replaces View with both Post and Get methods
#     form_class = ReviewForm
#     template_name = "reviews/review.html"  # get defined here
#     success_url = "/thank-you"      # Post redirect page

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form) # saving data to database

class ReviewView(CreateView):   #replaces FormView
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url ="/thank-you"


# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html" # shorter way of making a classview when only get method is required, I prefer to show get def

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context

# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"  List view simplifies this

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):                   can still modify query in ListView
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

# class ReviewDetailView(TemplateView):
#     template_name = "reviews/detail.html"

#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         print(review_id)
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context

class ReviewDetailView(DetailView):
    template_name ="reviews/detail.html"
    model = Review
    

# def review(request):              no longer need thanks to ReviewView Class
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             # review= Review(
#                 # user_name=form.cleaned_data['user_name'],     Modelform allows data to be saved directly from ModelForm
#                 # review_text=form.cleaned_data['review_text'],
#                 # rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save()

#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })

# def thank_you(request):
#     return render(request, "reviews/thank_you.html")      # classview replaced this