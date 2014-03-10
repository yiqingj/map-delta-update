from pyramid.view import view_config

import json
import os


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'apiservice'}

@view_config(route_name='list', renderer='json')
def list_area(request):
    area_list = json.load(open("script/area-list.json"))
    return area_list

@view_config(route_name='data', renderer='json')
def get_data(request):

    return {}

@view_config(route_name='update', renderer='json')
def update_data(request):
    os.system("script/delta-gen.py")
    return {}