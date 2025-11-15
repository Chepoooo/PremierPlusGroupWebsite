# translation.py
from modeltranslation.translator import TranslationOptions, register
from .models import Servicio, FAQ


@register(Servicio)
class ServicioTranslationOptions(TranslationOptions):
    fields = ('titulo', 'descripcion',)


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('pregunta', 'respuesta',)