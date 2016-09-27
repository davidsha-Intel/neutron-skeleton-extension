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

from oslo_log import log as logging

from neutron.agent.l2 import l2_agent_extension
from neutron import manager

LOG = logging.getLogger(__name__)

class SkeletonPortAgentExtension(l2_agent_extension.L2AgentExtension):

    def consume_api(self, agent_api):
        '''Used to pass Neutron Agent properties to extensions'''
        self.agent_api = agent_api

    def initialize(self, connection, driver_type):
        '''Initialize the Agent Extension.'''

        LOG.debug("Initializing SkeletonPortAgentExtension with driver type: %s"
                  % (driver_type))
        #NOTE(davidsha) 'neutron_skeleton_extension.l2.agent_drivers' is in setup.cfg
        #driver_type constains the neutron l2 driver being used ie. ovs
        #the driver_type is mapped to the driver location within the project.
        #For ovs that is:
        # neutron_skeleton_extension.services.skeleton_port.agent.extensions.openvswitch.
        # skeleton_port_driver.SkeletonPortOVSDriver

        self.skeleton_port_driver = manager.NeutronManager.load_class_for_provider(
            'neutron_skeleton_extension.skeleton_port.drivers', driver_type)()
        #NOTE(davidsha) Consume_api should always be called before
        #initializing the driver.
        self.skeleton_port_driver.consume_api(self.agent_api)
        self.skeleton_port_driver.initialize()
        self.known_ports = []

    def handle_port(self, context, port):
        '''The Function called by the AgentExtensionsManger on port update.'''
        if port['port_id'] in self.known_ports:
            LOG.debug("port %s updated", port['port_id'])
            self.skeleton_port_driver.port_updated(port)
        else:
            LOG.debug("port %s created", port['port_id'])
            self.skeleton_port_driver.port_created(port)
            self.known_ports.append(port['port_id'])

    def delete_port(self, context, port):
        '''The Function called by the AgentExtensionsManger on port delete.'''
        LOG.debug("port %s deleted", port['port_id'])
        self.skeleton_port_driver.port_deleted(port)
        self.known_ports.remove(port['port_id'])
