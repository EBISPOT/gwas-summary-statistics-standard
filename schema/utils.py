"""
Use for generating json schema from pydantic model
"""


import json
from metadata import SumStatsMetadata

with open("schema/metadata-json-schema.json", "w") as f:
    json.dump(SumStatsMetadata.schema(), f, indent=4)
