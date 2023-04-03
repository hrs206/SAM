from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home),
    path("login", views.login, name="login"),
    path("ui", views.ui, name="ui"),
    path("bi", views.bi, name="bi"),
    path("pi", views.pi, name="pi"),
    path("admin1", views.admin, name="admin"),
    path("c_signup_page", views.c_signup_page, name="c_signup_page"),
    path("c_login_page", views.c_login_page, name="c_login_page"),
    path("b_signup_page", views.b_signup_page, name="b_signup_page"),
    path("b_login_page", views.b_login_page, name="b_login_page"),
    path("p_login_page", views.p_login_page, name="p_login_page"),
    path("search_b", views.search_b, name="search_b"),
    path("search_c", views.search_c, name="search_c"),
    path("cart", views.cart, name="cart"),
    path("book_electric", views.book_electric, name="book_electric"),
    path("edit_services", views.edit_services, name="edit_services"),

]