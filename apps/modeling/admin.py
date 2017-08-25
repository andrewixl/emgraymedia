from django.contrib import admin
from .models import Album, Picture, Home, Contact, Package, About, Navbar, Promotion, ContactPage
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.text import force_text

def get_picture_preview(obj):
    if obj.pk:  # if object has already been saved and has a primary key, show picture preview
        return """<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
            src=obj.photo.url,
            title=obj.photo_caption,
        )
    return _("(choose a picture and save and continue editing to see the preview)")
get_picture_preview.allow_tags = True
get_picture_preview.short_description = _("Picture Preview")


class PictureInline(admin.StackedInline):
    model = Picture
    extra = 0
    fields = ["get_edit_link", "photo_caption", "photo", get_picture_preview]
    readonly_fields = ["get_edit_link", get_picture_preview]

    def get_edit_link(self, obj=None):
        if obj.pk:  # if object has already been saved and has a primary key, show link to it
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            return """<a href="{url}">{text}</a>""".format(
                url=url,
                text=_("Edit this %s separately") % obj._meta.verbose_name,
            )
        return _("(save and continue editing to create a link)")
    get_edit_link.short_description = _("Edit link")
    get_edit_link.allow_tags = True


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ["album_name", "album_cover", "album_location", "album_description", "album_photographer", "shoot_date"]
    inlines = [PictureInline]

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ["master_album", "photo_caption", "photo", get_picture_preview]
    readonly_fields = [get_picture_preview]



# admin.site.register(Album)
# admin.site.register(Photo)
admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(Package)
admin.site.register(About)
admin.site.register(Navbar)
admin.site.register(Promotion)
admin.site.register(ContactPage)
# Register your models here.
