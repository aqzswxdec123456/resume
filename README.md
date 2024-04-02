

## 環境
* Linux centos 7
* [Python](https://www.python.org/downloads/) >= 3.6
* MariaDB >= 10.4

## Python 安裝參考
```bash
yum install wget unzip epel-release gcc gcc-c++ zlib-devel bzip2-devel openssl-devel -y
yum install ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel make -y

wget https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tgz
tar -zxvf Python-3.9.16.tgz
cd Python-3.9.16
./configure prefix=/usr/local/python3
make && make install
ln -s /usr/local/python3/bin/python3.9 /usr/bin/python3 
ln -s /usr/local/python3/bin/pip3.9 /usr/bin/pip3
```

## 套件
* django
```bash
pip3 install django
```

## MariaDB 安裝參考
```bash
# /etc/yum.repos.d/MariaDB.repo
[mariadb]
name = MariaDB
baseurl = https://tw1.mirror.blendbyte.net/mariadb/yum/10.4/centos/$releasever/$basearch
module_hotfixes = 1
gpgkey = https://tw1.mirror.blendbyte.net/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck = 1

# 安裝套件
yum install MariaDB-server MariaDB-client mariadb-devel -y

# 服務啟用
systemctl start mariadb
systemctl enable mariadb
systemctl status mariadb
```

# resume
透過 Python - Django 打造簡易履歷

