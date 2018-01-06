#!/bin/bash

vagrant up --provider=azure

fab -f despliegue/fabfile.py -H vagrant@maquinaagendalearning.southcentralus.cloudapp.azure.com RemoveApp
fab -f despliegue/fabfile.py -H vagrant@maquinaagendalearning.southcentralus.cloudapp.azure.com InstallApp
fab -f despliegue/fabfile.py -H vagrant@maquinaagendalearning.southcentralus.cloudapp.azure.com StartApp


