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

from oslo_config import cfg

from neutron_skeleton_extension._i18n import _

L2_EXT_DRIVER_OPTS = [
    cfg.ListOpt('drivers',
                default=['dummy'],
                help=_("An ordered list of Blank L2 drivers "
                       "entrypoints to be loaded from the "
                       "neutron_skeleton_extension.skeleton_port.drivers namespace.")),
]


cfg.CONF.register_opts(L2_EXT_DRIVER_OPTS, "skeleton_port")
