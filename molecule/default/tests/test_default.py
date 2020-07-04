import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nodejs_package_installed(host):
    assert host.package("nodejs").is_installed


def test_nodejs_binary_exists(host):
    assert host.file('/usr/bin/node').exists


def test_nodejs_binary_file(host):
    assert host.file('/usr/bin/node').is_file


def test_npm_binary_exists(host):
    assert host.file('/usr/bin/npm').exists


def test_npm_binary_file(host):
    assert host.file('/usr/bin/npm').is_file


def test_npx_binary_exists(host):
    assert host.file('/usr/bin/npx').exists


def test_npx_binary_file(host):
    assert host.file('/usr/bin/npx').is_file


def test_nodejs_repo_exists(host):
    assert host.file('/etc/apt/sources.list.d/nodejs.list').exists or \
      host.file('/etc/yum.repos.d/nodejs.repo').exists


def test_nodejs_repo_file(host):
    assert host.file('/etc/apt/sources.list.d/nodejs.list').is_file or \
      host.file('/etc/yum.repos.d/nodejs.repo').is_file


def test_nodejs_binary_which(host):
    assert host.check_output('which node') == '/usr/bin/node'


def test_npm_binary_which(host):
    assert host.check_output('which npm') == '/usr/bin/npm'


def test_npx_binary_which(host):
    assert host.check_output('which npx') == '/usr/bin/npx'
