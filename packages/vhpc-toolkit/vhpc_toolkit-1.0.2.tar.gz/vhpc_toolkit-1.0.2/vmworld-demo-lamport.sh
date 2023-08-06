./vhpc_toolkit clone --vm a-redhatos8-template --template tp-cluster1-n01 --cluster hpcml-compute --datastore vsanDatastore --linked

#1. Preparation
pwd
source venv/bin/activate
cp config/vCenter-lamport.conf config/vCenter.conf 
cd bin
./vhpc_toolkit view

#2. Clone a new VM from an existing VM using linked clone
./vhpc_toolkit clone --vm A-vmworld-demo-01 --template a-redhatos8-template --cluster hpcml-compute --datastore vsanDatastore --linked

#3. Power off and change the CPU and memory of that VM
./vhpc_toolkit power --vm A-vmworld-demo-01 --off
./vhpc_toolkit cpumem --vm A-vmworld-demo-01 --cpu 8 --memory 32 --cpu_reservation y --memory_reservation y

#4. Network
./vhpc_toolkit network --vm A-vmworld-demo-01 --add --port_group DSwitch-VMNetwork
	# static IP
./vhpc_toolkit network_cfg --vm A-vmworld-demo-01 --port_group DSwitch-VMNetwork --ip 10.203.80.49 --netmask 255.255.255.0 --gateway 10.203.80.253 --dns 10.142.7.1 --domain eng.vmware.com

#5. Power that VM on
./vhpc_toolkit power --vm A-vmworld-demo-01 --on
ping 10.203.80.49

#6. Remove that VM
./vhpc_toolkit destroy --vm A-vmworld-demo-01

#7. Create a virtual cluster
./vhpc_toolkit cluster --create --file ../examples/cluster-scripts/cluster-simple-lamport.conf

#8. Destroy the virtual cluster
./vhpc_toolkit cluster --destroy --file ../examples/cluster-scripts/cluster-simple-lamport.conf