from dotenv import load_dotenv, dotenv_values
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import markdown
from string import Template
from pathlib import Path
import frontmatter
from frontmatter.default_handlers import YAMLHandler

def attach_image(filename, content_id):
    with open(filename, "rb") as file:
        msgImage = MIMEImage(file.read())
    msgImage.add_header('Content-ID', content_id)
    return msgImage

config = dotenv_values(".env")

with open("hello-world/02-requirements/README.md", "r", encoding="utf-8") as input_file:
    metadata, text = frontmatter.parse(input_file.read(), handler=YAMLHandler())

subject = metadata['title']

html_text = markdown.markdown(text, extensions=['codehilite'])

print(html_text)

template = Template(Path("template.html").read_text())
body = template.substitute({ "subject": subject, "content": html_text })

content = MIMEMultipart()
content["subject"] = subject
content["from"] = config['SMTP_FROM']
content["to"] = config['SMTP_TO']
content.attach(MIMEText(body, 'html'))

filename = "02-requirements.pdf"  # In same directory as script

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
content.attach(part)

content.attach(attach_image('monosparta-favicon.png', '<monosparta-favicon>'))
content.attach(attach_image('monosparta-logo.png', '<monosparta-logo>'))

with smtplib.SMTP(host=config['SMTP_HOST'], port=config['SMTP_PORT']) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(config['SMTP_USER'], config['SMTP_PASS'])
        smtp.send_message(content)
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)