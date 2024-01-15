# Ansible Role - radiorabe.rabe_zabbix.data_collection

Manages Infrastructure in Zabbix using Foreman.

## Role Variables

This role does not expose any variables.

## Dependencies

The `radiorabe.rabe_zabbix.data_collection` role depends on the [`community.zabbix`](https://galaxy.ansible.com/community/zabbix/) collection.

## Example Playbooks

```yaml
- name: Configure Zabbix Data Collection
  hosts: localhost
  gather_facts: false
  roles:
    - role: radiorabe.rabe_zabbix.data_collection
```

## License

This role is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, version 3 of the License.
