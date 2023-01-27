# Diagrams

Diagrams to help understand the project

## Class Diagrams

Creating [class diagrams](https://mermaid.js.org/syntax/classDiagram.html)

- Accession
- Bagger
- ScanAV
- Metadata
  - Jove (and modules)
  - DROID

### Accession

```mermaid
classDiagram
    class Accession
    Accession : +String acc_id
    Accession : +Bagger bag
    Accession : -dict bagArchivera
    Accession : -dict archiveraDC
    Accession : +ReadConfig(path)
    Accession : +QueryAPI(userName)
    Accession : +CreateBag(bag)
    Accession : +ScanAV(files)


```

### Bagger

```mermaid
classDiagram
  class Bagger
  Bagger: +List[dir] src
  Bagger: +dir dest
  Bagger: -CopyFiles(src, dest)
  Bagger: -CreateBag(bag)
```

### ScanAV

```mermaid
classDiagram
  class ScanAV
  ScanAV: -str pathLogs
  ScanAV: -str pathRootDir
  ScanAV: -str pathExe
  ScanAV: -str pathUpdate
  ScanAV: -str pathFiles
  ScanAV: -int quarantine
  ScanAV: -date ScanDate
  ScanAV: -UpdateDBAV()
  ScanAV: -ScanAV(pathFiles)
  ScanAV: -InQuarantine()
```

### Format Identifiers

There are two format identifiers in use: [JHOVE](http://jhove.openpreservation.org/) and [DROID](https://www.nationalarchives.gov.uk/information-management/manage-information/preserving-digital-records/droid/). We start with a base class for the format identifiers, then we expand the base class for each identifier.

```mermaid
classDiagram
  class formatIdentifier
  formatIdentifier: +str pathRootDir
  formatIdentifier: +str fileExe
  formatIdentifier: +str outputFormat
  formatIdentifier: +bool hasModules
```

---

## Entity Relationship

The big picture

```mermaid
erDiagram
    Accession ||--|| ScanAV : scan
    Accession ||--|| Bag: has
```
