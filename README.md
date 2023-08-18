[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/wwt/ansible-meraki-demo) [![Run in Cisco Cloud IDE](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/codeexchange/devenv/wwt/ansible-meraki-demo/)

# ansible-meraki-demo

This repository contains sample Ansible Playbooks and Event-Driven Ansible Rulebooks as demonstrated during the **"Using Ansible to automate edge site infrastructure at scale"** talk delivered in Red Hat's booth during Cisco Live US 2023.

## Details

### Included Playbooks

* `claim_devices.yml` - Claim Meraki Devices, Orders, or Licenses into your Meraki Dashboard.
* `configure_network.yml` - Uses `wwt.meraki` Ansible collection to provision demo environment.
* `unconfigure_demo.yml` - Calls `remove_mqtt.yml` and `remove_network.yml` to tear down Demo Environment in the proper order.
* `send_webex_message.yml` - Captures Meraki MV Camera snapshot and sends a Webex Teams message.  Called from Event-Driven Ansible.

### Included Rulebooks

* `rulebooks/mt30-mqtt-rulebook.yml` - Listens for MQTT Messages from Meraki MT30 sensor and triggers environment tear down or camera snapshot.

### .env Example

* `ENVEXAMPLE` - Example .env file to be used if using `ansible-playbook` to run playbooks.

## Contributors

Nick Thompson - <https://github.com/nsthompson>
