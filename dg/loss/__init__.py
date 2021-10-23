from __future__ import absolute_import

from .triplet import SoftTripletLoss
from .crossentropy import CrossEntropyLabelSmooth

__all__ = [
    'CrossEntropyLabelSmooth',
    'SoftTripletLoss',
]
