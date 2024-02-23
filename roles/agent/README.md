# Ansible Role - radiorabe.rabe_zabbix.agent

Opinionated Zabbix agent installation

* installs Zabbix Agent2 without enabling any repos
* configures a client cert using [`rhel.rhel_system_roles.certificate`](https://github.com/linux-system-roles/certificate) with certmonger and configures the agent to use it
* centralizes the server config for agents and ensure that they are configured for native mTLS
* built for use with [Foreman Ansible](https://theforeman.org/plugins/foreman_ansible/2.x/index.html).

## Role Variables

| Variable | Default |
| -------- | ------- |
| `radiorabe_zabbix_agent_server` | `monitoring.service.int.rabe.ch` |
| `radiorabe_zabbix_agent_serveractive | `monitoring.service.int.rabe.ch` |

### Other Variables

| Variable | Default |
| -------- | ------- |
| `foreman.foreman_fqdn` | from [Foreman](https://theforeman.org/) |
| `radiorabe_core_int_hostname` | from [`radiorabe.common.core`](https://github.com/radiorabe/ansible-collection-common/tree/main/roles/core) |

## Dependencies

The `radiorabe.rabe_zabbix.agent` role depends on the [`community.zabbix`](https://galaxy.ansible.com/community/zabbix/) and [`fedora.linux_system_roles`](https://galaxy.ansible.com/fedora/linux_system_roles) collections.

## Example Playbooks

```yaml
- name: Configure Zabbix Agent
  hosts: localhost
  gather_facts: false
  roles:
    - role: radiorabe.rabe_zabbix.agent
```

## License

This role is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, version 3 of the License.
