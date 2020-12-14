from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),

    # book
    path('api/createBook', views.createBook),
    path('api/retrieveBook', views.retrieveBook),
    path('api/updateBook', views.updateBook),
    path('api/deleteBook', views.deleteBook),

    # # user
    # path('api/createUser', views.createUser),
    # path('api/retrieveUser', views.retrieveUser),
    # path('api/updateUser', views.updateUser),
    # path('api/deleteBook', views.deleteBook),

    # # borrow information
    # path('api/createBorrowInfo', views.createBorrowInfo),
    # path('api/retrieveBorrowInfo', views.retrieveBorrowInfo),
    # path('api/updateBorrowInfo', views.updateBorrowInfo),
    # path('api/deleteBorrowInfo', views.deleteBorrowInfo),

]