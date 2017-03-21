# idb
third project for CS373


Models:
========
Artist:
name
date of birth
date of death
Nationality
country of origin
image

connects to works
connects to centuries
connects to styles

Work:
medium
date
style
size
colorset (colors used in work)
image

connects to artist
connects to centuries
connects to styles


Centuries:
Artists
Works
Styles
countries of note
mediums of note


connects to works
connects to artists
connects to styles

Styles:
common colors (the api has a good set for this)
average age of a piece in this style
founding artists
avg dimensions
images of the style

connects to works
connects to artists
connects to centuries
