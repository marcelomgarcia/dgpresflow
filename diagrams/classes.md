# Class Diagrams

Creating [class diagrams](https://mermaid.js.org/syntax/classDiagram.html)

- Accession
- Bagger
- ScanAV
- Metadata
  - Jove (and modules)
  - DROID

## Accession

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

## Bagger

```mermaid
classDiagram
  class Bagger
  Bagger: +List[dir] src
  Bagger: +dir dest
  Bagger: -CopyFiles(src, dest)
  Bagger: -CreateBag(bag)
```

## ScanAV

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
