#!/bin/bash -eux

# Update yum cache etc
sudo yum -y update

# Install Go
sudo yum -y install git cpp gcc golang-src golang-bin mpfr libmpc golang

# Prepare Go-workspace
mkdir -p /opt/go-workspace
export GOPATH=/opt/go-workspace/
mkdir -p $GOPATH/bin
mkdir -p $GOPATH/pkg
mkdir -p $GOPATH/src
mkdir -p $GOPATH/src/github.com

# Setup Go Path in profile and then reload
echo -e "export GOPATH=/opt/go-workspace/ PATH=$PATH:$GOPATH/bin:$GOPATH/src" | tee ~/.bash_profile ~/.bashrc
. ~/.bash_profile
source ~/.bash_profile

# Prepare and install beego libraries
 git config --global http.sslVerify false
 go get github.com/astaxie/beego
