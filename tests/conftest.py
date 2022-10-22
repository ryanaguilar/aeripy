"""Prepare py.test."""
import json
import os

import betamax
import pytest
from betamax.cassette.cassette import Cassette, dispatch_hooks
from betamax.serializers import JSONSerializer

