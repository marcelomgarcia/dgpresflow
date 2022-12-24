from datetime import date
from pydantic import BaseModel, ValidationError, Field, validator
from pydantic import DirectoryPath
from pathlib import Path


class ScanAV(BaseModel):
    """Basic class to handle anti-virus scan."""

    root_dir: DirectoryPath
    av_update: str
    av_exe: str
    av_root_log: DirectoryPath
    quarantine: int
    quar_start: date = Field(default_factory=date.today)
    av_run: bool


class BagIt(BaseModel):
    """Set the folders that will be bagged, and the destination folder for the
    bag
    """

    input_line: str
    bag_dir: str
    input_dirs: list = []

    def __init__(self, **data):
        super().__init__(**data)
        self.input_dirs = [dir.strip() for dir in self.input_line.split(",")]

    @validator("bag_dir")
    def create_dir(cls, dir):
        if Path(dir).expanduser().exists():
            raise AssertionError(f"Bag dir '{dir}' already exists. Remove it first.")
        return dir


class AccessionFlow(BaseModel):
    """Basic class for digital preservation workflow"""

    accession_id: str
    av_scan: ScanAV
    bag_it: BagIt


def read_av_config(config) -> ScanAV:
    """Return an object 'ScanAV' that controls the AV scan and quarentine of
    the objects to ingest
    """

    scan_av = ScanAV(
        root_dir=config.get("av_dir"),
        av_update=config.get("av_update"),
        av_exe=config.get("av_clamav"),
        av_root_log=config.get("av_logs_root"),
        quarantine=config.getint("quarantine_days", 30),
        av_run=config.getboolean("run_it", True),
    )

    return scan_av


def read_bag_config(config) -> BagIt:
    """Read the folders to bag, and the destination of the bag"""

    bag_it = BagIt(input_line=config.get("source_dir"), bag_dir=config.get("dest_dir"))

    return bag_it


def mk_accession(config) -> AccessionFlow:
    """Create an accession object from the configuration file"""

    accession_id = config["ACCESSION"].get("accession_id")

    av_scan = read_av_config(config["CLAMAV"])

    bag_it = read_bag_config(config["BAGGER"])

    return AccessionFlow(accession_id=accession_id, av_scan=av_scan, bag_it=bag_it)
