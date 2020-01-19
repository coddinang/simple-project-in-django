from django.urls import path
from . import views

# urls from the polls app
# for specify the url of an app, just add the name of the app
# Then in the template type '<name_of_app>:<name_of_app_template>'
app_name = 'polls'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]