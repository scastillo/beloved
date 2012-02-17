from tastypie import fields
from tastypie.resources import ModelResource

from beloved.core.models import Beloved

class BelovedResource(ModelResource):
    """
    Resource for my dear and beloved stuff
    """
    
    class Meta:
        queryset = Beloved.objects.all()
        include_resource_uri = True
        resource_name = 'beloveds'
        
