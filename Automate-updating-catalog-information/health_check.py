#!/usr/bin/env python3
import psutil
import shutil
import socket
import os
import sys
import emails


def check_disk_space(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 80


def check_memory_usage():
    """Verifies that there's enough available memory"""
    available_memory = psutil.virtual_memory().available
    available_memory_in_mb = available_memory / 1024 ** 2  # convert to MB
    return available_memory_in_mb > 500


def check_localhost():
    """Verifies that the hostname "localhost" can be resolved to '127.0.0.1'"""
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"


def generate_error_report(error):
    """Sends an email with the error warning"""
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = error
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)


def main(argv):
    if not check_disk_space('/'):
        subject = "Error - Available disk space is less than 20%"
        generate_error_report(subject)
    if not check_cpu_usage():
        subject = "Error - CPU usage is over 80%"
        generate_error_report(subject)
    if not check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        generate_error_report(subject)
    if not check_memory_usage():
        subject = "Error - Available memory is less than 500MB"
        generate_error_report(subject)


if __name__ == "__main__":
    main(sys.argv)
