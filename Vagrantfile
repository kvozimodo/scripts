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
  # boxes at https://vagrantcloud.com/search.
  #config.vm.box = "jenkins_main/centos-7"
  # master vm
  config.vm.define "master" do |centos_jenkins_master|
	 centos_jenkins_master.vm.box="centos/7"
		centos_jenkins_master.vm.provider :virtualbox do |v|
		v.customize ["modifyvm", :id, "--memory", 4096]
		v.customize ["modifyvm", :id, "--name", "centos_jenkins_master"]
	#	v.gui = true
	  end
	  centos_jenkins_master.vm.network "forwarded_port", guest: 80, host: 8080
	  centos_jenkins_master.vm.network "private_network",
		type:"dhcp"
	 centos_jenkins_master.vm.provision "shell", inline: <<-SHELL
	   sudo yum install wget -y
	   sudo yum install java-11-openjdk -y
	   sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
	   sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
	   sudo yum upgrade -y
	   sudo yum install jenkins java-11-openjdk-devel -y
	   sudo systemctl daemon-reload
     sudo systemctl start jenkins
	 SHELL
   end

config.vm.define "slave" do |centos_slave|
	 centos_slave.vm.box="centos/7"
		centos_slave.vm.provider :virtualbox do |v|
		v.customize ["modifyvm", :id, "--memory", 4096]
		v.customize ["modifyvm", :id, "--name", "centos_slave"]
	#	v.gui = true
	  end
	  centos_slave.vm.network "forwarded_port", guest: 8081, host: 8081
	  centos_slave.vm.network "private_network",
		type:"dhcp"
	 centos_slave.vm.provision "shell", inline: <<-SHELL 
	 sudo yum install wget -y
	 sudo yum install java-11-openjdk -y
	 SHELL
   end
end