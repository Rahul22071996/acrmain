
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .import views
# from .views import GeneratePdf

urlpatterns = [
    path('acr/<int:id>',views.acr_data,name="acr_data"),
    path('Appraisee/list/',views.Appraisee,name="Appraisee"),
    path('Personal-Data/<int:id>',views.Personal_Data,name="Personal_Data"),
    path('pdf/<int:id>',views.pdf,name="pdf"),
    # path('pdf/', GeneratePdf.as_view()),
    path('lol/<int:id>',views.BirthCertificate_PDF)
]+static(settings.MEDIA_URL,doucment_root=settings.MEDIA_ROOT)
