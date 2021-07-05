---
title: 開發自己的 Markdown 自動化工具
subtitle: Monosparta 軟體開發實戰訓練
papersize: A4
margin-left: 20mm
margin-right: 25mm
margin-top: 10mm
margin-bottom: 20mm
css: pandoc.css
---

這篇教學示範如何輕易地打造適合程式開發者使用的 Markdown 編輯環境，以及透過 Python 撰寫簡單的自動化工具，協助你將 Markdown 文件轉換為 HTML 與 PDF 格式。通常我們會在專案中使用 Markdown 撰寫 README 等開發文件，有時這份文件需要先經過轉檔，以方便列印或作為電子郵件的附件，交給專案的其他人員例如專案經理或客戶。

本篇需要用到的工具有：

1. Visual Studio Code (VSCode)
2. Python 3.x
3. Pandoc

VSCode 本身已經對 Markdown 文件編輯有良好的支援，但是你可以參考官方的這份說明，瞭解更多關於 Markdown 的實用技巧。

https://code.visualstudio.com/docs/languages/markdown

其中我們推薦：

* 加裝 markdownlint 套件，它可以 ~~強迫~~ 建議你撰寫出更好的風格。
* 瞭解 Preview 功能的操作，方便你在編寫 Markdown 代碼的同時，顯示網頁版本的輸出預覽。

![vscode + markdown](vscode-markdown.jpg)

Python 具有易學易用的特性，我們只需要找到合適的套件，就能輕鬆處理 Markdown 的轉換。

Python-Markdown
https://github.com/Python-Markdown/markdown

使用 `pip` 安裝 Python-Markdown 套件。

``` bash
pip install markdown
```

撰寫 `README.md`

完成最簡單的範例。

``` python
import markdown

with open('README.md', 'r') as f:
    html = markdown.markdown(f.read())

with open('README.html', 'w') as f:
    f.write(html)
```

<!--# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --print-to-pdf=README.pdf --disable-gpu README.html -->

Test
