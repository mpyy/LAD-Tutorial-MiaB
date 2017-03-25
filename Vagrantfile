# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "trusty64"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  config.vm.network "public_network", type: "dhcp"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "saltstack/etc", "/srv/salt"
  config.vm.synced_folder "project", "/project"

  # Configure our server to use "Salt"
  config.vm.provision :salt do |salt|
    # Run salt independently without requring a central management
    # "master" server.
    salt.masterless = true

    # Tell it to use our minion config file "minion".
    salt.minion_config = "saltstack/etc/minion"

    # After the server boots, run the salt states to defined in the
    # "salt" directory.
    salt.run_highstate = true
  end # End of Salt config.
end # End of Vagrant config.
