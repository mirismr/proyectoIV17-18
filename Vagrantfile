# -*- mode: ruby -*-
# vi: set ft=ruby :

puts ENV["AZURE_TENANT_ID"]
puts ENV["AZURE_CLIENT_ID"]
puts ENV["AZURE_CLIENT_SECRET"]
puts ENV["AZURE_SUBSCRIPTION_ID"]

Vagrant.configure('2') do |config|

  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacía
  config.vm.network "private_network",ip: "192.168.11.4", virtualbox__intnet: "vboxnet0" #Ip privada
  config.vm.hostname = "localhost"
  config.vm.network "forwarded_port", guest: 80, host: 80

  # use local ssh key to connect to remote vagrant box
  config.vm.provider :azure do |azure, override|
    config.ssh.private_key_path = '~/.ssh/id_rsa'
    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130'
    azure.vm_size = 'Basic_A0'
    azure.location = 'southcentralus'
    azure.tcp_endpoints = '80'
    azure.vm_name = "maquinaagendalearning"
    azure.resource_group_name= "agendaLearning"
    azure.tenant_id = '789922d6-0ea1-414b-9f43-801d31e3d7b1'
    #azure.tenant_id = ENV["AZURE_TENANT_ID"]
    azure.client_id = '2ca8f5dc-2ab2-4e0f-95d9-458122868fc4'
    #azure.client_id = ENV["AZURE_CLIENT_ID"]
    azure.client_secret = 'FX1eDlCZNTVx/SCj4rsZ92ws3mh+VfsEC04E2F86GMI='
    #azure.client_secret = ENV["AZURE_CLIENT_SECRET"]
    azure.subscription_id = 'bb5afabf-0460-48f9-ba84-0bc5da6f0552'
    #azure.subscription_id = ENV["AZURE_SUBSCRIPTION_ID"]


    
  end

  # Provisionar con ansible
  config.vm.provision "ansible" do |ansible|
    ansible.sudo = true
    ansible.playbook = "./playbook.yml"
    ansible.verbose = "-vvvv"

    ansible.host_key_checking = false
  end

end

