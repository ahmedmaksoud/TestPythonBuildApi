#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task
#import uvicorn
import sys
import os
#from src.main.python import mian

use_plugin("python.core")
use_plugin("python.install_dependencies")
#use_plugin("python.unittest")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")




name = "testBuild"
default_task = ["publish"]

@init
def initialize(project):
    project.set_property('dir_source_main_python', 'src/main/python')
    project.set_property('dir_source_unittest_python', 'src/unittest/python')
    #project.build_depends_on("mockito")
    #project.build_depends_on("fastapi")
    #project.build_depends_on("uvicorn")
    #project.depends_on("requests") 

    project.depends_on_requirements("requirements.txt")
@task
def run_server(project):
    import uvicorn;
    print('pathh  ', sys.path)
    print(f"dir_source_main_python is set to: {project.get_property('dir_source_main_python')}")
    sys.path.insert(0, os.path.abspath(project.get_property('dir_source_main_python')))
    #sys.path.insert(0, os.path.abspath('src/main/python'))
    uvicorn.run("app.mian:app",  host="127.0.0.1", port=8000, reload=True)

#@init
#def set_properties(project):
#    pass
