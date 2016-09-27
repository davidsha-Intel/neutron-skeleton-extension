# Copyright 2016 Intel. All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc
import six

@six.add_metaclass(abc.ABCMeta)
class SkeletonPortAgentDriverBase(object):
    '''Class all drivers can be derived from for consistency.'''

    @abc.abstractmethod
    def initialize(self):
        '''Initialize the drivers'''

    def consume_api(self, agent_api):
        '''Passes Neutron Agent properties to drivers'''

    @abc.abstractmethod
    def port_created(self, port):
        pass

    @abc.abstractmethod
    def port_updated(self, port):
        pass

    @abc.abstractmethod
    def port_deleted(self, port):
        pass

