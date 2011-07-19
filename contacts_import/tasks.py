from celery.task import task

from contacts_import.backends import importers


tasks.register(importers.VcardImporter)
tasks.register(importers.GoogleImporter)
tasks.register(importers.YahooImporter)