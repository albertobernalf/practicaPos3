from django.contrib import admin

# Register your models here.

from cartera.models import FormasPagos, TiposPagos,Pagos,TiposGlosas,MotivosGlosas, Radicaciones, Remisiones


@admin.register(FormasPagos)
class formasPagosAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)


@admin.register(TiposPagos)
class tiposPagosAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ('nombre',)


@admin.register(Pagos)
class pagosAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "documento", "tipoPago","formaPago")
    search_fields = ("id", "fecha", "documento", "tipoPago","formaPago")
    # Filtrar
    list_filter = ("id", "fecha", "documento", "tipoPago","formaPago")

@admin.register(TiposGlosas)
class tiposGlosasAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")
    # Filtrar
    list_filter = ("id", "nombre")



@admin.register(MotivosGlosas)
class motivosGlosasAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre","descripcion")
    search_fields = ("id", "nombre","descripcion")
    # Filtrar
    list_filter = ("id", "nombre","descripcion")



@admin.register(Radicaciones)
class radicacionesAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "radicacion")
    search_fields = ("id","fecha", "radicacion")
    # Filtrar
    list_filter = ("id", "fecha","radicacion")



@admin.register(Remisiones)
class remisionesAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha","remision")
    search_fields = ("id", "fecha","remision")
    # Filtrar
    list_filter = ("id", "fecha","remision")

