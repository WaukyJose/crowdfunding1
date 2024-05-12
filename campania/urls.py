from django.urls import path
from . import views
from .views import CampaniaDetailView

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.do_signup, name="signup"),
    path("success-signup/", views.success_signup, name="success_signup"),
    path("signin/", views.do_signin, name="signin"),
    path("logout/", views.do_logout, name="logout"),
    path(
        "campania/<int:pk>/", views.CampaniaDetailView.as_view(), name="campania-detail"
    ),
    path("campania/<int:pk>/", CampaniaDetailView.as_view(), name="campania_detail"),
    path(
        "categorias/<int:categoria_id>/campanias/",
        views.get_campania_por_categoria,
        name="campanias_por_categoria",
    ),
    path(
        "donacion/<int:campania_id>/", views.procesar_donacion, name="procesar_donacion"
    ),
    path("campania-fin/", views.campania_fin, name="campania_fin"),
    path("mis-donaciones/", views.get_mis_donaciones, name="mis_donaciones"),
]
