

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

## Python 套件
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

## Django 指令
```bash
# 設定指令可以使用
ls /usr/local/python3/bin/django-admin
export PATH=$PATH:/usr/local/python3/bin
source ~/.bashrc

# 建立專案
django-admin startproject dev_resume
cd dev_resume

# 進入專案以後 建立APP
python3 manage.py startapp resume
```

## 配置 專案
* settings.py
```bash
# 修改語系、時區 
sed -i "s|en-us|zh-Hant|g" dev_resume/settings.py
sed -i "s|UTC|Asia/Taipei|g" dev_resume/settings.py

# 修改 APP 配置
sed -i "/'django.contrib.staticfiles',/a \    'resume'," dev_resume/settings.py

# 修改 HTTP_HOST
sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = ['*']/" dev_resume/settings.py

# 修改DB連線資訊 這邊假設 登入資訊：root/123456 端口：3306 Host：本地 Database：dev_resume
sed -i "/'default': {/,/    }/d" dev_resume/settings.py
sed -i "/DATABASES = {/a \    'default': {\n        'ENGINE': 'django.db.backends.mysql',\n        'NAME': 'dev_resume',\n        'USER': 'root',\n        'PASSWORD': '123456',\n        'HOST': 'localhost',\n        'PORT': '3306',\n        'OPTIONS': {\n            'init_command': \"SET sql_mode='STRICT_TRANS_TABLES'\",\n            'charset': 'utf8mb4',\n        },\n    }" dev_resume/settings.py

```
* urls.py
```bash
# 修改語系、時區 


```

## 配置 APP
* django
```bash
# 配置 html
mkdir -p dev_resume/templates/dev_resume
touch dev_resume/templates/dev_resume/resume.html
```

# resume
透過 Python - Django 打造簡易履歷

