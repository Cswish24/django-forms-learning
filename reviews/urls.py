from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()), # updated to class views. need .asview for classes
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("detail/<int:pk>", views.ReviewDetailView.as_view())
]