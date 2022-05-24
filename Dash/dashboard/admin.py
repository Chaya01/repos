from django.contrib import admin

# Register your models here.
from .models import Usuarios
from .models import Departamentos
from .models import Num_telefono
from .models import Series
from .models import Historial
from .models import Equipos

admin.site.register(Usuarios)
admin.site.register(Departamentos)
admin.site.register(Num_telefono)
admin.site.register(Series)
admin.site.register(Historial)
admin.site.register(Equipos)