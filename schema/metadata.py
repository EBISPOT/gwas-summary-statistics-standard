"""
A pydantic (https://docs.pydantic.dev/) schema that can be 
used by python projects for defining the metadata model.
"""

from pydantic import (BaseModel,
                      constr)
from datetime import date
from typing import List, Optional
from enum import Enum

"""
Enums
"""



class SexEnum(str, Enum):
    male = 'M'
    female = 'F'
    combined = 'combined'


class CoordinateSystemEnum(str, Enum):
    zero = '0-based'
    one = '1-based'


"""
Models
"""


class SampleMetadata(BaseModel):
    ancestry_method: Optional[List[str]] = None
    case_control_study: Optional[bool] = None
    case_count: Optional[int] = None
    control_count: Optional[int] = None
    sample_size: int = None
    sample_ancestry: List[str] = None


class SumStatsMetadata(BaseModel):
    genotyping_technology: List[str] = None
    gwas_id: Optional[constr(regex=r'^GCST\d+$')] = None
    trait_description: List[str] = None
    minor_allele_freq_lower_limit: Optional[float] = None
    data_file_name: str = None
    file_type: str = None
    data_file_md5sum: str = None
    is_harmonised: Optional[bool] = False
    is_sorted: Optional[bool] = False
    date_last_modified: date = None
    genome_assembly: str = None
    analysis_software: Optional[str] = None
    imputation_panel: Optional[str] = None
    imputation_software: Optional[str] = None
    harmonisation_reference: Optional[str] = None
    adjusted_covariates: Optional[List[str]] = None
    ontology_mapping: Optional[List[str]] = None
    author_notes: Optional[str] = None
    gwas_catalog_api: Optional[str] = None
    sex: Optional[SexEnum] = None
    coordinate_system: CoordinateSystemEnum = None
    samples: List[SampleMetadata] = None
    
    class Config:
        title = 'GWAS Summary Statistics metadata schema'
