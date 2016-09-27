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

class SkeletonPortLBDriver(skeleton_port_driver_base.SkeletonPortAgentDriver):

    def initailize(self):
        LOG.debug("\n\nInitializing Blank L2 LinuxBridge driver\n\n")
        self.known_ports = []

    def port_created(self, port):
        p_id = port['port_id']
        LOG.debug("\n\nLinuxbridge port_created called on port %s\n\n" % p_id)

    def port_updated(self, port):
        p_id = port['port_id']
        LOG.debug("\n\nlinuxbridge port_updated called on port %s\n\n" % p_id)

    def port_deleted(self, port):
        p_id = port['port_id']
        LOG.debug("\n\nlinuxbridge port_deleted called on port %s\n\n" % p_id)

