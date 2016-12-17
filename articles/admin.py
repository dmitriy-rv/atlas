from django.contrib import admin
from articles.models import Article, Excursions, Image, Gallery, Map
from image_cropping import ImageCroppingMixin

# Register your models here.


admin.site.register(Article)
admin.site.register(Map)

class InlineImage(admin.TabularInline):
    model = Image

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
	pass

class CelebrityAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [InlineImage]
    pass



admin.site.register(Excursions, CelebrityAdmin)
admin.site.register(Gallery, MyModelAdmin)