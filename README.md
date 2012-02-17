<3 BELOVED
===========

Test application for use django-nonorel with mongo-engine and tastypie. 

BTW it helps me keeping track of my beloved stuff eg. my tshirt, tastypie, pizza and my girldfriend.


API
----

Example request: http://cl.ly/242t1C3o1X2U2k1Y2r3O


**Beloved items:**
          /api/v1/beloveds/


Get paginated items: curl -X GET -H "Accept: application/json" localhost:8888/api/v1/beloveds/
          
{
  "meta": {
    "previous": null,
    "next": null,
    "total_count": 2,
    "limit": 20,
    "offset": 0
  },
  "objects": [
    {
      "name": "Colourlovers",
      "public_love_rate": 0,
      "my_love_rate": 100,
      "tags": "[u'web', u'design', u'color']",
      "id": "4f3e18e7aeef8fb793000000",
      "resource_uri": "/api/v1/beloveds/4f3e18e7aeef8fb793000000/"
    },
    {
      "name": "Youtube background pattern",
      "public_love_rate": 0,
      "my_love_rate": 100,
      "tags": "[u'pattern', u'design']",
      "id": "4f3e191faeef8fb793000002",
      "resource_uri": "/api/v1/beloveds/4f3e191faeef8fb793000002/"
    }
  ]
}

Get one item: curl -X GET -H "Accept: application/json" localhost:8888/api/v1/beloveds/4f3e191faeef8fb793000002/
{
  "name": "Youtube background pattern",
  "public_love_rate": 0,
  "my_love_rate": 100,
  "tags": "[u'pattern', u'design']",
  "id": "4f3e191faeef8fb793000002",
  "resource_uri": "/api/v1/beloveds/4f3e191faeef8fb793000002/"
}
