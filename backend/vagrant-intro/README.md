---
title: 使用 Vagrant 建立 Laravel 開發環境
subtitle: Monosparta 軟體開發實戰訓練
papersize: A4
margin-left: 20mm
margin-right: 25mm
margin-top: 10mm
margin-bottom: 20mm
css: pandoc.css
---

## 認識 Vagrant

軟體開發者需要經常為開發環境建立專用的虛擬機器，儘管 VirtualBox 的操作並不困難，但是反覆操作相同的流程，對於擅長寫程式把任務自動化的開發者來說，你是否也覺得一件事如果需要重複做 2 次以上，就應該把它自動化呢？

Infrastructure as Code（簡稱 IaC）觀念有愈來愈多實踐 DevOps 的團隊採用，我們也可以將 IaC 實際應用於開發與測試階段所需的環境建立，簡單地說，只要用代碼定義一次專案執行所需要的虛擬機器配置，日後就可以用自動化程序幫你重建所需的虛擬機器。

Vagrant 是由 HashiCorp 開發的虛擬機器（Virtual Machine）管理工具，只要你先寫好一組名為 Vagrantfile 的設定檔，日後就可以方便地用它快速建立符合需求的虛擬機器。

## 安裝 Vagrant

Vagrant 支援在 macOS、Windows 與 Linux 上執行，我們建議使用套件管理工具（brew 或 apt-get）簡化安裝與升級管理。

https://www.vagrantup.com/downloads

## 搜尋 Vagrant Box

由官方或其他開發者預先配置好的 Vagrant 套件被稱為 Box，你可以在 Vagrant 官方平台上找到已經發佈的 Box 們。

https://app.vagrantup.com/boxes/search

例如 Ubuntu Linux 已經有許多立即可用的 Vagrant Box。

https://app.vagrantup.com/ubuntu

因此如果你希望打造一個 Ubuntu Linux 20.04 LTS 虛擬機器，只要使用 `ubuntu/focal64` 這個 Box 即可。

https://app.vagrantup.com/ubuntu/boxes/focal64

## 開始使用 Vagrant

使用 Vagrant 快速建立一組 Ubuntu Linux 20.04 LTS 虛擬機器，只要

``` bash
vagrant init ubuntu/focal64
vagrant up
```

接著你就可以先去泡杯咖啡，等待讓 Vagrant 自動幫你建立虛擬機器。

使用 SSH 登入到已經建立好的虛擬機器：

``` bash
vagrant ssh
```

先幫 Ubuntu 更新套件吧！

``` bash
sudo apt-get update
sudo apt-get upgrade
```

透過 Vagrant 管理虛擬機器，大幅節省了每次重建虛擬機器所需的時間，你也可以隨時將虛擬機器移除，藉此節省有限的磁碟空間。

``` bash
vagrant destroy
```

日後只要使用 `vagrant up` 就能再次重建虛擬機器。

請試著開始改用 Vagrant 管理你的虛擬機器吧！
