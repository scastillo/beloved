from django.db import models
from djangotoolbox.fields import ListField

from beloved.core.forms import StringListField

#Fields
class BelovedListField(ListField):
    """ Base ListField for the project
        this one fixes listfields problems in admin
        (thanks to jonashaag gist: 1200165)
    """
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)

class TagField(BelovedListField):
    """ Tags like in django-tagging eg. tag1, tag2, tag3 """
    pass

class CommentField(BelovedListField):
    """ Comments like blog post ones """
    pass

#Models
class Beloved(models.Model):
    """
    Simple stuff beloved by my.
    eg: Tastypie, youtube's background pattern, my girldfriend, ...
    """
    
    name = models.CharField(max_length=200)
    my_love_rate = models.IntegerField()
    public_love_rate = models.IntegerField(default=0)
    tags = TagField()
    # TODO: Comments comming soon!
    #comments = CommentField()


