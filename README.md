## GWAS-SSF: A GWAS Summary Statistics Format

This repository is for maintaining the GWAS-SSF (GWAS summary statistics format) specification. 

Click [here](gwas-ssf_v0.1.pdf) for the current specification. 
Examples are [here](examples).

Comments, suggestions and issues are welcome via the issue tracker.


### Summary

* GWAS summary statistics format (GWAS-SSF) is composed of two files:
  1. summary statistics data file (TSV) e.g. [0000123.tsv](examples/0000123.tsv)
  2. accompanying metadata file (YAML) e.g. [0000123.yaml](examples/0000123.yaml)

#### Summary statistics data file
* The summary statistics data file is a TSV flat file of tab-delimited values that can be compressed (see [schamatic](images/schematic.png)), reporting data from a single genome-wide analysis. 
* The first line of the summary statistics data file contains the headers to the table. 
* The rows after the header store the variant association data. 
* Where permitted, values can be omitted by the presence of 'NA'. 
* There are no limits to the number of rows or columns that the table can have, however, a set of mandatory fields (defined in [spec](gwas-ssf_v0.1.pdf), see Table 1) must be present in a defined order. 
* A file may contain additional columns beyond the set of mandatory fields. 

#### Metadata file
* The metadata data file describes the summary statistics data file such as the filename and md5sum (see [example](examples/0000123.yaml) for example)
* The metadata data file describes the GWAS data such as sample, trait, genome assembly etc (see [spec](gwas-ssf_v0.1.pdf))

### Create the pdf spec
Convert the .tex to pdf:
`pdflatex gwas-ssf_<version>.tex` generates the pdf, gwas-ssf_<version>.pdf.