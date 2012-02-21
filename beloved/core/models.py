from django.db import models
from djangotoolbox.fields import ListField, DictField
from djangotoolbox.fields import EmbeddedModelField
from django_mongodb_engine.contrib import MongoDBManager

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

class Point(models.Model):
    longitude = models.FloatField()
    lattitude = models.FloatField()

    def all(self):
        """
        WIRD workaround for 'the_m2ms.all()' problem with tastypie 
        """
        return self.__class__.objects.all()

    #def __unicode__(self):
    #    return '(%s, %s)' % (self.longitude, self.lattitude)

class Beloved(models.Model):
    """
    Simple stuff beloved by my.
    eg: Tastypie, youtube's background pattern, my girldfriend, ...
    """
    
    objects = MongoDBManager()
    
    name = models.CharField(max_length=200)
    my_love_rate = models.IntegerField()
    public_love_rate = models.IntegerField(default=0)
    tags = TagField()
    loc = EmbeddedModelField('Point')
    # TODO: Comments comming soon!
    #comments = CommentField()


