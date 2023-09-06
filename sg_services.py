#!/usr/bin/env python


import os, sys
import json
from json.decoder import JSONDecodeError
from snap import snap, common
import jinja2
from collections import namedtuple
from contextlib import contextmanager
import datetime
import time


class UnregisteredTemplateError(Exception):
    def __init__(self, template_name):
        super().__init__(f'No template registered under the alias {template_name}.')


class MissingTemplateFileError(Exception):
    def __init__(self, template_name, filename):
        super().__init__(f'The template file {filename}, registered under the alias {template_name}, does not exist.')


class TemplatingService(object):
    def __init__(self, **init_params):

        self.template_dir = init_params['template_dir']

        template_tbl = dict()
        templates = init_params['template_files']

        for entry in templates:
            for id,filename in entry.items():
                template_tbl[id] = filename


    def lookup_template(self, tpl_name):

        template_file = self.template_tbl.get(tpl_name)
        if not template_file:
            raise UnregisteredTemplateError(tpl_name)
        
        template_path = os.path.join(os.getcwd(), self.template_dir, template_file)

        if not os.path.isfile(template_path):
            raise MissingTemplateFileError(tpl_name, template_path)


    def render(self, template_name, **params):

        j2env = jinja2.Environment(trim_blocks=True)
        template_mgr = common.JinjaTemplateManager(j2env)

        template_file = self.lookup_template(template_name)

        template_str = None
        with open(template_file, 'r') as f:
            template_str = f.read()

        j2template = j2env.from_string(template_str)
        return j2template.render(**params)