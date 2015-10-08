from django.db import models
from django import forms

# Create your models here.


class CustomAdminDisplayModelChoiceField(forms.ModelChoiceField):
    """This does the second part of the customization.

    Instead of simply displaying the author's name, adds the "(age)" to that.

    Here we have access to the object, and should return its representation.
    Less hacky, more worky.
    """
    def label_from_instance(self, obj):
        return u"{name} ({age})".format(name=obj.name, age=obj.age)


class ForeignCustomDisplayKey(models.ForeignKey):
    """Hooks up the custom model choice field to the model.
    """
    def formfield(self, **kwargs):
        kwargs.update({'form_class': CustomAdminDisplayModelChoiceField})
        return super(ForeignCustomDisplayKey, self).formfield(**kwargs)


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return u"{}".format(self.name)


class Book(models.Model):
    name = models.CharField(max_length=200)
    authors = ForeignCustomDisplayKey(Author, null=True)

    def __str__(self):
        return u"{}".format(self.name)

