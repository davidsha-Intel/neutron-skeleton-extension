# Copyright (c) 2016 Intel. All Rights Reserved.
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

from neutronclient.common import extension
from neutronclient.neutron import v2_0 as neutronv20

from neutron_skeleton_extension._i18n import _


class SkeletonPortParameter(extension.NeutronClientExtension):
    resource = "skeleton_port_parameter"
    resource_plural = '%ss' % resource
    object_path = '/skeleton_port/%s' % resource_plural
    resource_path = '/skeleton_port/%s/%%s' % resource_plural
    versions = ['2.0']

class SkeletonPortParameterUpdate(extension.ClientExtensionUpdate,
                             SkeletonPortParameter):
    """Update a Skeleton Parameter."""
    shell_command = "skeleton-port-parameter-update"

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name',
            metavar='NAME',
            help=_('Name of the Skeleton Parameter.'))
        parser.add_argument(
            '--description',
            help=_('Description for the Skeleton Parameter.'))
        parser.add_argument(
            '--unique_parameter',
            help=_('Skeleton Parameter for port.'))

    def args2body(self, parsed_args):
        body = {}
        neutronv20.update_dict(parsed_args, body, ['name', 'description',
                                                   'unique_parameter'])
        return {self.resource: body}

class SkeletonPortParameterCreate(extension.ClientExtensionCreate,
                             SkeletonPortParameter):
    """Create a Skeleton Parameter."""
    shell_command = "skeleton-port-parameter-create"

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name',
            metavar='NAME',
            help=_('Name of the Skeleton Parameter.'))
        parser.add_argument(
            '--description',
            help=_('Description for the Skeleton Parameter.'))
        parser.add_argument(
            '--unique_parameter',
            help=_('Skeleton Parameter for port.'))

    def args2body(self, parsed_args):
        body = {}
        neutronv20.update_dict(parsed_args, body, ['name', 'description',
                                                   'unique_parameter'])
        return {self.resource: body}


class SkeletonPortParameterDelete(extension.ClientExtensionDelete,
                             SkeletonPortParameter):
    """Delete a given Skeleton Parameter."""

    shell_command = 'skeleton-port-parameter-delete'


class SkeletonPortParameterList(extension.ClientExtensionList,
                             SkeletonPortParameter):
    """List the Skeleton Parameters that belong to a given tenant."""

    shell_command = 'Skeleton-port-parameter-list'
    list_columns = ['id', 'name', 'unique_parameter']
    pagination_support = True
    sorting_support = True


class SkeletonPortParameterShow(extension.ClientExtensionShow,
                             SkeletonPortParameter):
    """Show information of a given Skeleton Parameter."""

    shell_command = 'skeleton-port-parameter-show'
