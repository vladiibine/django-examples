from django.contrib import admin
from django.forms import widgets

from .models import Author, Book
# Register your models here.


class CustomBookNameWidget(widgets.Select):
    """If the desired choices is "ASDF", makes if look like ">>>ASDF<<<"

    The desired choice is given by the str(model) (or unicode in Py2)
    You'd ask yourself... "If I can override my model's `str`, then why
    bother?" - well because sometimes the model is in another app.

    This applies to situations when you create relationships between your
    models and Django's User, Group, or whatever, and lets you still customize
    your admin


    Remarks: It couldn't be done in __init__ even though it looks like it.
        Here's the __init__

    def __init__(self, attrs=None, choices=()):
        super(Select, self).__init__(attrs)
        self.choices = list(choices)

    ... the thing is, somewhere (in the RelatedFieldWidgetWrapper.render)
    the .choices is overwritten, so we can intersect this assignment
    and tweak it.
     """
    @property
    def choices(self):
        return self._choices

    @choices.setter
    def choices(self, val):
        self._choices = list(
            (key, ">>>{}<<<".format(value) if key else value)
            for key, value in val
        )


class BookAdmin(admin.ModelAdmin):
    """This admin simply replaces the default Select widget, with a custom one
    """
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        old_field = super(BookAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

        old_widget = old_field.widget

        new_widget = CustomBookNameWidget(old_widget.attrs, old_widget.choices)

        old_field.widget = new_widget
        return old_field


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
