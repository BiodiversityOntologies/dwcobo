# Creating Darwin Core OWL files for OBO Foundry ontologies

### Licensce
The intention is to make this repo CC0, however, I am waiting for clarification of the DwC license.

## Darwin Core background
The [Darwin Core Standard](https://www.tdwg.org/standards/dwc/) (DwC) includes a glossary of terms intended to facilitate the sharing of information about biological diversity by providing identifiers, labels, and definitions. Darwin Core is primarily based on taxa, their occurrence in nature as documented by observations, specimens, samples, and related information. The bulk of terms in DwC are properties, with a handful of classes that are used to group the properties. DwC does not specify any formal relations between its properties and classe DwC is available as RDF in two forms: 

1. With properties intended to be used with literals in the range, under the namespace https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms/
2. With properties intended to be used with IRIs in the range, under the namespace https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/iri/


## DwC for OBO ontologies
The purpose of this repo is to create OWL versions of the two DwC RDF files described above, following OBO Foundry best practices and common methods. This will make it easier for anyone who wants to import DwC properties into their OBO ontology. 

I will monitor DwC and update the ontologies here whenever there is a new releases of DwC.

### DwC in BCO

The primary use case for DwC with the BCO is as a set of metadata properties to describe specimens, collecting events, and related entities. To do this, we create an OWL file from DwC, interpreting the properties in https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms/terms.csv as owl:data properties. We use the class groupings as 'owl:domain' for these properties.

In the future, BCO may create another import file that uses DwC as object properties. 

## Steps for creating DwC OWL files

### Import DwC files

Download the latest versions of https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms/terms.csv and https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/iri/iri.csv and store in /src/ontology/imports

**TODO:** Add command to makefile to automatically check for new versions of source files and import them if needed.



### Modify the DwC terms file to work with Robot

See `/src/ontology/dwcrobot.py`

This code carries out the following steps:
- Loads ../imports/terms.csv or ../imports/iri.csv
- Concatenates 'DWC:' to each ID in column 2
- Changes the "rfd-type" column to the appropriate OWL type
- Inserts a term label row, as needed by ROBOT, as row 2 into the CSV file.
- Saves output to a CSV file.

By default, converts terms.csv to dwcterms.csv. To convert iri.csv to dwciri.csv, just specify the input and output files.

**TODO:** Change the 'tdwgutility_organizedInClass' column in `iri.csv` to the domains for each property. It currently just says `http://rs.tdwg.org/dwc/terms/attributes/UseWithIRI`

### Run Robot to create OWL file

For terms.csv:

`robot template --template dwcterms.csv --prefix "dwc: http://rs.tdwg.org/dwc/terms/" --ontology-iri "http://purl.obolibrary.org/obo/dwcobo-terms.owl" --output dwcobo-terms.owl`

For iri.csv:

`robot template --template dwciri.csv --prefix "dwc: http://rs.tdwg.org/dwc/iri/" --ontology-iri "http://purl.obolibrary.org/obo/dwcobo-iri.owl" --output dwcobo-iri.owl`

**TODO:** Add this to the makefile

## Ontology release process

**Still needs to be done**

A new release will be made whenever DwC is updated.

Release files will live in the root directory, with OBO Foundry PURLs of the form `http://purl.obolibrary.org/obo/dwcobo-terms.owl` and `http://purl.obolibrary.org/obo/dwcobo-iri.owl`, if approved.
