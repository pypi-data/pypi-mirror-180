echo "hello world 3" >> test3.log

# Test some commentlines
DNS1="10.142.7.1"
DNS2="10.132.7.2"

echo nameserver $DNS1 >> /etc/resolv.conf
echo nameserver $DNS2 >> /etc/resolv.conf
systemctl restart network-online.target