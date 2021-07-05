# send tutorial to mailbox

安裝 wkhtmltopdf 與 pandoc（用於轉換 Markdown 至 PDF 格式）

```bash
brew install --cask wkhtmltopdf
brew install pandoc
brew install pngquant
brew install ImageMagick
```

安裝 Python 必要的套件

```bash
python3 -m venv .venv
source ./venv/bin/activate

pip install --upgrade pip

pip install bs4
pip install markdown
pip install Pygments
pip install pypandoc
pip install python-dotenv
pip install python-frontmatter
pip install htmlmin

# pip install -r requirements.txt
```

請先配置正確的 `.env` 設定

執行範例

```bash
# Test Only
./sendmail.py -i chapter/section/README.md -l subscribers.csv -t

# Real Run
./sendmail.py -i chapter/section/README.md -l subscribers.csv
```

References

* htmlemail.io/inline
