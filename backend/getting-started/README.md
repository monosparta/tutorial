---
title: 使用 Vagrant 建立 LAMP 開發環境
subtitle: Monosparta 軟體開發實戰訓練
papersize: A4
margin-left: 20mm
margin-right: 25mm
margin-top: 10mm
margin-bottom: 20mm
css: pandoc.css
---

安裝 VirtualBox

```bash
brew install virtualbox virtualbox-extension-pack
```

安裝 Vagrant

```bash
brew install vagrant
```

建立 Vagrantfile

```bash
mkdir hello-laravel
cd hello-laravel
vagrant init ubuntu/focal64
```

建立虛擬機器

```bash
vagrant up
```

使用 SSH 存取虛擬機器

```bash
vagrant ssh
```

安裝 PHP 開發環境

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install mysql-server
sudo apt-get install phpmyadmin
```

建立 Laravel 專案

1. [https://getcomposer.org/download/](https://getcomposer.org/download/)
2. [https://laravel.com/docs/8.x/installation](https://laravel.com/docs/8.x/installation)
3. [https://laravel.com/docs/8.x/starter-kits](https://laravel.com/docs/8.x/starter-kits)
4. [https://github.com/nodesource/distributions/blob/master/README.md](https://github.com/nodesource/distributions/blob/master/README.md)

```bash
composer create-project laravel/laravel example-app
cd example-app
composer require laravel/breeze --dev
php artisan breeze:install vue
npm install
npm run dev
php artisan migrate
```

上面的 migrate 需要正確配置資料庫才能通過

```bash
sudo mysql -uroot -e 'CREATE DATABASE laravel;'
```

編輯 `.env` 設定，資料庫帳號密碼用 `sudo cat /etc/mysql/debian.cnf` 查詢

```bash
DB_USERNAME=debian-sys-maint
DB_PASSWORD=axnUXEqsztD4fCjf
```

再執行一次 migrate

```bash
php artisan migrate
```

確認 Laravel 專案啟動成功

```bash
php artisan serve

# 如果瀏覽器打不開，試試加上 --host 參數
php artisan serve --host=0.0.0.0
```

建立 SSH Key

如果本地沒有 `~/.ssh/id_rsa` 和 `~/.ssh/id_rsa.pub` 檔案，先用 `ssh-keygen` 建立一組。

```bash
ssh-keygen
```

編輯 Vagrantfile

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.box_check_update = true

  config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "2048"
  end

  config.ssh.insert_key = false
  config.ssh.private_key_path = ['~/.vagrant.d/insecure_private_key', '~/.ssh/id_rsa']
  config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"
  config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/id_rsa.pub"
  config.vm.provision "file", source: "~/.ssh/id_rsa", destination: "~/.ssh/id_rsa"

  config.vm.provision "shell", inline: <<-SHELL
    sudo sed -i -e "\\#PasswordAuthentication yes# s#PasswordAuthentication yes#PasswordAuthentication no#g" /etc/ssh/sshd_config
    sudo systemctl restart sshd.service
    echo "finished"
  SHELL

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get -y upgrade
    DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server libapache2-mod-php php php-cli php-common php-mysql php-xml php-gd php-opcache php-mbstring php-tokenizer php-json php-bcmath php-zip unzip
    curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer
    curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
    DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs
  SHELL

end
```

確認 ssh 可以直接連線

```bash
ssh vagrant@localhost -p 2222
```

設置 VirtualBox Remote

1. Remote Development using SSH
[https://code.visualstudio.com/docs/remote/ssh](https://code.visualstudio.com/docs/remote/ssh)

確認 `~/.ssh/config` 有以下的配置。

```bash
Host localhost
  HostName localhost
  User vagrant
  Port 2222
  ForwardAgent yes
```