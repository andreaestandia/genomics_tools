# A few useful tools if you work in genomics
This repo contains useful functions to process genomic data. Feel free to contact me if you have any questions (andrea.estandia@biology.ox.ac.uk)

## Installation

1. Clone the repository 

   ```
   git clone https://github.com/andreaestandia/genomics_tools.git
   ```

2. Navigate to main project folder, then run:

   ```
     conda env create --file requirements.yml && conda activate tools_genomics-env
   ```

## Functions

* Subset BEAGLE files produced by ANGSD

  ```bash
  python subset_beagle.py --beagle beagle_file --samples list_samples --out output_file
  ```

* Convert BEAGLE format to VCF format

  ```bash
  python beagle_to_vcf.py --input_file beagle_file --output_file output_file 
  ```

* Extract annotation from GFF file

  ```bash
    python extract_annotation_gff.py --gff3_file gff_file --start_position start_pos --end_position end_pos --chromosome chr
  ```

* Extract FASTA sequence from reference genome

  ```bash
  python extract_fasta_sequence.py --fasta_file fasta --sequence_id chr_or_scaffold --start_position start_pos --end_position end_pos
  ```

* Select a certain number of SNPs from IMMANC file (Bayesass input) 

  ```bash
  python select_snps_ba.py --input_file input.ba3 --num_markers n_markers --output_file output.ba3
  ```

* Update population labels in IMMANC file

  ```bash
  python update_labels_BA.py list_samples.txt input.ba3 output.ba3
  ```

* Filter samples from IMMANC file 

  ```bash
  python filter_ba.py --full_file BA_file --sample_names list_names --output_file out
  ```

  



