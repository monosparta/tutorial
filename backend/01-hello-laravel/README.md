---
title: 本週實作目標 - 後端開發起手式
subtitle: Monosparta 軟體開發實戰訓練
papersize: A4
margin-left: 20mm
margin-right: 25mm
margin-top: 10mm
margin-bottom: 20mm
css: pandoc.css
---

Monosparta 第一階段的培訓中，目標是動手完成一個包含前端與後端實作的 Web-based Application，使用 Git 進行版本控管，加入自動化建置與測試，以及使用 GitLab CI / CD 實現持續整合與部署的開發流程，這是目前業界許多專業軟體開發團隊採用的方法。

為降低開發難度，後端我們選擇 PHP Laravel 8 實現快速開發，並搭配廣泛被採用的 Ubuntu Server 模擬正式伺服器，這套方法未來可以應用在三大主流雲端運算平台，包括 AWS、Azure 與 GCP 的部署。

請依照以下的單元順序，動手完成你的第一個實作練習。

1. 使用 VirtualBox 建立新的虛擬機器
2. 安裝 Ubuntu Server 20.04 LTS 至虛擬機器
3. 透過 SSH 連線至虛擬 Linux 伺服器
4. 透過 apt-get 安裝套件，建置 LAMP 開發環境（Apache + MySQL + PHP）
5. 使用 VSCode 的 Remote - SSH 延伸套件，連線至虛擬 Linux 伺服器（以下皆透過 VSCode 在遠端虛擬伺服器操作）
6. 使用 Starter Kit 建立 Laravel Breeze 專案，前端使用 Vue 框架
7. 使用 Git 將新建的專案 Commit 與 Push 至 Monosparta GitLab

如果遇到問題，請不必擔心，在培訓過程中，你可以在 Slack 上提問，我們也會陸續提供教學，協助你克服每個難關。
