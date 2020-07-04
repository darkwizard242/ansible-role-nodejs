[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-nodejs.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-nodejs) ![Ansible Role](https://img.shields.io/ansible/role/47706?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47706?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47706?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-nodejs&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-nodejs) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-nodejs?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-nodejs?color=orange&style=flat-square)

# Ansible Role: nodejs

Role to install (_by default_) [nodejs](https://github.com/nodejs/node) package or uninstall (_if passed as var_) on Debian based systems and EL based systems. **nodejs** is a JavaScript runtime environment. **npm** & **npx** are also installed as part of this role. The default version is set to install version `14.x` of NodeJS unless explicitly specified to install any other specific version as the repository's source is based on that.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
nodejs_app: nodejs
nodejs_app_desired_state: present
nodejs_version: 14.x

# Debian family based
nodejs_debian_pre_reqs:
  - apt-transport-https
  - gnupg
nodejs_debian_pre_reqs_desired_state: present
nodejs_repo_debian_gpg_key: https://deb.nodesource.com/gpgkey/nodesource.gpg.key
nodejs_repo_debian: "deb https://deb.nodesource.com/node_{{ nodejs_version }} {{ ansible_lsb['codename'] }} main"
nodejs_repo_debian_filename: "{{ nodejs_app }}"
nodejs_repo_debian_desired_state: present

# EL family based
nodejs_repo_el: "https://rpm.nodesource.com/pub_{{ nodejs_version }}/el/{{ ansible_distribution_major_version }}/$basearch"
nodejs_repo_el_name: nodesource
nodejs_repo_el_description: Node.js EL Family Repo
nodejs_repo_el_gpgkey: https://rpm.nodesource.com/pub/el/NODESOURCE-GPG-SIGNING-KEY-EL
nodejs_repo_el_gpgcheck: yes
nodejs_repo_el_enabled: yes
nodejs_repo_el_filename: "{{ nodejs_app }}"
nodejs_repo_el_desired_state: present
```

### Variables table:

Variable                             | Value (default)                                                                                             | Description
------------------------------------ | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
nodejs_app                           | nodejs                                                                                                      | Name of nodejs application package require to be installed i.e. `nodejs`
nodejs_app_desired_state             | present                                                                                                     | State of the nodejs_app package. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
nodejs_version                       | 14.x                                                                                                        | Version of NodeJS to install.
nodejs_debian_pre_reqs               | apt-transport-https, gnupg                                                                                  | NodeJS recommends the installation of both these packages on Debian family systems and as such, they are considered pre-requisites.
nodejs_debian_pre_reqs_desired_state | present                                                                                                     | Desired state for NodeJS pre-requisite apps on Debian family systems.
nodejs_repo_debian_gpg_key           | <https://deb.nodesource.com/gpgkey/nodesource.gpg.key>                                                      | NodeJS GPG key required on Debian family systems
nodejs_repo_debian                   | deb <https://deb.nodesource.com/node_{{> nodejs_version }} {{ ansible_lsb['codename'] }} main               | NodeJS repo URL for Debain family systems. Utilized facts such as `ansible_lsb['codename']`.
nodejs_repo_debain_filename          | "{{ nodejs_app }}"                                                                                          | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
nodejs_repo_debian_desired_state     | present                                                                                                     | `present` indicates creating the repository file if it doesn't exist on Debian based systems. Alternative is `absent` (not recommended as it will prevent from installation of **nodejs** package).
nodejs_repo_el                       | <https://rpm.nodesource.com/pub_{{> nodejs_version }}/el/{{ ansible_distribution_major_version }}/$basearch | Repository `baseurl` for NodeJS on EL based systems. Utilizes `ansible_distribution_major_version` ansible fact to set appropriate version of EL system.
nodejs_repo_el_name                  | nodesource                                                                                                  | Repository name for NodeJS on EL based systems.
nodejs_repo_el_description           | Node.js EL Family Repo                                                                                      | Description to be added in EL based repository file for NodeJS.
nodejs_repo_el_gpgkey                | <https://rpm.nodesource.com/pub/el/NODESOURCE-GPG-SIGNING-KEY-EL>                                           | NodeJS GPG key required on EL family systems
nodejs_repo_el_gpgcheck              | yes                                                                                                         | Boolean for whether to perform gpg check against NodeJS on EL based systems.
nodejs_repo_el_enabled               | yes                                                                                                         | Boolean to set so that NodeJS repository is enabled on EL based systems.
nodejs_repo_el_filename              | "{{ nodejs_app }}"                                                                                          | Name of the repository file that will be stored at `/yum/sources.list.d/nodejs.repo` on EL based systems.
nodejs_repo_el_desired_state         | present                                                                                                     | `present` indicates creating the repository file if it doesn't exist on EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **nodejs** package).

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **nodejs** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.nodejs
```

For customizing behavior of role (i.e. installing a 12.x as an example) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.nodejs
  vars:
    nodejs_version: 12.x
```

For customizing behavior of role (i.e. un-installation of **nodejs** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.nodejs
  vars:
    nodejs_apps_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-nodejs/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
