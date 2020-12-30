# Creating Darwin Core Imports for ontologies

## Darwin Core background
The [Darwin Core Standard](https://www.tdwg.org/standards/dwc/) (DwC) includes a glossary of terms intended to facilitate the sharing of information about biological diversity by providing identifiers, labels, and definitions. Darwin Core is primarily based on taxa, their occurrence in nature as documented by observations, specimens, samples, and related information. The bulk of terms in DwC are properties, with a handful of classes that are used to group the properties. DwC does not specify any formal relations between its properties and classe DwC is available as RDF in two forms: 

1. With properties intended to be used with literals in the range, under the namespace https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms/
2. With properties intended to be used with IRIs in the range, under the namespace https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/iri/


## DwC for OBO ontologies
The purpose of this repo is to create OWL versions of the two DwC RDF files described above, following OBO Foundry best practices and common methods. This will make it easier for anyone who wants to import DwC properties into their OBO ontology. 

I will monitor DwC and update the ontologies here whenever there is a new releases of DwC.

## DwC in BCO

The primary use case for DwC with the BCO is as a set of metadata properties to describe specimens, collecting events, and related entities. To do this, we create an OWL file from DwC, interpreting the properties in https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms/terms.csv as owl:data properties. We use the class groupings as 'owl:domain' for these properties.

In the future, we may create another import file that uses DwC as object properties, using https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/iri/iri.csv. 

## Steps for creating import ontology

### Import DwC files

Download the latest version of https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms/terms.csv and store in /src/ontology/imports


### Modify the DwC terms file to work with Robot

See `/src/dwcterms.py`

This code carries out the following steps:
- Load imports/terms.csv
- Insert a term label row, as needed by ROBOT, as row 2 into the CSV file.
- Concatenate 'DWC:' to each ID in column 2 ("term_localName")
- Save output to a CSV file called `dwcterms.csv`.

So far only it has only been tested to work with terms.csv. Will test for iri.csv later.

### Run Robot to create OWL file

``robot template --template dwcterms.csv \
  --prefix "dwc: http://rs.tdwg.org/dwc/terms/" \
  --ontology-iri "http://purl.obolibrary.org/obo/bco/imports/dwcterms.owl" \
  --output ../dwcterms.owl
  ``

## ToDo:

- Write a makefile to automate this process. 
- Update `/src/dwcterms.py` to work with either `terms.csv` or `iri.csv` or create `/src/dwciri.py` for `iri.csv`.
- Write code that checks that the format of the input file has not changed, because `/src/terms_label_row.csv` is written specifically for the current (10/2020) version of `terms.csv`.
- request an OBO purl for the DwC files.
- write an script to automatically monitor DwC releases, if possible.
- import `dwcterms.owl` into the BCO repo.
