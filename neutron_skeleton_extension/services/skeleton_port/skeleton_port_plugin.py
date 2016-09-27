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

from neutron_skeleton_extension.extensions import skeleton_port

LOG = logging.getLogger(__name__)

class SkeletonPortPlugin(skeleton_port.SkeletonPortPluginBase):

    supported_extension_aliases = [skeleton_port.L2_EXT]
    path_prefix = skeleton_port.L2_PREFIX

    def __init__(self):
        super(SkeletonPortPlugin, self).__init__()
        self.driver_manager = None

    def create_skeleton_port_port_parameter(self, context, port):
        LOG.debug("create_skeleton_port_port_parameter")

    def update_skeleton_port_port_parameter(self, context, port_id, port):
        LOG.debug("update_skeleton_port_port_parameter")

    def delete_skeleton_port_port_parameter(self, context, port_id, port):
        LOG.debug("delete_skeleton_port_port_parameter")

    def get_skeleton_port_port_parameter(self, context, port_id):
        LOG.debug("get_skeleton_port_port_parameter")

    def get_skeleton_port_port_parameters(self, context, **kwargs):
        LOG.debug("get_skeleton_port_port_parameters")

