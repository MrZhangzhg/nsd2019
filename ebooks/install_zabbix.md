groupadd zabbix
useradd -g zabbix zabbix
yum install mariadb-server
systemctl start mariadb
systemctl enable mariadb
mysql -uroot
CREATE DATABASE zabbix DEFAULT CHARSET utf8;
GRANT ALL ON *.* TO 'zabbix'@'%' IDENTIFIED BY 'zabbix';
GRANT ALL ON *.* TO 'zabbix'@'localhost' IDENTIFIED BY 'zabbix';
yum install -y httpd gd php php-ctype php-xml php-xmlreader php-xmlwriter php-session php-net-socket php-mbstring php-gettext php-ldap mariadb-devel libxml2-devel.x86_64 net-snmp-devel libcurl-devel.x86_64 php-mysql php-gd
rpm -ihv libevent-devel-2.0.21-4.el7.x86_64.rpm php-bcmath-5.4.16-42.el7.x86_64.rpm php-fpm-5.4.16-42.el7.x86_64.rpm php-mbstring-5.4.16-42.el7.x86_64.rpm
tar xf zabbix-3.4.4.tar.gz
cd zabbix-3.4.4/
./configure --enable-server --enable-agent --with-mysql --enable-ipv6 --with-net-snmp --with-libcurl --with-libxml2
make install
cp -r frontends/php/ /var/www/html/zabbix
chown -R apache.apache /var/www/html/zabbix/
cd database/mysql/
mysql -uzabbix -pzabbix zabbix < schema.sql
mysql -uzabbix -pzabbix zabbix < images.sql
mysql -uzabbix -pzabbix zabbix < data.sql
cd ../..
cp misc/init.d/fedora/core/* /etc/init.d/
vim /usr/local/etc/zabbix_server.conf
DBHost=localhost
DBName=zabbix
DBUser=zabbix
DBPassword=zabbix
DBPort=3306
service zabbix_server start
chkconfig zabbix_server on
vim /etc/php.ini
post_max_size = 16M
max_execution_time = 300
max_input_time = 300
date.timezone = Asia/Shanghai


systemctl start httpd
systemctl enable httpd

