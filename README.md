# send tutorial to mailbox

安裝 wkhtmltopdf 與 pandoc（用於轉換 Markdown 至 PDF 格式）

```
brew install --cask wkhtmltopdf
brew install pandoc
brew install pngquant
```

安裝 Python 必要的套件

```
python3 -m venv venv
source ./venv/bin/activate

pip install bs4
pip install markdown
pip install Pygments
pip install pypandoc
pip install python-dotenv
pip install python-frontmatter
```

請先配置正確的 `.env` 設定

執行範例

```
# Test Only
./sendmail.py -i hello-world/02-requirements/README.md -l subscribers.csv -t

# Real Run
./sendmail.py -i hello-world/02-requirements/README.md -l subscribers.csv
```