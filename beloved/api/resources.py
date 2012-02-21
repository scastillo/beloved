from tastypie import fields
from tastypie.resources import ModelResource

from beloved.core.models import Beloved, Point


class PointResource(ModelResource):
    """
    Represents a geolocalized waypoint
    """
    class Meta:
        queryset = Point.objects.all()
        include_resource_uri = False
        resource_name = 'points'

class BelovedResource(ModelResource):
    """
    Resource for my dear and beloved stuff
    """
    loc = fields.ToManyField(PointResource, 'loc', full=True)

    class Meta:
        queryset = Beloved.objects.all()
        include_resource_uri = True
        resource_name = 'beloveds'

    def dehydrate(self, bundle):
        print "bundle: %s" % bundle
        return bundle

#    def dehydrate_loc(self, bundle):
#        print '$$$$$'
#        print type(bundle.data['loc'])
#        print bundle.data['loc']
#        print '$$$$$'
#        return bundle.obj
        #return (bundle.data['loc'].lattitude, bundle.data['loc'].longitude)

#    def alter_list_data_to_serialize(self, request, data_dict):
#        print "####ALTER"
#        if isinstance(data_dict, dict):
#            print "########DICT: %s" % data_dict
#            if 'objects' in data_dict:
#                if 'loc' in data_dict['objects']:
#                    point = data_dict['objects']['loc']
#                    del(data_dict['loc'])
#                    data_dict['lat'] = point.latitude
#                    data_dict['long'] = point.longitude
#        return data_dict
