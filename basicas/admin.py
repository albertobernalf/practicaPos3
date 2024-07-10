from django.contrib import admin

# Register your models here.



from basicas.models import EstadoCivil,  Ocupaciones, CentrosCosto, Eventos, TiposFamilia, TiposContacto, Periodos, FuripsLista, FuripsParametro

@admin.register(EstadoCivil)
class estadoCivilAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)

@admin.register(Ocupaciones)
class ocupacionesAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)

@admin.register(CentrosCosto)
class centrosCostoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)


@admin.register(Eventos)
class eventosoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ("id", "nombre")

@admin.register(TiposFamilia)
class tiposFamiliaCostoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)

@admin.register(TiposContacto)
class tiposContactoCostoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)

@admin.register(Periodos)
class periodosoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre","año","mes","diaInicial","diaFinal")
    search_fields = ("id", "nombre","año","mes","diaInicial","diaFinal")
    # Filtrar
    list_filter =("id", "nombre","año","mes","diaInicial","diaFinal")

@admin.register(FuripsLista)
class furipsListaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)

@admin.register(FuripsParametro)
class furipsParametroAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre","furipsLista")
    search_fields = ("id", "nombre","furipsLista")
    # Filtrar
    list_filter = ('nombre',"furipsLista")