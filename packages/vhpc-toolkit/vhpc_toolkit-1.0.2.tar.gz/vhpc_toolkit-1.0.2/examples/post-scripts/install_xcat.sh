#!/bin/bash
# LOG=sms.log
echo "hello world 1" >> test.log 

# 2. install xCAT
# [FRONTEND]
setenforce Permissive
## Enable xCat's Public repo
wget -P /etc/yum.repos.d https://xcat.org/files/xcat/repos/yum/latest/xcat-core/xcat-core.repo
## Enable the repo of xCat's dependent package for local use
wget -P /etc/yum.repos.d https://xcat.org/files/xcat/repos/yum/xcat-dep/rh8/x86_64/xcat-dep.repo
sudo dnf -y install xCAT >> test.log
## enable xCAT tools for use in current shell
. /etc/profile.d/xcat.sh
# Add provisioned VMs (compute nodes) to xCat's database
echo "stop here" >> test2.log
