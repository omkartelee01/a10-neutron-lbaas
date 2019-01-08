# Copyright 2014, Doug Wiegley (dougwig), A10 Networks
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

import acos_client.errors as acos_errors
import handler_base_v2
import logging
import v2_context as a10

from a10_neutron_lbaas.acos import openstack_mappings
from policy import PolicyUtil

LOG = logging.getLogger(__name__)

class L7PolicyHandler(handler_base_v2.HandlerBaseV2):

    def _set(self, set_method,c, context, l7policy, file="", script="", size=0, action="", **kwargs):
        set_method(l7policy, file=file, script=script, size=size, action=action)
        
    def create(self, context, l7policy, **kwargs):
        import pdb; pdb.set_trace()
        print("placeholder")
        with a10.A10WriteStatusContext(self, context, l7policy) as c:
            try:
                filename= l7policy.id
                size = 200
                action="import"
                p = PolicyUtil()
                script= p.createPolicy(l7policy)
                print(script)
                self._set(c.client.slb.aflex_policy.create,
                          c, context, l7policy, filename,script, size, action)
            except acos_errors.Exists:
                pass
