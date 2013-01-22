from django.contrib import admin
from bees.models import *

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
	list_display = ("name",)
	
class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class PhotoAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("gallery", "image", "caption")}
	list_display = ("slug", "caption", "gallery",)
	
class PhotoInline(admin.StackedInline):
	model = Photo
	prepopulated_fields = {"slug": ("gallery", "image", "caption")}
	
class GalleryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ("title",)
	sortable_field_name = "index"
	inlines = [ PhotoInline, ]

class MemberAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("last_name","first_name",)}
	list_display = ("last_name", "first_name", "weapon",)
	radio_fields = {"gender": admin.HORIZONTAL, "weapon": admin.HORIZONTAL}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Member, MemberAdmin)