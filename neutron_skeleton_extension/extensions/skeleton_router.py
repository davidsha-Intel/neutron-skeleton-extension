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

from abc import ABCMeta
from abc import abstractmethod

import six

from oslo_config import cfg

from neutron.api import extensions as neutron_ext
from neutron.api.v2 import attributes as attr
from neutron.api.v2 import resource_helper
from neutron.services import service_base

from neutron_skeleton_extension import extensions

cfg.CONF.import_opt('api_extensions_path', 'neutron.common.config')
neutron_ext.append_api_extensions_path(extensions.__path__)

L3_PREFIX = "/skeleton_router"
L3_EXT = "skeleton_router"

def validate_string(String):
    if String is None:
        String = ''
    return String

#NOTE(davidsha) This list can be extended to include any fields
RESOURCE_ATTRIBUTE_MAP = {
    'skeleton_router_parameters': {
        'id': {
            'allow_post': False, 'allow_put': False,
            'is_visible': True,
            'validate': {'type:uuid': None},
            'primary_key': True},
        'name': {
            'allow_post': True, 'allow_put': True,
            'is_visible': True, 'default': None,
            'validate': {'type:string': attr.NAME_MAX_LEN},
            'convert_to': validate_string},
        'description': {
            'allow_post': True, 'allow_put': True,
            'is_visible': True, 'default': None,
            'validate': {'type:string': attr.DESCRIPTION_MAX_LEN},
            'convert_to': validate_string},
        'tenant_id': {
            'allow_post': True, 'allow_put': False,
            'is_visible': True,
            'validate': {'type:string': attr.TENANT_ID_MAX_LEN},
            'convert_to': validate_string,
            'required_by_policy': True},
        'unique_parameter': {
            'allow_post': True, 'allow_put': False,
            'is_visible': True,
            'validate': {'type:string': attr.TENANT_ID_MAX_LEN},
            'convert_to': validate_string,
            'required_by_policy': True},
    },
}

skeleton_router_quota_opts = [
    cfg.IntOpt('quota_skeleton_router_parameters',
               default=10,
               help=_('Maximum number of skeleton_router_parameters per tenant. '
                      'A negative value means unlimited.'))
]

cfg.CONF.register_opts(skeleton_router_quota_opts, 'QUOTAS')

class Skeleton_router(neutron_ext.ExtensionDescriptor):
    """Skeleton Router API extension."""

    @classmethod
    def get_name(cls):
        return "skeleton_router"

    @classmethod
    def get_alias(cls):
        return "skeleton_router"

    @classmethod
    def get_description(cls):
        return "The Skeleton Router extension."

    @classmethod
    def get_updated(cls):
        return "2015-27-09T10:00:00-00:00"

    @classmethod
    def get_plugin_interface(cls):
        return extensions.skeleton_router.SkeletonRouterPluginBase

    @classmethod
    def get_resources(cls):
        """Returns Ext Resources."""
        special_mappings = {'skeleton_router_parameters': 'skeleton_router_parameter'}
        plural_mappings = resource_helper.build_plural_mappings(
            {}, RESOURCE_ATTRIBUTE_MAP)
        attr.PLURALS.update(plural_mappings)

        resources = resource_helper.build_resource_info(
                plural_mappings,
                RESOURCE_ATTRIBUTE_MAP,
                "skeleton_router",
                translate_name=True,
                allow_bulk=True)

        return resources

    def update_attributes_map(self, attributes, extension_attrs_map=None):
        super(Skeleton_router, self).update_attributes_map(
            attributes, extension_attrs_map=RESOURCE_ATTRIBUTE_MAP)

    def get_extended_resources(self, version):
        if version == "2.0":
            return RESOURCE_ATTRIBUTE_MAP
        else:
            return {}


@six.add_metaclass(ABCMeta)
class SkeletonRouterPluginBase(service_base.ServicePluginBase):

    def get_plugin_name(self):
        return L3_EXT

    def get_plugin_type(self):
        return L3_EXT

    def get_plugin_description(self):
        return 'Skeleton Router service plugin.'

    #NOTE(davidsha) Following commands are tied to REST API.
    # These require a create, update, delete and get/get(s) function

    def create_skeleton_router_parameter(self, context, router):
        pass

    def update_skeleton_router_parameter(self, context, router_id, router):
        pass

    def delete_skeleton_router_parameter(self, context, router_id, router):
        pass

    def get_skeleton_router_parameter(self, context, router_id):
        pass

    def get_skeleton_router_parameters(self, context, **kwargs):
        pass
