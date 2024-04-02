from dataclasses import dataclass
from family import Family

@dataclass
class Office():
    """Base class for offices in the Company"""
    _office_holder: Family = Family()

    