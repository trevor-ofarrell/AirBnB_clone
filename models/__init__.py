#!/usr/bin/python3
"""initialize models & storage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
