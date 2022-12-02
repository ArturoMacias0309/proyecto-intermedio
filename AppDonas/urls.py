from django.urls import path
from AppDonas.views import *

urlpatterns = [
    
    path("inicio", inicio, name="inicio"),
    path("donaprem", donaprem, name="donaprem"),
    path("donareg", donareg, name="donareg"),
    path("malteadas", malteadas, name="malteadas"),
    path("busqueda_donaprem", busqueda_donaprem, name="busqueda_donaprem"),
    path("resultado_busqueda_donaprem", resultado_busqueda_donaprem, name="resultado_busqueda_donaprem"),


]
