from django.contrib import admin

#from .models import Author
#@admin.register(Author)
#class AuthorAdmin(admin.ModelAdmin)
#    pass

# Register your models here.
from .models import Usuarios
from .models import Num_telefono
from .models import Marca
from .models import ParamTipo
from .models import Modelos
from .models import Smartphones
from .models import Tablets
from .models import Notebooks
from .models import Camionetas
from .models import Asignacion
from .models import Estados
from .models import Procesador

admin.site.register(Usuarios)
admin.site.register(Num_telefono)
admin.site.register(Marca)
admin.site.register(ParamTipo)
admin.site.register(Modelos)
admin.site.register(Smartphones)
admin.site.register(Tablets)
admin.site.register(Notebooks)
admin.site.register(Camionetas)
admin.site.register(Asignacion)
admin.site.register(Estados)
admin.site.register(Procesador)