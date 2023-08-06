#
#  Copyright 2017 Netflix, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# 
from setuptools import setup

setup(
    name='frinx_conductor_workers',
    packages=['frinx_conductor_workers', 'frinx_conductor_workflows'],
    version='1.1.1',
    description='Conductor python client workers',
    author='Frinx',
    author_email='info@frinx.io',
    url='https://github.com/FRINXio/fm-base-workers',
    keywords=['conductor'],
    license='Apache 2.0',
    include_package_data=True
    # install_requires = [
    #   'requests',
    # ]
)
