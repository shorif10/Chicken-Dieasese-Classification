from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """Configuration for the project"""
    root_dir:Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path