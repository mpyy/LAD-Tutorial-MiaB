# Install the packages "python3-dev" and "python-pip".
dev_packages:
    pkg.installed:
        - pkgs:
            - python3-dev
            - python-pip
            - libmysqlclient-dev

# Install "virtualenvwrapper" with pip.
dev_pip_packages:
    pip.installed:
        - pkgs:
            - virtualenvwrapper

# Create the directory for our virtual env.
/usr/local/virtualenvs:
    file.directory:
        - user: vagrant
        - group: vagrant

# Create the virtual environment.
/usr/local/virtualenvs/env:
    virtualenv.managed:
        - system_site_packages: False
        - python: python3.4
        - user: vagrant

# Setup virtualenvwrapper.
virtualenvwrapper_configuration:
    file.append:
        - name: /home/vagrant/.bashrc
        - text: |+
            WORKON_HOME=/usr/local/virtualenvs
            PROJECT_HOME=/project
            source /usr/local/bin/virtualenvwrapper.sh

# Setup virtualenvwrapper for root.
virtualenvwrapper_root_configuration:
    file.append:
        - name: /root/.bashrc
        - text: |+
            WORKON_HOME=/usr/local/virtualenvs
            PROJECT_HOME=/project
            source /usr/local/bin/virtualenvwrapper.sh

# Install the MySQL server using the root password of 'password'.
mysql_server_installed:
    debconf.set:
        - name: mysql-server
        - data:
            'mysql-server/root_password': {'type': 'string', 'value': 'password'}
            'mysql-server/root_password_again': {'type': 'string', 'value': 'password'}
    pkg.installed:
        - pkgs:
            - mysql-server

# Enable the service so MySQL starts when the server boots.
mysql_service_enabled:
    service.running:
        - name: mysql
        - enable: True

# Create a database in MySQL called 'miab_db'
create_database:
    mysql_database.present:
        - connection_user: root
        - connection_pass: 'password'
        - connection_charset: utf8
        - name: 'miab_db'
