====================================
Sequence tolerance benchmark
====================================

Sequence tolerance protocols predict the tolerated sequence space for a given protein-protein interface or protein domain.
The benchmark currently contains one such protocol capture. Analysis is provided by an R script which creates a series of
figures and a position weight matrix.

This protocol capture is based off the original captures from the Smith & Kortemme papers listed above however most of
the output directories have been excluded here to reduce the size of the repository.

The original output directories can be found in the `RosettaCommons repositories <https://github.com/RosettaCommons/demos/tree/master/protocol_capture/2010/backrub_seqtol>`_ or at http://kortemmelab.ucsf.edu/data/.

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

- *data* : contains some data from the Smith and Kortemme 2010 publication about the input structures and proteins.
- *input* : contains the input files for the benchmark. Input files specific to a particular protocol are in a subdirectory named after the protocol.
- *output* : these directories are empty by default. This is the default output location for protocols if they are run on the local machine.
- *output/sample* : contains sample output data that can be used to test the sequence_tolerance.R analysis script.
- *output/1N7T* : contains sample output data that can be used to partially (see below) test the figures.R script.
- *analysis* : contains the analysis scripts used to analyze the output of a prediction run. All protocols are expected to produce output that will work with the analysis scripts.
- *protocols* : contains the scripts needed to run a job. The scripts for a protocol are provided in a specific subdirectory.
- *hpc* : contains scripts that can be used to run the entire benchmark using specific cluster architectures. For practical reasons, a limited number of cluster systems are supported. Please feel free to provide scripts which run the benchmark for your particular cluster system.

--------------------------------------
Analysis
--------------------------------------

The analysis script generates four metrics which can be used to evaluate the results of the sequence tolerance simulations.
The analysis scripts are described in more detail in analysis/README.rst.

======================================
Protocol 1: Backrub/Sequence Tolerance
======================================

-------------------
General Information
-------------------

Created by: Colin A. Smith [1]_

Software suite: Rosetta

Protocol directory: backrub_seqtol

-------------------
Description
-------------------

This method first generates an ensemble of backbone structures by running backrub simulations on an input structure. For
each member of the ensemble, a large number of sequences are scored and then Boltzmann weighted to generate a position
weight matrix for the specified sequence positions. Interactions within and between different parts of the structure can
be individually reweighted, depending on the desired objective.

-------------------
Instructions
-------------------

To run this protocol, the backrub application is used to generate an ensemble of structures. Next, the sequence tolerance
application is used to sample a large number of sequence for each member of the ensemble. A python script is included which
handles generation of single ensemble member using backrub and sequence scoring using sequence_tolerance. It includes a
few paths which must be customized to run correctly on a user's system. Please note that 20 backbones is the minimum
suggested to get acceptable output. The more backbone structures that are generated, the less prone the results will be
to stochastic fluctuations.

------------------------
Protocol capture scripts
------------------------

The protocols/backrub_seqtol/backrub_seqtol.py script is provided to help with running the protocol. It has been modified
slightly from Colin Smith's original version to try to accommodate changes in the Rosetta command-line flags and default
score function since the original publications. The default settings use the latest default Rosetta score functions and
assume a recent version of Rosetta. The script can also be configured for use with older versions of Rosetta so that results
similar to the publications may be generated.

The purpose of the scripts are to allow the user to use the best general settings. For fine tuning, please see the sections
below describing the command line flags.


-------------------
Common Flags
-------------------

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


----------------------
Example command lines
----------------------

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


----------------------------
Supporting tool versions
----------------------------

This protocol capture has been tested with:

- Python 2.4.3 and R 2.12.1
- Python 2.7.8 and R 3.1.1

-------------------------------------------------
References to published works using this protocol
-------------------------------------------------

Smith, CA, Kortemme, T. Structure-Based Prediction of the Peptide Sequence Space Recognized by Natural and Synthetic PDZ Domains. 2010. J Mol Biol 402(2):460-74. `doi: 10.1016/j.jmb.2010.07.032 <http://dx.doi.org/10.1016/j.jmb.2010.07.032>`_.

Smith, CA, Kortemme, T. Predicting the Tolerated Sequences for Proteins and Protein Interfaces Using RosettaBackrub
Flexible Backbone Design. 2011.
PLoS ONE 6(7):e20451. `doi: 10.1371/journal.pone.0020451 <http://dx.doi.org/10.1371/journal.pone.0020451>`_.


.. [1] The original version of this protocol capture was developed and tested for Rosetta 3.2. Any errors in the current version above are likely to be our fault rather than that of the original author. Please contact support@kortemmelab.ucsf.edu with any issues which may arise.

.. [2] The default Rosetta score function switched to Talaris 2013, making some previous flags redundant.

