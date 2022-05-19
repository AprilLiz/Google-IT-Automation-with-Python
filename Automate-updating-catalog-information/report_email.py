#!/usr/bin/env python3
import os
from datetime import date
import emails
import reports
import sys


def generate_pdf_contents():
    """Prepare the data for a PDF report by parsing text files"""
    cwd = os.getcwd()
    path = cwd + '/supplier-data/descriptions/'
    files = os.listdir(path)
    pdf = ""
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(path, file), 'r') as f:
                line = f.readlines()
                name = line[0].strip()
                weight = line[1].strip()
                pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    return pdf


def main(argv):
    # Process the data and generate a full PDF report out of it."""
    attachment = "/tmp/processed.pdf"
    report_title = "Processed Update on " + date.today().strftime("%B %d, %Y")
    paragraph = generate_pdf_contents()
    reports.generate_report(attachment, report_title, paragraph)

    # Send the generated PDF report as an email attachment"""
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)


if __name__ == "__main__":
    main(sys.argv)
