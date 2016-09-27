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

from neutron.agent.l3 import l3_agent_extension
from oslo_log import log as logging

LOG = logging.getLogger(__name__)

class SkeletonRouterAgentExtension(l3_agent_extension.L3AgentCoreResourceExtension):

    SUPPORTED_RESOURCE_TYPES = []

    def __init__(self):
        LOG.debug("\n\n\nSkeleton Router: extension loading\n\n")
        super(SkeletonRouterAgentExtension, self).__init__()

    def initialize(self,  connection, driver_type):
        LOG.debug("\n\n\nSkeleton Router: extension loaded with driver: %s\n\n" % driver_type)

    def consume_api(self, agent_api):
        LOG.debug("\n\n\nSkeleton Router: extension Consuming agent api\n\n")
        self.agent_api = agent_api

    def add_router(self, context, new_router):
        LOG.debug("\n\n\nSkeleton Router: new router added: %s\n\n" % new_router['name'])

    def update_router(self, context, updated_router):
        LOG.debug("\n\n\nSkeleton Router: router updated: %s\n\n" % updated_router['name'])

    def delete_router(self, context, deleted_router):
        LOG.debug("\n\n\nSkeleton Router: router deleted: %s\n\n" % deleted_router['name'])
