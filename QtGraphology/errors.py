#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import TYPE_CHECKING

class NodeMenuError(Exception): pass


class NodePropertyError(Exception): pass


class NodeWidgetError(Exception): pass


class NodeCreationError(Exception): pass


class NodeDeletionError(Exception): pass


class NodeRegistrationError(Exception): pass


class PortError(Exception): pass


class PortRegistrationError(Exception): pass
