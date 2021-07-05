#!/usr/bin/env python
import os
import sys
import getopt
import csv
from dotenv import load_dotenv, dotenv_values
from email import encoders
from email.utils import formataddr
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
import pypandoc

def attach_image(filename, content_id):
    with open(filename, "rb") as file:
        mimeobj = MIMEImage(file.read())
    mimeobj.add_header('Content-ID', content_id)
    return mimeobj

def attach_file(filename):
    with open(filename, "rb") as attachment:
        mimeobj = MIMEBase("application", "octet-stream")
        mimeobj.set_payload(attachment.read())
    encoders.encode_base64(mimeobj)
    mimeobj.add_header(
        "Content-Disposition",
        f"attachment; filename={filename}",
    )
    return mimeobj

def convert_pdf(filename, output_filename):
    output = pypandoc.convert_file(
        filename,
        to='html5',
        outputfile=output_filename,
        extra_args=['-s', '--verbose'])

def markdown_load(filename, template_filename):
    with open(filename, 'r', encoding='utf-8') as input_file:
        metadata, text = frontmatter.parse(input_file.read(), handler=YAMLHandler())
        subject = metadata['title']
        html_text = markdown.markdown(text, extensions=['codehilite'])
        template = Template(Path(template_filename).read_text())
        html_content = template.substitute({ 'subject': subject, 'content': html_text })
        return subject, html_content

def main(argv):

    inputfile = ''
    listfile = ''
    is_test_only = False

    try:
        opts, args = getopt.getopt(argv, 'hti:l:', ['input=', 'list=', 'test-only'])
    except getopt.GetoptError:
        print('./sendmail.py -i <inputfile> -l <listfile>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('./sendmail.py -i <inputfile> -l <listfile>')
            sys.exit()
        elif opt in ('-i', '--input'):
            inputfile = arg
        elif opt in ('-l', '--list'):
            listfile = arg
        elif opt in ('-t', '--test-only'):
            is_test_only = True


    if not os.path.isfile(inputfile):
        print('Error: {} file not exists.'.format(inputfile))
        print('./sendmail.py -i <inputfile> -l <listfile>')
        sys.exit()

    if not os.path.isfile(listfile):
        print('Error: {} file not exists.'.format(listfile))
        print('./sendmail.py -i <inputfile> -l <listfile>')
        sys.exit()

    config = dotenv_values(".env")

    pre, ext = os.path.splitext(os.path.basename(inputfile))
    pdf_filename = pre + '.pdf'

    print('Generating PDF file {}'.format(pdf_filename))
    convert_pdf(inputfile, pdf_filename)

    subject, html_content = markdown_load(inputfile, 'template.html')

    content = MIMEMultipart()
    content['subject'] = subject
    content['from'] = config['SMTP_FROM']
    content['to'] = ''

    content.attach(MIMEText(html_content, 'html'))
    content.attach(attach_file(pdf_filename))
    content.attach(attach_image('monosparta-favicon.png', '<monosparta-favicon>'))
    content.attach(attach_image('monosparta-logo.png', '<monosparta-logo>'))

    with open(listfile, newline='') as csvfile:
        for row in csv.reader(csvfile):
            subscriber = formataddr((row[0].strip(), row[1].strip()))
            print('Sent to {}'.format(subscriber))
            content.replace_header('to', subscriber)

            with smtplib.SMTP(host=config['SMTP_HOST'], port=config['SMTP_PORT']) as smtp:
                try:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login(config['SMTP_USER'], config['SMTP_PASS'])
                    if not is_test_only:
                        smtp.send_message(content)
                        print('Completed.')
                    else:
                        print('Tested.')
                except Exception as e:
                    print('Error message: ', e)

if __name__ == "__main__":
   main(sys.argv[1:])