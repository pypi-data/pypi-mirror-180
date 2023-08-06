#!/usr/bin/python3

import sys

from saigen.confbase import *
from saigen.confutils import *


class InboundRouting(ConfBase):

    def __init__(self, params={}):
        super().__init__(params)

    def items(self):
        self.numYields = 0
        print('  Generating InboundRouting ...', file=sys.stderr)
        p = self.params
        cp = self.cooked_params
        vm_underlay_dip = ipaddress.ip_address(p.PAL)

        for eni_index, eni in enumerate(range(p.ENI_START, p.ENI_START + p.ENI_COUNT * p.ENI_STEP, p.ENI_STEP)):
            vm_underlay_dip = vm_underlay_dip + int(ipaddress.ip_address(p.IP_STEP1))

            self.numYields += 1
            inbound_routing_data = {
                'name': 'inbound_routing_#%d' % eni,
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'eni_id': '%d' % eni,
                    'vni': '%d' % eni
                },
                'attributes': [
                    'SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION',
                    'SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP_PA_VALIDATE',
                    'SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID',
                    '$vnet_1'
                ]
            }

            yield inbound_routing_data


if __name__ == '__main__':
    conf = InboundRouting()
    common_main(conf)
