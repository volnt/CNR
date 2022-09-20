from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("inscription/", views.inscription_view, name="inscription"),
    path("fonctionnement/", views.fonctionnement_view, name="fonctionnement"),
    path("cgu/", views.cgu_view, name="cgu"),
    path("mentions-legales/", views.mentions_legales_view, name="mentions_legales"),
    path("accessibilite/", views.accessibilite_view, name="accessibilite"),
    path("donnees-personnelles/", views.donnees_personnelles_view, name="donnees_personnelles"),
    path("survey/", views.survey_view, name="survey"),
    path("survey-intro/", views.survey_intro_view, name="survey_intro"),
    path("survey-outro/", views.survey_outro_view, name="survey_outro"),
]
