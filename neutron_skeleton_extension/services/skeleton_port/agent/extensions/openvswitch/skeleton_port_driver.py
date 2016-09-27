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

from oslo_log import log as logging

from neutron_skeleton_extension.services.skeleton_port.agent.extensions import skeleton_port_driver_base

LOG = logging.getLogger(__name__)

class SkeletonPortOvsDriver(skeleton_port_driver_base.SkeletonPortAgentDriverBase):

    def initialize(self):
        LOG.debug("\n\nInitializing Blank L2 OVS driver\n\n")
        self.known_ports = []

        LOG.debug("\n\nRequesting Bridges from AgentExtensionsAPI\n\n")

        self.br_int = self.agent_api.request_int_br()
        self.br_tun = self.agent_api.request_int_br()

        if self.br_tun is None:
            LOG.debug("\n\nTunneling is not enabled on Neutron\n\n")
        else:
            LOG.debug("\n\nTunneling enabled on Neutron\n\n")


    def consume_api(self, agent_api):
        LOG.debug("\n\nAgentApi recieved and stored\n\n")

        self.agent_api = agent_api

    def port_created(self, port):
        p_id = port['port_id']
        LOG.debug("\n\nOVS driver port_created called on port %s\n\n" % p_id)

    def port_updated(self, port):
        p_id = port['port_id']
        LOG.debug("\n\nOVS driver port_updated called on port %s\n\n" % p_id)

    def port_deleted(self, port):
        p_id = port['port_id']
        LOG.debug("\n\nOVS driver port_deleted called on port %s\n\n" % p_id)

