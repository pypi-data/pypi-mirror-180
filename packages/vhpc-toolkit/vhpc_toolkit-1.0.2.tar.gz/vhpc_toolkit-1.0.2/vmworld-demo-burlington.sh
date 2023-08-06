#1. Preparation
pwd
cp 
source venv/bin/activate
cp config/vCenter-burlington.conf config/vCenter.conf 
cd bin
./vhpc_toolkit view

#2. Clone a new VM from an existing VM using linked clone
./vhpc_toolkit clone --vm hpc-vm-01 --template centos7_template --cluster VMworld_Demo --datastore datastore9-1 --linked

#3. Power off and change the CPU and memory of that VM
./vhpc_toolkit power --vm hpc-vm-01 --off
./vhpc_toolkit cpumem --vm hpc-vm-01 --cpu 8 --memory 32 --cpu_reservation y --memory_reservation y

#4. Add a VMXNet3 network adaptor and configure IP
./vhpc_toolkit network --vm hpc-vm-01 --add --port_group VMNetwork
./vhpc_toolkit network_cfg --vm hpc-vm-01 --port_group VMNetwork --is_dhcp --netmask 255.255.255.0 --gateway 10.118.232.253 --dns 10.118.254.1 --domain eng.vmware.com

#5. Power that VM on
./vhpc_toolkit power --vm hpc-vm-01 --on
ping 10.118.232.90

#6. Remove that VM
./vhpc_toolkit destroy --vm hpc-vm-01

#7. Create a virtual cluster
./vhpc_toolkit cluster --create --file ../examples/cluster-scripts/cluster-simple.conf

#8. Destroy the virtual cluster
./vhpc_toolkit cluster --destroy --file ../examples/cluster-scripts/cluster-simple.conf