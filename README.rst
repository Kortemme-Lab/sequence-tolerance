====================================
Sequence tolerance benchmark
====================================

Sequence tolerance protocols predict the tolerated sequence space for a given protein-protein interface or protein domain.
This sequence tolerance benchmark measures the recapitulation of a reference distribution over a sequence space given the
conformation of a prototypical sequence.

This benchmark includes:

- phage display data that describe the peptide recognition preferences for: i) 169 naturally occurring and engineered PDZ domain-peptide complexes; ii) the human growth hormone-human growth hormone receptor (hGH-hGHR) interface; and iii) the 6 core and boundary residues in GB1.
- configuration details for the backrub ensemble protocol described in Smith & Kortemme (2010) and Smith & Kortemme (2011);
- analysis scripts that compare a predicted multiple sequence alignment to a reference multiple sequence alignment using four recapitulation metrics each based on the position weight matrix estimated for the ensemble.

This protocol capture is based off the original captures from the Smith & Kortemme papers listed above however most of
the output directories have been excluded here to reduce the size of the repository. The full output of a successful run
can be found in the `RosettaCommons repositories <https://github.com/RosettaCommons/demos/tree/master/protocol_capture/2010/backrub_seqtol>`_ and
at http://kortemmelab.ucsf.edu/data/.

---------
Licensing
---------

The contents of the repository *where possible* are licensed under the MIT License. The license only applies to files which either: i) include the license statement; or ii) which are explicitly listed in some file in the repository as being covered by the license. All other files may be covered under a separate license. The LICENSE file in the root of this repository is present only for the convenience of the user to indicate the license which covers any novel content presented herein.

-------------------------
Downloading the benchmark
-------------------------

The benchmark is hosted on GitHub. The most recent version can be checked out using the `git <http://git-scm.com/>`_ command-line tool:

::

  git clone https://github.com/Kortemme-Lab/sequence-tolerance.git

---------------------------
Directories in this archive
---------------------------

This archive contains the following directories:

- *data* : contains experimental phage display data compiled from the Smith and Kortemme 2010 publication. This is used to generate the benchmark analysis;
- *input* : contains the input files for the benchmark. Input files specific to a particular protocol are in a subdirectory named after the protocol. The input files are described in more detail in input/README.rst.
- *output* : these directories are empty by default. This is the default output location for protocols if they are run on the local machine.
- *output/sample* : contains sample output data that can be used to test the sequence_tolerance.R analysis script.
- *output/1N7T* : contains sample output data that can be used to partially (see below) test the figures.R script.
- *analysis* : contains the analysis scripts used to analyze the output of a prediction run. All protocols are expected to produce output that will work with the analysis scripts.
- *protocols* : contains the scripts needed to run a job. The scripts for a protocol are provided in a specific subdirectory.
- *hpc* : contains scripts that can be used to run the entire benchmark using specific cluster architectures. For practical reasons, a limited number of cluster systems are supported. Please feel free to provide scripts which run the benchmark for your particular cluster system.

=========
Protocols
=========

This repository contains one protocol which can be used to run the benchmark. We welcome the inclusion of more protocols.
Please contact support@kortemmelab.ucsf if you wish to contribute towards the repository.

Each protocol is accompanied by specific documentation in its protocol directory.

--------------------------------------
Protocol 1: Backrub/Sequence Tolerance
--------------------------------------

Created by: Colin A. Smith [1]_

Software suite: Rosetta

Protocol directory: protocols/backrub_seqtol

__________
References
__________

Smith, CA, Kortemme, T. Structure-Based Prediction of the Peptide Sequence Space Recognized by Natural and Synthetic PDZ Domains.
2010. J Mol Biol 402(2):460-74. `doi: 10.1016/j.jmb.2010.07.032 <http://dx.doi.org/10.1016/j.jmb.2010.07.032>`_.

Smith, CA, Kortemme, T. Predicting the Tolerated Sequences for Proteins and Protein Interfaces Using RosettaBackrub Flexible Backbone Design.
2011. PLoS ONE 6(7):e20451. `doi: 10.1371/journal.pone.0020451 <http://dx.doi.org/10.1371/journal.pone.0020451>`_.


.. [1] The original version of this protocol capture was developed and tested for Rosetta 3.2. Any errors in the current version above are likely to be our fault rather than that of the original author. Please contact support@kortemmelab.ucsf.edu with any issues which may arise.


========
Analysis
========

The same set of analysis scripts is used by all protocols. Conceptually, the analysis scripts should be a black box that
is separated from the output of each protocol by an interface. Currently, the scripts are tied particularly to the Rosetta
protocol included herein however we are happy to make the scripts more modular once another protocol is added to the
benchmark capture.

The analysis scripts generates four metrics which can be used to evaluate the results of the sequence tolerance simulations as
well as a series of plots. The scripts are described in more detail in analysis/README.rst.
