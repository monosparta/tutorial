---
title: 安裝 VirtualBox 虛擬機器軟體
subtitle: Monosparta 軟體開發實戰訓練
papersize: A4
margin-left: 20mm
margin-right: 25mm
margin-top: 10mm
margin-bottom: 20mm
css: pandoc.css
---

VirtualBox 是一款功能強大的 x86 虛擬機器軟體，簡單說就是讓你的筆電或桌機，可以同時運行多個虛擬化的作業系統，共享同一部電腦的硬體資源。目前同樣占有市場主導地位的相似軟體，還有 VMWare 與 Hyper-V，而 VirtualBox 具備以下優點：

1. 免費且開放源碼
2. 跨平台（可以安裝於 Windows、Mac 與 Linux 作業系統）
3. 相容常見虛擬機器系統（包括 Windows、Mac、Linux、FreeBSD 與 Android 等）

雖然安裝 VirtualBox 很容易，只要在官網找到作業系統對應的安裝程式，即可完成下載安裝。

https://www.virtualbox.org/wiki/Downloads

但是對職業軟體工程師來說，我們更偏好以「Package Manager」（軟體套件管理工具），進行自動化地安裝及日後的升級維護。

目前軟體開發者常用的三大主流作業系統，皆已有發展成熟的套件管理工具，

## Linux

如果你不想換台 Mac，想把電腦重灌或灌成雙系統，那麼 Ubuntu Linux 會是很棒的選擇，我們建議你可以先嘗試 64 位元桌面版的 Ubuntu Desktop， 目前 LTS 最新版本是 20.04，安裝 LTS（長期支援）版本，對新手來說是比較穩定可靠的選擇。

下載 Ubuntu 作業系統\
https://ubuntu.com/download

Ubuntu 與 Debian 這類型的 Linux 皆內建 APT（Advanced Packaging Tools）作為系統原生的套件管理，因此可以直接使用 `apt` 或 `apt-get` 指令安裝或升級你所需要的軟體。

PS. 另一種 Linux 常見套件管理工具是 YUM，它是 RedHat、CentOS、openSUSE 內建的套件管理工具，功能與 APT 相似。

請參考 VirtualBox 官方提供關於 Linux 系統的安裝說明。

https://www.virtualbox.org/wiki/Linux_Downloads

Ubuntu Linux 本身提供 virtualbox 套件，可以直接安裝：

```bash
sudo apt update
sudo apt install virtualbox virtualbox-ext-pack
```

但如果你想安裝 VirtualBox 最新版本，則必須先設定以 VirtualBox 官方套件庫作為來源：

``` bash
echo 'deb http://download.virtualbox.org/virtualbox/debian '$(lsb_release -cs)' contrib non-free' > /etc/apt/sources.list.d/virtualbox.list

wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
```

接著再以 `apt-get` 指令進行安裝。

``` bash
sudo apt-get update
sudo apt-get install virtualbox-6.1
```

日後升級只要執行：

``` bash
sudo apt-get update
sudo apt-get upgrade
```

就會連同新版 VirtualBox（如果有更新的話）一起完成升級，非常方便管理。

## Mac

看到 Linux 有好用的 APT，那很潮的 Mac 使用者，是不是也有類似的管理工具呢？

當然有！只是不是 Apple 官方的工具，目前最多軟體開發者使用的 Mac 套件管理工具是 Homebrew。

Homebrew\
https://brew.sh/index_zh-tw

它只要輸入一行指令就能完成安裝，

``` bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

接著就能以 `brew` 指令進行安裝：

``` bash
brew install --cask virtualbox
brew install --cask virtualbox-extension-pack
```

如此一來，日後的軟體升級只要執行：

``` bash
brew update
brew upgrade
```

Homebrew 讓 Mac 使用者也能享受便利的軟體套件管理。

## Windows

看到 Linux 和 Mac 皆有方便的軟體套件管理，那 Windows 使用者呢？

在你打算重灌成 Linux 或改買 Mac 電腦前，如果你不怕踩雷、喜歡挑戰，那就試試 Chocolatey 吧！

只要你可以成功安裝執行 Chocolatey，那麼也可以在 Windows 享受自動化安裝 VirtualBox 的便利。

``` plain
choco install virtualbox --params "/ExtensionPack"
```

未來的更新也很方便。

``` plain
choco upgrade all
```

至於安裝的方法，留給不怕踩雷的 Windows 愛用者自己努力試試囉！

Chocolatey\
https://chocolatey.org/install
