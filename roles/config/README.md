# Ansible Role - radiorabe.rabe_zabbix.config

Manages Infrastructure in Zabbix using Foreman.

## Role Variables

| Variable | Default |
| -------- | ------- |
| `radiorabe_zabbix_prefix` | `'RaBe: '` |
| `radiorabe_zabbix_mod_name` | `'Manager on Duty'` |
| `radiorabe_zabbix_categories` | See [defaults](./defaults/main.yml) |

## Dependencies

The `radiorabe.rabe_zabbix.config` role depends on the [`community.zabbix`](https://galaxy.ansible.com/community/zabbix/) collection.

## Example Playbooks

```yaml
- name: Configure Zabbix Data Collection
  hosts: localhost
  gather_facts: false
  roles:
    - role: radiorabe.rabe_zabbix.config
```

## License

This role is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, version 3 of the License.
