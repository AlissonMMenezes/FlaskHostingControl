from flask import Flask
from db import db

class ActivePackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    web_template = db.Column(db.String,nullable=False)
    proxy_template = db.Column(db.String,nullable=False)
    dns_template = db.Column(db.String,nullable=False)
    bash = db.Column(db.String,nullable=False)
    web_domains = db.Column(db.Integer,nullable=False)
    web_aliases = db.Column(db.Integer,nullable=False)
    dns_domains = db.Column(db.Integer,nullable=False)
    dns_records = db.Column(db.Integer,nullable=False)
    mail_domains = db.Column(db.Integer,nullable=False)
    mail_accounts = db.Column(db.Integer,nullable=False)
    cron_jobs = db.Column(db.Integer,nullable=False)
    databases = db.Column(db.Integer,nullable=False)
    backups = db.Column(db.Integer,nullable=False)
    bandwidth = db.Column(db.Integer,nullable=False)
    nameservers = db.Column(db.String,nullable=False)
    package_id = db.Column(db.Integer,db.ForeignKey('package.id'),nullable=True)
    package = db.relationship("Package")
    user = db.relationship("User")

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False)    
    dns_template = db.Column(db.String,nullable=False)
    bash = db.Column(db.String,nullable=False)
    web_domains = db.Column(db.Integer,nullable=False)
    web_aliases = db.Column(db.Integer,nullable=False)
    dns_domains = db.Column(db.Integer,nullable=False)
    dns_records = db.Column(db.Integer,nullable=False)
    mail_domains = db.Column(db.Integer,nullable=False)
    mail_accounts = db.Column(db.Integer,nullable=False)
    cron_jobs = db.Column(db.Integer,nullable=False)
    databases = db.Column(db.Integer,nullable=False)
    backups = db.Column(db.Integer,nullable=False)
    quota = db.Column(db.Integer,nullable=False)
    bandwidth = db.Column(db.Integer,nullable=False)

    
if __name__ == "__main__":
    manager.run()
