from modeltranslation.translator import register, TranslationOptions
from .models import Servicio, FAQ

# Traducciones para Servicio
class ServicioTranslationOptions(TranslationOptions):
    fields = ('titulo', 'descripcion')  # los campos que quieres traducir

translator.register(Servicio, ServicioTranslationOptions)

# Traducciones para FAQ
class FAQTranslationOptions(TranslationOptions):
    fields = ('pregunta', 'respuesta')

translator.register(FAQ, FAQTranslationOptions)