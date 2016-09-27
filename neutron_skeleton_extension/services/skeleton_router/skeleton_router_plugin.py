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

from neutron_skeleton_extension.extensions import skeleton_router

LOG = logging.getLogger(__name__)

class SkeletonRouterPlugin(skeleton_router.SkeletonRouterPluginBase):

    supported_extension_aliases = [skeleton_router.L3_EXT]
    path_prefix = skeleton_router.L3_PREFIX

    def __init__(self):
        super(SkeletonRouterPlugin, self).__init__()
        LOG.debug("Initialising Blank L3 Plugin")

    def create_skeleton_router_parameter(self, context, router):
        LOG.debug("Creating Blank L3 router parameter : %s" % router)

    def update_skeleton_router_parameter(self, context, router_id, router):
        LOG.debug("Updating Blank L3 router parameter : %s" % router)

    def delete_skeleton_router_parameter(self, context, router_id, router):
        LOG.debug("Deleting Blank L3 router parameter : %s" % router)

    def get_skeleton_router_parameter(self, context, router_id):
        LOG.debug("Getting Blank L3 router parameter : %s" % id)

    def get_skeleton_router_parameters(self, context, **kwargs):
        LOG.debug("Getting Blank L3 router parameter : %s" % kwargs)

