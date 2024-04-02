# 簡介
* [前端來源 - 第三個項目](https://medium.com/@trista_liu/2018%E5%B9%B4%E6%9C%80%E5%A5%BD%E7%94%A8%E7%9A%8420%E5%80%8Bbootstrap%E7%B6%B2%E7%AB%99%E6%A8%A1%E6%9D%BF-e99772f8ae38)
* 透過 Python - Django 打造簡易履歷

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

# 建立專案 假設我放在 /opt 底下
django-admin startproject dev_resume
cd dev_resume

# 進入專案以後 建立APP
python3 manage.py startapp resume
```

## 配置 專案
* 取得 git 倉庫
```bash
# 假設我放在 tmp 底下
git clone https://github.com/aqzswxdec123456/resume.git

```

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
覆蓋專案 url，假設專案與APP不是以下名稱，可自行修改
```bash
\cp -f /tmp/resume/project/urls.py /opt/dev_resume/dev_resume/urls.py
```

## 配置 APP
可以自行配置，以下內容都是參考用
* admin.py
* models.py
* urls.py
* views.py
```bash
\cp -f /tmp/resume/app/admin.py /opt/dev_resume/resume/admin.py
\cp -f /tmp/resume/app/models.py /opt/dev_resume/resume/models.py
\cp -f /tmp/resume/app/urls.py /opt/dev_resume/resume/urls.py
\cp -f /tmp/resume/app/views.py /opt/dev_resume/resume/views.py
```

* 建立前端，也可自行配置
```bash
# 配置 html
mkdir -p /opt/dev_resume/resume/templates/dev_resume
\cp -f /tmp/resume/web/*.html /opt/dev_resume/resume/templates/dev_resume

# 配置 css、js
mkdir -p /opt/dev_resume/resume/static
unzip /tmp/resume/startbootstrap-resume-gh-pages.zip -d /tmp/resume/
\cp -rf /tmp/resume/startbootstrap-resume-gh-pages/{assets,css,js} /opt/dev_resume/resume/static
```

## 建立 database
```bash
CREATE DATABASE dev_resume CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
``` 

## 匯入 database
```bash
cd /opt/dev_resume/
python3 manage.py makemigrations
python3 manage.py migrate
\cp -f /tmp/resume/csv/resume.py /opt/dev_resume/
python3 resume.py 1 /tmp/resume/csv/personal_info.csv
python3 resume.py 2 /tmp/resume/csv/work_experience.csv
python3 resume.py 3 /tmp/resume/csv/education.csv
python3 resume.py 4 /tmp/resume/csv/skills_tree.csv
``` 

## 運行
```bash
python3 manage.py runserver 0.0.0.0:443
# 開啟 url http://172.31.11.23:443/resume/
```
