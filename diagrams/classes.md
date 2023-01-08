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
---
title: Accession Class
---

classDiagram
    class Accession
    Accession: +String acc_id
    Accession: +Bagger bag
    Accession: +queryAPI(userName)
    Accession: +createBag(bag)
```

## Bagger

```mermaid
---
title: Bagger
---

classDiagram
    class Bagger
    Bagger: +List[dir] source
    Bagger: +dir dest
    Bagger: -copyFiles(dir)
    Bagger: -createBag(dir)
```
