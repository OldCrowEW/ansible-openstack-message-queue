import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rabbitmq_server_is_installed(host):
    package = host.package('rabbitmq-server')

    assert package.is_installed


def test_rabbitmq_server_running_and_enabled(host):
    service = host.service('rabbitmq-server')

    assert service.is_running
    assert service.is_enabled
