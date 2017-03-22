# idb
third project for CS373


Models:
========

## Artist:
- name
- date of birth
- date of death
- Nationality
- country of origin
- image
### Connections:
- connects to works
- connects to centuries
- connects to styles

## Work:
- medium
- date
- style
- size
- colorset (colors used in work)
- image
### Connections:
- connects to artist
- connects to centuries
- connects to styles


## Centuries:
- Artists
- Works
- Styles
- countries of note
- mediums of note
### Connections
- connects to works
- connects to artists
- connects to styles

## Styles:
- common colors (the api has a good set for this)
- average age of a piece in this style
- founding artists
- avg dimensions
- images of the style
### Connections:
- connects to works
- connects to artists
- connects to centuries


# Google Doc for our technical report (this link allows you to edit)
https://docs.google.com/document/d/1GdcxVpxK2OqV5jX1nx5vna8D56v27KsXv1sreU_bGB8/edit?usp=sharing
