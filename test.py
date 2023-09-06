#!/usr/bin/env python



def testme(service_registry, **test_params):
    
    template_svc = service_registry.lookup('templatesvc')
    print(template_svc.render('test', **test_params))

