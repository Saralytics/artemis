from flask import abort, make_response, jsonify
import datetime
import inspect
from functools import wraps, update_wrapper
import hashlib
import os
import logging
import asyncio
from time import sleep
from collections import defaultdict

from enum import Enum


def get_logger(filepath):
    path = os.path.normpath(os.path.splitext(filepath)[0]).split(os.sep)
    return logging.getLogger(".".join(path[(len(path) - 1 - path[::-1].index("artemis")):]))  # fmt: skip


logger = get_logger(__file__)