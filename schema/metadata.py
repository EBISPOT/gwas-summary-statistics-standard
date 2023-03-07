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


class EffectStatisticEnum(str, Enum):
    beta = 'beta'
    odds_ratio = 'odds_ratio'
    hazard_ratio = 'hazard_ratio'


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
    ancestryMethod: Optional[List[str]] = None
    caseControlStudy: Optional[bool] = None
    caseCount: Optional[int] = None
    controlCount: Optional[int] = None
    sampleSize: int = None
    sampleAncestry: List[str] = None


class SumStatsMetadata(BaseModel):
    genotypingTechnology: List[str] = None
    GWASID: Optional[constr(regex=r'^GCST\d+$')] = None
    traitDescription: List[str] = None
    effectAlleleFreqLowerLimit: Optional[float] = None
    dataFileName: str = None
    fileType: str = None
    dataFileMd5sum: str = None
    isHarmonised: Optional[bool] = False
    isSorted: Optional[bool] = False
    dateLastModified: date = None
    genomeAssembly: str = None
    analysisSoftware: Optional[str] = None
    imputationPanel: Optional[str] = None
    imputationSoftware: Optional[str] = None
    harmonisationReference: Optional[str] = None
    adjustedCovariates: Optional[List[str]] = None
    ontologyMapping: Optional[List[str]] = None
    authorNotes: Optional[str] = None
    GWASCatalogAPI: Optional[str] = None
    sex: Optional[SexEnum] = None
    coordinateSystem: CoordinateSystemEnum = None
    samples: List[SampleMetadata] = None
    
    class Config:
        title = 'GWAS Summary Statistics metadata schema'
