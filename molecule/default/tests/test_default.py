import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'nodejs'
PACKAGE_BINARY = '/usr/bin/node'
NPM_BINARY = '/usr/bin/npm'
NPX_BINARY = '/usr/bin/npx'
DEBIAN_REPO_FILE = '/etc/apt/sources.list.d/nodejs.list'
EL_REPO_FILE = '/etc/yum.repos.d/nodejs.repo'


def test_nodejs_package_installed(host):
    """
    Tests if nodejs is installed.
    """
    assert host.package("nodejs").is_installed


def test_nodejs_binary_exists(host):
    """
    Tests if nodejs binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_nodejs_binary_file(host):
    """
    Tests if nodejs binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_nodejs_binary_which(host):
    """
    Tests the output to confirm nodejs's binary location.
    """
    assert host.check_output('which node') == PACKAGE_BINARY


def test_npm_binary_exists(host):
    """
    Tests if npm binary exists.
    """
    assert host.file(NPM_BINARY).exists


def test_npm_binary_file(host):
    """
    Tests if npm binary is a file type.
    """
    assert host.file(NPM_BINARY).is_file


def test_npm_binary_which(host):
    """
    Tests the output to confirm npm's binary location.
    """
    assert host.check_output('which npm') == '/usr/bin/npm'


def test_npx_binary_exists(host):
    """
    Tests if npx binary exists.
    """
    assert host.file(NPX_BINARY).exists


def test_npx_binary_file(host):
    """
    Tests if npx binary is a file type.
    """
    assert host.file(NPX_BINARY).is_file


def test_npx_binary_which(host):
    """
    Tests the output to confirm npx's binary location.
    """
    assert host.check_output('which npx') == NPX_BINARY


def test_nodejs_repo_exists(host):
    """
    Tests if nodejs repo exists on DEBIAN/EL Systems.
    """
    assert host.file(DEBIAN_REPO_FILE).exists or \
        host.file(EL_REPO_FILE).exists


def test_nodejs_repo_file(host):
    """
    Tests if nodejs repo is a file type on DEBIAN/EL Systems.
    """
    assert host.file(DEBIAN_REPO_FILE).is_file or \
        host.file(EL_REPO_FILE).is_file
