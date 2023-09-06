
#!/usr/bin/env python

 
from snap import snap
from snap import core
import json
from snap.loggers import transform_logger as log



def ping_func(input_data, service_objects, **kwargs):
    return core.TransformStatus(
        json.dumps({"status": "ok", "message": "The Sightglass service is alive."})
    )


def page_func(input_data, service_objects, **kwargs):
    
    htmldata = None
    with open('pages/test.html', 'r') as f:
        htmldata = f.read()

    return core.TransformStatus(htmldata)


def nav_func(input_data, service_objects, **kwargs):

    htmldata = None
    with open('pages/nav.html', 'r') as f:
        htmldata = f.read()

    return core.TransformStatus(htmldata)
    
