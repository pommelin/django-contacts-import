from celery.task import task

from contacts_import.backends import importers


task.register(importers.VcardImporter)
task.register(importers.GoogleImporter)
task.register(importers.YahooImporter)