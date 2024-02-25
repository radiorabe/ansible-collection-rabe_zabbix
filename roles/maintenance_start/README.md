# Ansible Role - radiorabe.rabe_zabbix.maintenance_start

Set the maintenance flag on a host. See `radiorabe.rabe_zabbix.maintenance_stop` for unsetting the flag.

* built for use with [Foreman Ansible](https://theforeman.org/plugins/foreman_ansible/2.x/index.html).

## Role Variables

Uses collection default vars for connecting to Zabbix.

### Other Variables

| Variable | Default |
| -------- | ------- |
| `foreman.foreman_fqdn` | from [Foreman](https://theforeman.org/) |

## Dependencies

The `radiorabe.rabe_zabbix.maintenance_start` role depends on the [`community.zabbix`](https://galaxy.ansible.com/community/zabbix/).

## Example Playbooks

```yaml
- name: Configure Zabbix Agent
  hosts: localhost
  gather_facts: false
  vars:
    rabe_zabbix_auth_key: ...
    zabbix_api_server_url: ...
    foreman:
      foreman_fqdn: ...
  roles:
    - role: radiorabe.rabe_zabbix.maintenance_start
```

## License

This role is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, version 3 of the License.
