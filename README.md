# Ansible Collection - radiorabe.rabe_zabbix

GitOps our Zabbix. This is where the base of our Zabbix installation and core configuration lives.

You can find the Zabbix templates that the system built with this collection uses in the [RaBe Zabbix](https://radiorabe.github.io/rabe-zabbix/) project.

## Plugins

### Modules

* [`zabbix_host_maintenance`](https://github.com/radiorabe/ansible-collection-rabe_zabbix/blob/main/plugins/modules/zabbix_host_maintenance.py) For setting and unsetting a hosts maintenance flag

## Roles

* [`agent`](https://github.com/radiorabe/ansible-collection-rabe_zabbix/tree/main/roles/agent) Opinionated agent install with Foreman and FreeIPA
* [`config`](https://github.com/radiorabe/ansible-collection-rabe_zabbix/tree/main/roles/config) Configure Zabbix via API and install our template collection
* [`maintenance_start`](https://github.com/radiorabe/ansible-collection-rabe_zabbix/tree/main/roles/maintenance_start) Set the maintenance flag on a host
* [`maintenance_stop`](https://github.com/radiorabe/ansible-collection-rabe_zabbix/tree/main/roles/maintenance_stop) Unset the maintenance flag on a host if it was set by `maintenance_start`

## License

This collection is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, version 3 of the License.
