#!/bin/bash
# LOG=sms.log
echo "hello world 1" >> test.log 

# Environment variables
frontend_name=rocky-no-slurm-head
compute_prefix="rocky-no-slurm"
first_node=1
last_node=4
compute_group_name="compute"
ip_vlan="10.203.80."
DNS1="10.142.7.1"
DNS2="10.132.7.2"
compute_ip_start=165
num_computes=4
num_sockets=2
cores_per_socket=12
threads_per_core=1
 
# [FRONTEND]
# Check FRONTEND's Network
# less /etc/sysconfig/network-scripts/ifcfg-ens192
echo "nameserver ${DNS1}" >> /etc/resolv.conf
echo "nameserver ${DNS2}" >> /etc/resolv.conf
# systemctl restart network-online.target

echo "$(date +%T) 1. Change head name"
# echo ${sms_ip} ${frontend_name} >> /etc/hosts
hostnamectl set-hostname ${frontend_name}
 
echo "$(date +%T) 2. install xCAT"
# [FRONTEND]
# Disable SELINUX
setenforce Permissive
echo "Disable SELINUX?"
## Enable xCat's Public repo
dnf install -y wget
wget -P /etc/yum.repos.d https://xcat.org/files/xcat/repos/yum/latest/xcat-core/xcat-core.repo
## Enable the repo of xCat's dependent package for local use
wget -P /etc/yum.repos.d https://xcat.org/files/xcat/repos/yum/xcat-dep/rh8/x86_64/xcat-dep.repo
dnf -y install xCAT >> test.log
## enable xCAT tools for use in current shell
. /etc/profile.d/xcat.sh
# Add provisioned VMs (compute nodes) to xCat's database
for ((i=$first_node; i <= $last_node; i++)); do mkdef -t node $compute_prefix$i groups=$compute_group_name,all ip=$ip_vlan$(( i + compute_ip_start)) arch=x86_64; done
# Add compute nodes to /etc/hosts
for ((i=$first_node; i <= $last_node; i++)); do echo "$ip_vlan$(( i + compute_ip_start)) $compute_prefix$i" >> /etc/hosts; done

echo "$(date +%T) 2.1 Change compute nodes name"
for ((i=$first_node; i <= $last_node; i++)); do xdsh $compute_prefix$i hostnamectl set-hostname $compute_prefix$i; done
# Sync DNS files to all compute nodes
xdcp $compute_group_name /etc/resolv.conf /etc/resolv.conf
xdsh $compute_group_name systemctl restart network-online.target
xdsh $compute_group_name hostname | sort
# Sync hosts file
xdcp $compute_group_name /etc/hosts /etc/

echo "$(date +%T) 2.2 Disable the Firewall for head and the compute Node"
systemctl disable firewalld.service
xdsh $compute_group_name systemctl disable firewalld.service

# [FRONTEND]
echo "$(date +%T) 4. Install OpenHPC repo on FrontEnd"
dnf -y install http://repos.openhpc.community/OpenHPC/2/CentOS_8/x86_64/ohpc-release-2-1.el8.x86_64.rpm
# Install OpenHPC repo on all compute nodes
xdsh $compute_group_name dnf -y install http://repos.openhpc.community/OpenHPC/2/CentOS_8/x86_64/ohpc-release-2-1.el8.x86_64.rpm