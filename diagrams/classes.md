# Class Diagrams

Creating [class diagrams](https://mermaid.js.org/syntax/classDiagram.html)

- Accession
- Bagger
- ScanAV
- Metadata
  - Jove (and modules)
  - DROID


```mermaid
 classDiagram
      Animal <|-- Duck
      Animal <|-- Fish
      Animal <|-- Zebra
      Animal : +int age
      Animal : +String gender
      Animal: +isMammal()
      Animal: +mate()
      class Duck{
          +String beakColor
          +swim()
          +quack()
       }
      class Fish{
          -int sizeInFeet
          -canEat()
      }
      class Zebra{
          +bool is_wild
          +run()
      }  
    
```

## Accession

```mermaid
classDiagram
    Accession : +String acc_id;
    Accession : +Bagger bag;
    Accession : +queryAPI(userName);
    Accession : +createBag(bag);
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
