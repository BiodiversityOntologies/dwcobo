# Creating Darwin Core Imports

## Darwin Core background
The [Darwin Core Standard](https://www.tdwg.org/standards/dwc/) (DwC) includes a glossary of terms intended to facilitate the sharing of information about biological diversity by providing identifiers, labels, and definitions. Darwin Core is primarily based on taxa, their occurrence in nature as documented by observations, specimens, samples, and related information. The bulk of terms in DwC are properties, with a handful of classes that are used to group the properties. DwC does not specify any formal relations between its properties and classe DwC is available as RDF in two forms: 

1. With properties intended to be used with literals in the range, under the namespace https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms/
2. With properties intended to be used with IRIs in the range, under the namespace https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/iri/


## DwC in BCO

The primary use case for DwC with the BCO is as a set of metadata properties to describe specimens, collecting events, and related entities. To do this, we create an OWL file from DwC, interpreting the properties in https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms/terms.csv as owl:data properties. We use the class groupings as 'owl:domain' for these properties.

In the future, we may create another import file that uses DwC as object properties, using https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/iri/iri.csv. 


## Steps for creating import ontology

**ToDo:** Write a script and makefile to automate this process. 

1. Download the latest version of https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms/terms.csv and store in /src/ontology/imports
2. Edit the "term_localName" column (i.e. ID) to prepend IDs with "DWC:". Save as "dwcterms.csv".
3. Insert a second row from the file `terms_label_row.csv`. This translates the header row (row 1) into the format needed for ROBOT. NOTE: This step depends on the format of the input file not changing, and it will need to be checked whenever the process is run.
4. Run ROBOT with the following command:

``robot template --template dwcterms.csv \
  --prefix "dwc: http://rs.tdwg.org/dwc/terms/" \
  --ontology-iri "http://purl.obolibrary.org/obo/bco/dwcterms.owl" \
  --output ../dwcterms.owl
  ``
