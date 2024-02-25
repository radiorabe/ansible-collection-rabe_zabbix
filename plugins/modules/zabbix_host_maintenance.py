#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) hairmare@rabe.ch
# GNU General Public License v3.0+ (https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.community.zabbix.plugins.module_utils.base import ZabbixBase  # noqa: E501
import ansible_collections.community.zabbix.plugins.module_utils.helpers as zabbix_utils  # noqa: E501


__metaclass__ = type


RETURN = r"""
---
hostids:
  type: list
"""

DOCUMENTATION = r"""
---
module: zabbix_host_maintnenace
short_description: Set and unset the maintenance flag.
description:
    - Set and unset maintenance flag on individual hosts by id
author:
    - "Lucas Bickel <hairmare@rabe.ch>"
requirements:
    - "python >= 3.9"
options:
    hostid:
        description:
            - Host ID
        required: true
        type: str
    maintenance:
        description:
            - Maintenance flag
        required: true
        type: bool

extends_documentation_fragment:
- community.zabbix.zabbix
"""

EXAMPLES = r"""
# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  ansible.builtin.set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  ansible.builtin.set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Set host maintenance
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  radiorabe.rabe_zabbix.zabbix_host_maintenance:
    hostid: "1"
    maintenance: true # or false to unset
"""  # noqa: E501


class HostUpdate(ZabbixBase):
    def set_maintenance(self, hostid: str, maintenance: bool):
        return self._zapi.host.update(
            {
                "hostid": hostid,
                "maintenance_status": {True: "1", False: "0"}[maintenance],
            }
        )


def main():
    argument_spec = zabbix_utils.zabbix_common_argument_spec()
    argument_spec.update(
        dict(
            hostid=dict(type="str", required=True),
            maintenance=dict(type="bool", required=True),
        )
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
    )

    updater = HostUpdate(module)
    result = updater.set_maintenance(
        module.params["hostid"], module.params["maintenance"]
    )
    module.exit_json(changed=True, result=result)


if __name__ == "__main__":
    main()
