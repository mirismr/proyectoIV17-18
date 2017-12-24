#!/bin/bash

vagrant up --provider=azure

fab -H vagrant@maquinaagendalearning.southcentralus.cloudapp.azure.com RemoveApp
fab -H vagrant@maquinaagendalearning.southcentralus.cloudapp.azure.com InstallApp
fab -H vagrant@maquinaagendalearning.southcentralus.cloudapp.azure.com StartApp


