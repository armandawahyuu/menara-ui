#!/usr/bin/env python3
"""Regenerate all Menara UI pages (dev-time only; users never need this).

    python3 tools/build.py && python3 tools/check.py
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from pages import admin_pages, store_pages, docs_pages  # noqa: E402

admin_pages.build()
store_pages.build()
docs_pages.build()
print("built")
