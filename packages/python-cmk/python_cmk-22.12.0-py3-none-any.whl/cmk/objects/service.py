"""Service-Status for Object-API."""
from __future__ import annotations

from . import base, dictionary

import logging


__log__ = logging.getLogger(__name__)


class Service(dictionary.Dictionary):
    domain_type = "service"

    class Service(base.ReadOnlyService):
        pass
