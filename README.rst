====================================
Sequence tolerance benchmark
====================================

Sequence tolerance protocols predict the tolerated sequence space for a given protein-protein interface or protein domain. The benchmark currently contains one such protocol capture. Analysis is provided by an R script which creates a series of figures and a position weight matrix.

---------------------------
Directories in this archive
---------------------------

This archive contains the following directories:

- *input* : contains the input files for the benchmark. Input files specific to a particular protocol are in a subdirectory named after the protocol.
- *output* : these directories are empty by default. This is the default output location for protocols if they are run on the local machine.
- *output/sample* : contains sample output data that can be used to test the analysis scripts.
- *analysis* : contains the analysis scripts used to analyze the output of a prediction run. All protocols are expected to produce output that will work with the analysis scripts.
- *protocols* : contains the scripts needed to run a job. The scripts for a protocol are provided in a specific subdirectory.
- *hpc* : contains scripts that can be used to run the entire benchmark using specific cluster architectures. For practical reasons, a limited number of cluster systems are supported. Please feel free to provide scripts which run the benchmark for your particular cluster system.

--------------------------------------
Analysis
--------------------------------------

~~~~~~~~~~~~~~~~~~~~~~~~
Required tools
~~~~~~~~~~~~~~~~~~~~~~~~

The analysis scripts require the `R software suite <http://www.r-project.org>`_. The scripts have been tested using R
versions 2.12.1 and 3.1.1.

~~~~~~~~~~~~~
Main analysis
~~~~~~~~~~~~~

The main analysis is performed by an R script. Navigate to the directory with the output data from the run and then call this R script *i.e.*:

::

  cd output/sample
  R
  > source("../../analysis/sequence_tolerance.R")
  > process_specificity()

This should create boxplots for the mutated positions, a position weight matrix, and predicted ranking table for selected amino acid types for the positions.
For more details, see the Smith & Kortemme 2010 paper (references below).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generating figures as in the Smith & Kortemme PLoS One 2011 paper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The analysis/figures.R script can be used to recreate figures akin to those in the 2011 paper. The commands below will recreate
Figures 1 and 2 from that paper as we have included some sample output files. To recreate the other figures, you will need to download
the full set of output data (see Notes below).

::

  cd output
  R
  > source("../analysis/figures.R")

_______________
Troubleshooting
_______________

If you receive the error message "unknown family 'Arial'" then you may be missing the Arial fonts used by the script. These
commands may fix the issue if you have the Arial.ttf installed on your system.

::

  > install.packages("extrafont")
  > library("extrafont")
  > font_import()

The result of running:

::

  > fonts()

should now include the Arial font. Exit R and now run:

::

  R
  > library("extrafont")
  > source("../analysis/figures.R")


--------------------------------------
Protocol 1: Backrub/Sequence Tolerance
--------------------------------------

~~~~~~~~~~~~~~~~~~~
General Information
~~~~~~~~~~~~~~~~~~~

Created by: Colin A. Smith [1]_

Software suite: Rosetta

Protocol directory: backrub_seqtol

~~~~~~~~~~~~~~~~~
Description
~~~~~~~~~~~~~~~~~

This method first generates an ensemble of backbone structures by running backrub simulations on an input structure. For each member of the ensemble, a large number of sequences are scored and then Boltzmann weighted to generate a position weight matrix for the specified sequence positions. Interactions within and between different parts of the structure can be individually reweighted, depending on the desired objective.

~~~~~~~~~~~~
Instructions
~~~~~~~~~~~~

To run this protocol, the backrub application is used to generate an ensemble of structures. Next, the sequence tolerance application is used to sample a large number of sequence for each member of the ensemble. A python script is included which handles generation of single ensemble member using backrub and sequence scoring using sequence_tolerance. It includes a few paths which must be customized to run correctly on a user's system. Please note that 20 backbones is the minimum suggested to get acceptable output. The more backbone structures that are generated, the less prone the results will be to stochastic fluctuations.

~~~~~~~~~~~~
Common Flags
~~~~~~~~~~~~

_____________
General flags
_____________

+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
+============================+===========================================================================================================================================+
| -s 	                     | This flag specifies the starting structure.                                                                                               |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| -resfile                   | This is used in backrub and sequence_tolerance to specify mutations and control sequence sampling. It is required for sequence_tolerance. |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| -score:weights             | This flag is used to specify a weights file that disables environment dependent hydrogen bonds.                                           |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| -score:patch               | This flag must be used to reapply the score12 patch to the standard scoring function.                                                     |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| -ex1 -ex2 -extrachi_cutoff | These flags enable higher resolution rotamer librares for mutation and sequence redesign.                                                 |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+



_____________
Backrub flags
_____________



+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+===========================+===================================================================================================================================================================+
| -backrub:ntrials          | This flag is used to increase the number of Monte Carlo steps above the default of 1000.                                                                          |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -backrub:minimize_movemap | If mutations are specified in the resfile, this movemap is used to specify degrees of freedom to be minimized in a three stage process: CHI, CHI+BB, CHI+BB+JUMP. |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -in:file:movemap -sm_prob | Both of these flags are required to enable small phi/psi moves during backrub sampling.                                                                           |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+




________________________
Sequence_tolerance flags
________________________

+-----------------------------------------------+------------------------------------------------------------------------------+
+===============================================+==============================================================================+
| -ms:checkpoint:prefix -ms:checkpoint:interval | Both of these flags must be specified to get output of the scored sequences. |
+-----------------------------------------------+------------------------------------------------------------------------------+
| -ms:generations -ms:pop_size -ms:pop_from_ss  | These flags affect the genetic algorithm used for sequence sampling.         |
+-----------------------------------------------+------------------------------------------------------------------------------+
| -score:ref_offsets                            | This flag is used to reweight the reference energies for given residues.     |
+-----------------------------------------------+------------------------------------------------------------------------------+
| -seq_tol:fitness_master_weights               | This flag controls the fitness function used for the genetic algorithm.      |
+-----------------------------------------------+------------------------------------------------------------------------------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Example command lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

____________
Backrub step
____________

''''''''''''
Rosetta 3.2
''''''''''''

::

  rosetta-3.2/rosetta_source/bin/backrub.linuxgccrelease -database rosetta-3.2/rosetta_database
  -s input/pdbs/1N7T_01.pdb -ex1 -ex2 -extrachi_cutoff 0 -mute core.io.pdb.file_data
  -backrub:ntrials 10000 -score:weights input/backrub_seqtol/rosetta3.2/standard_NO_HB_ENV_DEP.wts
  -score:patch score12

''''''''''''''''''''''''''''''''
Rosetta, 2013-08-11 onwards [2]_
''''''''''''''''''''''''''''''''

::

  rosetta/source/bin/backrub.linuxgccrelease -database rosetta/database
  -s input/pdbs/1N7T_01.pdb -ex1 -ex2 -extrachi_cutoff 0 -mute core.io.pdb.file_data
  -backrub:ntrials 10000

_______________________
Sequence tolerance step
_______________________

''''''''''''
Rosetta 3.2
''''''''''''

::

  rosetta-3.2/rosetta_source/bin/sequence_tolerance.linuxgccrelease -database rosetta-3.2/rosetta_database
  -s input/pdbs/1N7T_01_0001_low.pdb.gz -ex1 -ex2 -extrachi_cutoff 0 -score:ref_offsets HIS 1.2
  -seq_tol:fitness_master_weights 1 1 1 2 -ms:generations 5 -ms:pop_size 2000 -ms:pop_from_ss 1
  -ms:checkpoint:prefix 1N7T_01_0001 -ms:checkpoint:interval 200 -ms:checkpoint:gz
  -score:weights input/backrub_seqtol/rosetta3.2/standard_NO_HB_ENV_DEP.wts -out:prefix 1N7T_01_0001
  -score:patch score12 -resfile input/backrub_seqtol/1N7T_seqtol.resfile

'''''''''''''''''''''''''''
Rosetta, 2013-08-11 onwards
'''''''''''''''''''''''''''

::

  rosetta/source/bin/sequence_tolerance.linuxgccrelease -database rosetta/database
  -s input/pdbs/1N7T_01_0001_low.pdb.gz -ex1 -ex2 -extrachi_cutoff 0 -ex1aro -ex2aro
  -seq_tol:fitness_master_weights 1 1 1 2 -ms:generations 5 -ms:pop_size 2000 -ms:pop_from_ss 1
  -ms:checkpoint:prefix 1N7T_01_0001 -ms:checkpoint:interval 200 -ms:checkpoint:gz
  -out:prefix 1N7T_01_0001 -resfile input/backrub_seqtol/1N7T_seqtol.resfile

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Using the seqtol_resfile.py python script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The seqtol_resfile.py takes as input a PDB file and generates a resfile for use with the sequence_tolerance app. It takes at least two other required arguments. The first is the command used for making residues designable. This is usually either "ALLAA" for all amino acids, or "PIKAA ..." for a restricted set of amino acids. The next arguments are the residues which should be designable, with the chain and residue number separated by a colon.

______________________________________
Example seqtol_resfile.py Command Line
______________________________________

::

  scripts/seqtol_resfile.py input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:2002 B:2003 B:2004 B:2005 B:2006

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Using the backrub_seqtol.py python script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The backrub_seqtol.py script takes as input a PDB file and other similarly named configuration files, and produces a single backrub ensemble member along with approximately 10,000 scored sequences on that member. All of the input files use a base name derived from removing the ".pdb" extension from the PDB file. For instance, the base name of 1MGF.pdb would be 1MFG.

If you want to use one PDB file with many different input files you can specify a different path from which to get the input files.

____________________
Required input files
____________________
+----------------------------+----------------------------------------------------------------------------------------------------------------------+
+============================+======================================================================================================================+
| <base name>_seqtol.resfile | This resfile specifies which sequence positions to sample, along with the residue positions that should be repacked. |
+----------------------------+----------------------------------------------------------------------------------------------------------------------+

____________________
Optional input files
____________________

+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+==============================+==========================================================================================================================================================================================================================================================+
| <base name>_backrub.resfile  | This resfile specifies which residues should have flexible side chains during the backrub run. By default, all side chains are flexible. This file can also define mutations that should be made to the input structure prior to the backrub simulation. |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <base name>_minimize.movemap | This file is passed to the -backrub:minimize_movemap flag (see above).                                                                                                                                                                                   |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <base name>_perturb.movemap  | This file is passed to the -in:file:movemap flag (see above). It also sets -sm_prob flag to 0.1.                                                                                                                                                         |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


____________________________
Example Overall Command Line
____________________________

::

  scripts/backrub_seqtol.py input_files/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb 1


~~~~~~~~~~~~~~~~~~~~~~~~
Supporting tool versions
~~~~~~~~~~~~~~~~~~~~~~~~

This protocol capture has been tested with:

- Python 2.4.3 and R 2.12.1
- Python 2.7.8 and R 3.1.1

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
References to published works using this protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Smith, CA, Kortemme, T. Structure-Based Prediction of the Peptide Sequence Space Recognized by Natural and Synthetic PDZ Domains. 2010. J Mol Biol 402(2):460-74. `doi: 10.1016/j.jmb.2010.07.032 <http://dx.doi.org/10.1016/j.jmb.2010.07.032>`_.

Smith, CA, Kortemme, T. Predicting the Tolerated Sequences for Proteins and Protein Interfaces Using RosettaBackrub Flexible Backbone Design. 2011.
PLoS ONE 6(7):e20451. `doi: 10.1371/journal.pone.0020451 <http://dx.doi.org/10.1371/journal.pone.0020451>`_.

~~~~~
Notes
~~~~~

This protocol capture is based off the original captures from the Smith & Kortemme papers listed above however most of the output directories have been excluded here to reduce the size of the repository.

The original output directories can be found in the `RosettaCommons repositories <https://github.com/RosettaCommons/demos/tree/master/protocol_capture/2010/backrub_seqtol>`_ or at http://kortemmelab.ucsf.edu/data/.


.. [1] The original version of this protocol capture was developed and tested for Rosetta 3.2. Any errors in the current version above are likely to be our fault rather than that of the original author. Please contact support@kortemmelab.ucsf.edu with any issues which may arise.

.. [2] The default Rosetta score function switched to Talaris 2013, making some previous flags redundant.

