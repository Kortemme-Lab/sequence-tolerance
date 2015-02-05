======================================
Protocol 1: Backrub/Sequence Tolerance
======================================

-------------------
General Information
-------------------

Created by: Colin A. Smith [1]_

Software suite: Rosetta

Protocol directory: backrub_seqtol

-----------
Description
-----------

This method uses flexible backbone modeling to predict the tolerated sequence space for a given protein-protein interface
or protein domain. There are two main computational steps.

First, an input structure is run through the Rosetta `backrub <https://www.rosettacommons.org/docs/latest/backrub.html>`_ application which uses a Monte Carlo sampling
and admits backbone flexibility. The result of this step is an ensemble of varied but similar backbone structures.

In the second step, the `sequence_tolerance <https://www.rosettacommons.org/docs/latest/sequence-tolerance.html>`_ application is
used to sample and score a large number of sequences for each member of the ensemble. Interactions within and between
different parts of the structure can be individually reweighted, depending on the desired objective. By default, the
application uses a set of weights which have been benchmarked against the data contained in this archive.

The output from both steps is then processed by the analysis scripts which use Boltzmann weighting to generate a position
weight matrix for the specified sequence positions.

The backrub and sequence tolerance steps are described in more detail in the `Example command lines`_ section.

----------------
Included scripts
----------------

There are two scripts included in this folder which can be used to help run the benchmark.

**backrub_seqtol.py**

This is the main script. It takes a PDB file and a Rosetta resfile (see `Resfiles`_ below), creates a new refined structure
using backrub, and then runs sequence tolerance to produce scored sequences. Note: this produces one ensemble member.
For consistent results, we recommend running this script 20-50 times as the more backbone structures that are generated,
the less prone the results will be to stochastic fluctuations.

backrub_seqtol.py needs to be configured to run correctly on a user's system. This is explained in `Configuration`_.

**seqtol_resfile.py**

This script is used to create resfiles for structures but is unnecessary for running the benchmark as the resfiles required
for running the benchmark have been included in input/backrub_seqtol. This script is included for convenience in case the
user wishes to test the protocol on structures not contained herein *e.g.* higher-resolution replacements for the benchmark
structures or on a different dataset.

@todo: in Running the benchmark below, we give examples of how to do so

-------------
Configuration
-------------

The file protocols/backrub_seqtol/settings.json should be created and configured according to the user's system. An
example configuration file in provided in protocols/backrub_seqtol/settings.json.example. Most users will only need to
configure the *rosetta_installation_path*, *rosetta_binary_extension* [2]_, and *output_dir* settings which provide the
location of the Rosetta installation, the suffix of the application binaries, and the output directory respectively.
The remaining settings are present in case the user wishes to run Rosetta using settings similar to those used in the
original publications.

The location of the Rosetta installation should be the directory which contains the checkout of the Rosetta repository
*i.e.* the directory containing:

- database
- README.md
- source
- tests

The file uses the
`JSON <http://www.json.org/>`_ format.

----------------------------
Paths and extensions
----------------------------

The command lines below use placeholders for paths and extensons. Please change these appropriately *e.g.*:

::

  WORKING_DIRECTORY=.
  BENCHMARK_PATH=<path/to/sequence-tolerance>
  ROSETTA_BASE=<path/to/rosetta>
  EXTENSION=linuxgccrelease
  # edit protocols/backrub_seqtol/settings.json to set some options

Note that the extension will change depending on what options were used to build Rosetta and on the architecture of the
machine used for the build.

------------
Dependencies
------------

The benchmark and analysis scripts use `Python <https://www.python.org/>`_ and the `R software suite <http://www.r-project.org>`_ respectively. These
scripts have been tested with:
- Python 2.4.3 and R 2.12.1
- Python 2.7.8 and R 3.1.1

An installation of Rosetta is required for this method. Rosetta can be downloaded `here <https://www.rosettacommons.org/>`_
and is freely available for academic use. Details of how to install Rosetta can be found in the `User Guide <https://www.rosettacommons.org/docs/latest/>`__.


=================
backrub_seqtol.py
=================

This is the main script used to run the protocol for the benchmark data. It has been modified slightly from Colin Smith's
original version to try to accommodate changes in the Rosetta command-line flags and default score function since the original
publications. The default settings use the latest default Rosetta score functions and assume a recent version of Rosetta.
The script can also be configured for use with older versions of Rosetta so that results similar to the publications may be
generated. The purpose of the script is to allow the user to use the best general settings. For fine tuning, please see the sections
below describing the command line flags.

This script takes as input a PDB file and other similarly named configuration files (`resfiles`_ and `movemaps`_) and generates a
single backrub ensemble member using backrub along with (by default) up to 10,000 scored sequences on that member using
the sequence_tolerance application. All of the input files use a base name derived from removing the ".pdb" extension from
the PDB file. For instance, the base name of 1MGF.pdb would be 1MFG so the associated resfile should be named 1MGF.resfile.
By default, the script looks for resfiles and movemaps in the same folder as the PDB file however the user may also specify
a separate path from which to find these files.

One run of the script will produce 1 ensemble member. Please note that 20-50 backbones (ensemble members) is the minimum
suggested to get acceptable output. The more backbone structures that are generated, the less prone the results will be to
stochastic fluctuations. We recommend that backrub_seqtol.py be called at least 20-50 times to generate enough structures
for proper analysis.

----------------------------
Command line options
----------------------------

The backrub_seqtol.py script takes the following options which can be specified either directly on the command line or via environment variables (but not both):

- pdb_path (PDB_PATH environment variable). Required option. This specifies the input PDB structure;
- iteration (SGE_TASK_ID environment variable). Optional, defaults to 1. The script should be run multiple times (*e.g.* 20) to create enough data for analysis. This option should be a unique integer specifying the run number (*e.g.* an integer between 1 and 20);
- input_path (INPUT_PATH environment variable). Optional, defaults to the directory containing pdb_path;
- "test_mode". Optional. This sets test parameters in the script to test whether the benchmark is configured correctly. See `Test mode`_ for more details.

----------------------------
Example command line
----------------------------

::

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol

This generates one ensemble member for 2I0L_A_C_V2006.pdb using backrub and then runs sequence tolerance on the generated
structure. Output is generated in the current working directory.

---------
Test mode
---------

To ensure that the script works, add the argument 'test_mode' in the command line. In test mode: i) the number
of Monte Carlo trials to run for the Backrub step is reduced from 10,000 to 100; and ii) the number of sequences per
generation is reduced from 2,000 to 40 for the sequence tolerance step. This speeds up the computation significantly
and helps to check whether the machinery works before a large job is started. Results produced in test mode should be ignored.

-----------
Input files
-----------

Besides the PDB structures, the benchmark also uses the following files during its run.

~~~~~~~~~~~~~~~~~~~~
Required input files
~~~~~~~~~~~~~~~~~~~~

These files are expected to be located in the same location as the input PDB file. The files from the original
protocol capture can be found in input/backrub_seqtol. The command liness used to create the resfiles are given in
input/README.rst.

+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+============================+===================================================================================================================================================================================+
| <base name>_seqtol.resfile | This resfile specifies which sequence positions to sample, along with the residue positions that should be repacked. This file can be created using the seqtol_resfile.py script. |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

~~~~~~~~~~~~~~~~~~~~
Optional input files
~~~~~~~~~~~~~~~~~~~~

These files are also expected to be located in the same location as the input PDB file. The files from the original
protocol capture can be found in input/backrub_seqtol.

+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+==============================+==========================================================================================================================================================================================================================================================+
| <base name>_backrub.resfile  | This resfile specifies which residues should have flexible side chains during the backrub run. By default, all side chains are flexible. This file can also define mutations that should be made to the input structure prior to the backrub simulation. |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <base name>_minimize.movemap | This file is passed to the -backrub:minimize_movemap flag (see above).                                                                                                                                                                                   |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <base name>_perturb.movemap  | This file is passed to the -in:file:movemap flag (see above). It also sets -sm_prob flag to 0.1.                                                                                                                                                         |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

=============================
How to run the full benchmark
=============================

These commands create data for the different benchmark cases. For test runs, add the argument "test_mode" to each line. For
brevity, we have only included the first and last command lines for each case (assuming an ensemble of 50 members).

The computation is highly parallelizable so we recommend that the benchmark be run either on a cluster or a machine with
a large number of cores. The commands below should work in general. Instructions for running the benchmark on a Sun Grid
Engine cluster are given in hpc/sge/backrub_seqtol/README.rst.

----------------------------
GB1 Fold Stability Tolerance
----------------------------

::

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2QMT/2QMT.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/2QMT
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2QMT/2QMT.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/2QMT

------------------------------
PDZ Domain Interface Tolerance
------------------------------

::

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/2I0L_A_C_V2006
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/2I0L_A_C_V2006

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2IWP_B_A_V1927/2IWP_B_A_V1927.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/2IWP_B_A_V1927
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2IWP_B_A_V1927/2IWP_B_A_V1927.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/2IWP_B_A_V1927

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2FNE_A_C_V2048/2FNE_A_C_V2048.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/2FNE_A_C_V2048
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2FNE_A_C_V2048/2FNE_A_C_V2048.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/2FNE_A_C_V2048

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_%02i.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/1N7T
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_%02i.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/1N7T

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_%02i.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/1N7T_V83K
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_%02i.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/1N7T_V83K

----------------------------
hGH/hGHR Interface Tolerance
----------------------------

::

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_1/1A22_1.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_1
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_1/1A22_1.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_1

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_2/1A22_2.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_2
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_2/1A22_2.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_2

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_3/1A22_3.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_3
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_3/1A22_3.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_3

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_4/1A22_4.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_4
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_4/1A22_4.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_4

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_5/1A22_5.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_5
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_5/1A22_5.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_5

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_6/1A22_6.pdb 1 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_6
  ...
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1A22_6/1A22_6.pdb 50 ${BENCHMARK_PATH}/input/backrub_seqtol/1A22_6


==============================
Analyzing the benchmark output
==============================

See analysis/README.rst for a full description of the analysis scripts. Briefly, navigate to the directory where the output
was produced and call the analysis e.g.

::

  cd output/sample
  R
  > source("../../analysis/sequence_tolerance.R")
  > process_seqtol()


=============================
Appendix A: seqtol_resfile.py
=============================

seqtol_resfile.py takes a PDB file as input and generates a resfile for use with the sequence_tolerance app. It takes
at least two other required arguments. The first is the command used for making residues designable. This is usually
either "ALLAA" for all amino acids, or "PIKAA ..." for a restricted set of amino acids. The next arguments are the residues
which should be designable, with the chain and residue number separated by a colon.

It is not necessary to use this script to run the benchmark as the required resfiles are provided herein. It is provided
to allow the user to easily use the sequence tolerance application on other structures.

----------------------------
Command line options
----------------------------

The seqtol_resfile.py script takes the following required options:

- pdb_path. This specifies the input PDB structure;
- design_command. As described above *e.g.* "ALLAA" or "PIKAA ADEFGHIKLMNPQRSTVWY" or "PIKAA AFILMPVW" *etc.*;
- a list of designed positions. As described above *e.g.* B:2002 B:2003 B:2004 B:2005 B:2006.

--------------------------------------
Example command line
--------------------------------------

::

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:2002 B:2003 B:2004 B:2005 B:2006


------------------------------
Resfile creation command lines
------------------------------

The resfiles contained in the input/backrub_seqtol directory were created using the following command lines.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GB1 Fold Stability Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/2QMT/2QMT.pdb "ALLAA" A:5 A:7 A:16 A:18 A:18 A:30 A:33


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PDZ Domain Interface Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:2002 B:2003 B:2004 B:2005 B:2006
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/2IWP_B_A_V1927/2IWP_B_A_V1927.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:1923 B:1924 B:1925 B:1926 B:1927
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/2FNE_A_C_V2048/2FNE_A_C_V2048.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:2044 B:2045 B:2046 B:2047 B:2048
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_01.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:303 B:304 B:305 B:306 B:307
  mv 1N7T_01_seqtol.resfile ${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_seqtol.resfile
  cp ${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_seqtol.resfile ${BENCHMARK_PATH}/input/pdbs/1N7T_V83K/1N7T_V83K_seqtol.resfile

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hGH/hGHR Interface Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/1A22_1/1A22_1.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:14 A:28 A:47 A:61 A:171 A:179
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/1A22_2/1A22_2.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:18 A:42 A:62 A:65 A:164 A:175
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/1A22_3/1A22_3.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:21 A:29 A:45 A:60 A:67 A:178
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/1A22_4/1A22_4.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:22 A:43 A:66 A:167 A:176 A:183
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/1A22_5/1A22_5.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:26 A:44 A:48 A:64 A:168 A:174
  ${BENCHMARK_PATH}/protocols/backrub_seqtol/seqtol_resfile.py ${BENCHMARK_PATH}/input/pdbs/1A22_6/1A22_6.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" A:25 A:41 A:46 A:63 A:172


=======================
Appendix B: Input files
=======================

--------
Resfiles
--------

Resfiles are input files for Rosetta which specify which determine side-chain conformational sampling and sequence identity.
Informally, a resfile is a list of commands, each of which identifies a set of residues and then describes actions on that set.
Examples of actions are:

- restriction of the set of residues allowed at the positions (controlling sequence identity);
- disallowing side-chain conformation sampling at the positions;
- allowing side-chain conformation sampling but preserving the original residue types/sequence identity;
- perform extra sampling at the positions.

The resfile file format is described in full in the Rosetta `User Guide <https://www.rosettacommons.org/docs/latest/resfiles.html>`__.
The resfiles required for running the benchmark using the backrub_seqtol method are included in this archive and are found
in the input/backrub_seqtol folder. The seqtol_resfile.py script can be used by the user to generate resfiles for new
structures.

--------
Movemaps
--------

Movemaps are input files for Rosetta which specify which torsion angles and rigid-body degrees of freedom are allowed to
be sampled. Similarly to a resfile, a movemap is a list of commands, each of which identifies a set of residues and then describes
allowed degrees of freedom for those residues. Examples of degrees of freedom are:

- allow backbone sampling;
- allow |chi|-angle sampling;
- disallowing side-chain conformation sampling at the positions;
- allowing side-chain conformation sampling but preserving the original residue types/sequence identity;
- perform extra sampling at the positions.

The movemap file format is described in full in the Rosetta `User Guide <https://www.rosettacommons.org/docs/latest/movemap-file.html>`__.
Most cases in the benchmark do not require movemaps but the movemap required for running the 1N7T V83K case is included in
this archive and can be found in the input/backrub_seqtol folder.

======================================
Appendix C: Rosetta command-line flags
======================================

This appendix describes some of the Rosetta command-line flags used in the scripts above. It is not required reading in
order to run the protocol but may be of interest to users who wish to benchmark with different command lines.

---------------------
General Rosetta flags
---------------------

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

---------------------
Backrub flags
---------------------



+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+===========================+===================================================================================================================================================================+
| -backrub:ntrials          | This flag is used to increase the number of Monte Carlo steps above the default of 1000.                                                                          |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -backrub:minimize_movemap | If mutations are specified in the resfile, this movemap is used to specify degrees of freedom to be minimized in a three stage process: CHI, CHI+BB, CHI+BB+JUMP. |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -in:file:movemap -sm_prob | Both of these flags are required to enable small phi/psi moves during backrub sampling.                                                                           |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+


------------------------
Sequence_tolerance flags
------------------------


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

~~~~~~~~~~~~
Backrub step
~~~~~~~~~~~~

This step in the protocol uses a Monte Carlo sampling algorithm to generate an ensemble of varied but similar backbone
structures for the given prototypical conformation.

Typical runtime: 3-5 minutes per structure.

Example input file:

::

  1N7T_01.pdb                                 A PDB file

Example generated files:

::

  ${WORKING_DIRECTORY}/1N7T_01_0001_low.pdb   The lowest energy structure found during the Monte Carlo simulation
  ${WORKING_DIRECTORY}/1N7T_01_0001_last.pdb  The last accepted structure during the Monte Carlo simulation (note: backrub_seqtol.py removes this file)
  ${WORKING_DIRECTORY}/1N7T_01_0001score.sc   The score components from the Rosetta scoring function

An explanation of the main Rosetta score components can be found `here <https://www.rosettacommons.org/docs/latest/score-types.html>`__.

''''''''''''
Rosetta 3.2
''''''''''''

::

  ${ROSETTA_BASE}/rosetta_source/bin/backrub.${EXTENSION} -database ${ROSETTA_BASE}/rosetta_database \
  -s ${BENCHMARK_PATH}/input/pdbs/1N7T_01.pdb -ex1 -ex2 -extrachi_cutoff 0 -mute core.io.pdb.file_data \
  -backrub:ntrials 10000 -score:weights ${BENCHMARK_PATH}/input/backrub_seqtol/rosetta3.2/standard_NO_HB_ENV_DEP.wts \
  -score:patch score12


''''''''''''''''''''''''''''''''
Rosetta, 2013-08-11 onwards [3]_
''''''''''''''''''''''''''''''''

::

  ${ROSETTA_BASE}/source/bin/backrub.${EXTENSION} -database ${ROSETTA_BASE}/database \
  -s ${BENCHMARK_PATH}/input/pdbs/1N7T_01.pdb -ex1 -ex2 -extrachi_cutoff 0 -mute core.io.pdb.file_data \
  -backrub:ntrials 10000

~~~~~~~~~~~~~~~~~~~~~~~
Sequence tolerance step
~~~~~~~~~~~~~~~~~~~~~~~

The sequence tolerance protocol is used for specificity prediction and library design. Given an input structure, the
application uses user-defined inter- and intra-molecular weights to determine the scores of a large number of sequences. In the
context of the backrub_seqtol protocol, this input structure is a structure created by the backrub step. The default values for
the weights have been shown to perform well for the structures considered in the references below.

The protocol uses a genetic algorithm which starts with an initial population of sequences and generates successive generations
where each generation has a better overall score from previous generations.

Typical runtime: 20 minutes per structure.

Example input files:

::

  ${WORKING_DIRECTORY}/1N7T_01_0001_low.pdb   The lowest energy structure from the backrub step
  1N7T_01.pdb                                 A resfile for 1N7T_01.pdb

Example generated files:

::

  ${WORKING_DIRECTORY}/1N7T_01_0001.ga.generations.gz    Contains all sequences from every generation
  ${WORKING_DIRECTORY}/1N7T_01_0001.ga.entities.gz       Contains all sequences from every generation and the fitness of each sequence

''''''''''''
Rosetta 3.2
''''''''''''

::

  ${ROSETTA_BASE}/rosetta_source/bin/sequence_tolerance.${EXTENSION} -database ${ROSETTA_BASE}/rosetta_database \
  -s ${WORKING_DIRECTORY}/pdbs/1N7T_01_0001_low.pdb -ex1 -ex2 -extrachi_cutoff 0 -score:ref_offsets HIS 1.2 \
  -seq_tol:fitness_master_weights 1 1 1 2 -ms:generations 5 -ms:pop_size 2000 -ms:pop_from_ss 1 \
  -ms:checkpoint:prefix 1N7T_01_0001 -ms:checkpoint:interval 200 -ms:checkpoint:gz \
  -score:weights ${BENCHMARK_PATH}/input/backrub_seqtol/rosetta3.2/standard_NO_HB_ENV_DEP.wts -out:prefix 1N7T_01_0001 \
  -score:patch score12 -resfile ${BENCHMARK_PATH}/input/backrub_seqtol/1N7T_seqtol.resfile

'''''''''''''''''''''''''''
Rosetta, 2013-08-11 onwards
'''''''''''''''''''''''''''

::

  ${ROSETTA_BASE}/source/bin/sequence_tolerance.${EXTENSION} -database ${ROSETTA_BASE}/database \
  -s ${WORKING_DIRECTORY}/pdbs/1N7T_01_0001_low.pdb -ex1 -ex2 -extrachi_cutoff 0 -ex1aro -ex2aro \
  -seq_tol:fitness_master_weights 1 1 1 2 -ms:generations 5 -ms:pop_size 2000 -ms:pop_from_ss 1 \
  -ms:checkpoint:prefix 1N7T_01_0001 -ms:checkpoint:interval 200 -ms:checkpoint:gz \
  -out:prefix 1N7T_01_0001 -resfile ${BENCHMARK_PATH}/input/backrub_seqtol/1N7T_seqtol.resfile



==========
References
==========

Smith, CA, Kortemme, T. Structure-Based Prediction of the Peptide Sequence Space Recognized by Natural and Synthetic PDZ Domains. 2010. J Mol Biol 402(2):460-74. `doi: 10.1016/j.jmb.2010.07.032 <http://dx.doi.org/10.1016/j.jmb.2010.07.032>`_.

Smith, CA, Kortemme, T. Predicting the Tolerated Sequences for Proteins and Protein Interfaces Using RosettaBackrub
Flexible Backbone Design. 2011.
PLoS ONE 6(7):e20451. `doi: 10.1371/journal.pone.0020451 <http://dx.doi.org/10.1371/journal.pone.0020451>`_.



.. [1] The original version of this protocol capture was developed and tested for Rosetta 3.2. Any errors in the current version above are likely to be our fault rather than that of the original author. Please contact support@kortemmelab.ucsf.edu with any issues which may arise.

.. [2] By default, a Linux release build of Rosetta built with GCC will append the suffix '.linuxgccrelease' to binaries *e.g.* backrub.linuxgccrelease is the binary for the backrub application.

.. [3] The default Rosetta score function switched to Talaris 2013, making some previous flags redundant.

.. |khgr| unicode:: U+003C7 .. GREEK SMALL LETTER CHI
.. |chi| replace:: |khgr|\
