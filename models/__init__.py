#!/usr/bin/python3
"""initialize models & storage"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
