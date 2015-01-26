===========================================
backrub_seqtol (Backrub/Sequence Tolerance)
===========================================

backrub_seqtol uses two Rosetta applications - `backrub <https://www.rosettacommons.org/docs/latest/backrub.html>`_ and
`sequence_tolerance <https://www.rosettacommons.org/docs/latest/sequence-tolerance.html>`_.

~~~~~~~~~~~~
Dependencies
~~~~~~~~~~~~

These scripts have been tested with Python 2.4.3 and Python 2.7.8.


~~~~~~~~~~~~~
settings.json
~~~~~~~~~~~~~

This file contains configuration options for the script. It includes a few paths which must be customized to run
correctly on a user's system, particularly the location of the Rosetta installation. To configure the script for your
Rosetta installation, create the file settings.json in this directory (an example file is provided).

The file uses the
`JSON <http://www.json.org/>`_ format.

~~~~~~~~~~~~~~~~~
backrub_seqtol.py
~~~~~~~~~~~~~~~~~

This script takes as input a PDB file and other similarly named configuration files and generates a single backrub ensemble
member using backrub along with (by default) up to 10,000 scored sequences on that member using the sequence_tolerance
application. All of the input files use a base name derived from removing the ".pdb" extension from the PDB file. For
instance, the base name of 1MGF.pdb would be 1MFG. If you want to use one PDB file with many different input files you can
specify a different path from which to get the input files.

Please note that 20 backbones (twenty ensemble members) is the minimum suggested to get acceptable output. The more
backbone structures that are generated, the less prone the results will be to stochastic fluctuations *i.e.*
backrub_seqtol.py should be called at least 20 times to generate enough structures for proper analysis.

----------------------------------------
Running the protocol script in test mode
----------------------------------------

To test to make sure that the script works, add the argument 'test_mode' in the command line. In test mode: i) the number
of Monte Carlo trials to run for the Backrub step is reduced from 10,000 to 100; and ii) the number of sequences per
generation is reduced from 2,000 to 40 for the sequence tolerance step. This speeds up the computation significantly and
can be used to test whether the script works before a large job is started however the results it produces should be ignored.

--------------------------------
Additional, required input files
--------------------------------

Note: these files are expected to be located in the same location as the input PDB file. The files from the original
protocol capture can be found in input/backrub_seqtol.

+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+============================+===================================================================================================================================================================================+
| <base name>_seqtol.resfile | This resfile specifies which sequence positions to sample, along with the residue positions that should be repacked. This file can be created using the seqtol_resfile.py script. |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

--------------------------------
Additional, optional input files
--------------------------------

Note: these files are expected to be located in the same location as the input PDB file. The files from the original
protocol capture can be found in input/backrub_seqtol.

+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+==============================+==========================================================================================================================================================================================================================================================+
| <base name>_backrub.resfile  | This resfile specifies which residues should have flexible side chains during the backrub run. By default, all side chains are flexible. This file can also define mutations that should be made to the input structure prior to the backrub simulation. |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <base name>_minimize.movemap | This file is passed to the -backrub:minimize_movemap flag (see above).                                                                                                                                                                                   |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <base name>_perturb.movemap  | This file is passed to the -in:file:movemap flag (see above). It also sets -sm_prob flag to 0.1.                                                                                                                                                         |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------
Paths and extensions
----------------------------

The command lines below use placeholders for paths and extensons. Please change these appropriately *e.g.*:

::

  WORKING_DIRECTORY=.
  BENCHMARK_PATH=<path/to/sequence-tolerance>
  # edit protocols/backrub_seqtol/settings.json to set some options

Note that the extension will change depending on what options were used to build Rosetta and on the architecture of the
machine used for the build.

----------------------------
Command line options
----------------------------

The backrub_seqtol.py script takes the following options which can be specified either directly on the command line or via environment variables (but not currently both):
 - pdb_path (PDB_PATH environment variable). Required option. This specifies the input PDB structure;
 - iteration (SGE_TASK_ID environment variable). Optional, defaults to 1. The script should be run multiple times (*e.g.* 20) to create enough data for analysis. This option should be a unique integer specificying the run number (*e.g.* an integer between 1 and 20);
 - input_path (INPUT_PATH environment variable). Optional, defaults to the directory containing pdb_path;
 - "test_mode". Optional. This sets test parameters in the script to test whether the benchmark is configured correctly. See above for more details.

----------------------------
Example Overall Command Line
----------------------------


::

  scripts/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb 1 test_mode


~~~~~~~~~~~~~~~~~
seqtol_resfile.py
~~~~~~~~~~~~~~~~~

The seqtol_resfile.py takes as input a PDB file and generates a resfile for use with the sequence_tolerance app. It takes
at least two other required arguments. The first is the command used for making residues designable. This is usually
either "ALLAA" for all amino acids, or "PIKAA ..." for a restricted set of amino acids. The next arguments are the residues
which should be designable, with the chain and residue number separated by a colon.

----------------------------
Command line options
----------------------------

The seqtol_resfile.py script takes the following required options:
 - pdb_path. This specifies the input PDB structure;
 - design_command. As described above *e.g.* "ALLAA" or "PIKAA ADEFGHIKLMNPQRSTVWY" or "PIKAA AFILMPVW" *etc.*;
 - a list of designed positions. As described above *e.g.* B:2002 B:2003 B:2004 B:2005 B:2006.

--------------------------------------
Example seqtol_resfile.py Command Line
--------------------------------------

::

  scripts/seqtol_resfile.py input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:2002 B:2003 B:2004 B:2005 B:2006


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Commands to run the benchmark cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The construction of the resfiles for the cases is described in input/README.rst. For completeness, here are commands to
recreate data for the 2I0L case in the test_mode (for a full run, remove the argument "test_mode").

::

  cd protocols/backrub_seqtol
  echo "Creating the sequence tolerance resfile. This will be colocated with the input PDB file."
  ./seqtol_resfile.py ../../input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:2002 B:2003 B:2004 B:2005 B:2006
  echo "Running the simulations."
  ./backrub_seqtol.py ../../input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb 1 test_mode
  ./backrub_seqtol.py ../../input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb 2 test_mode
  ...
  ./backrub_seqtol.py ../../input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb 50 test_mode


The other cases are similar:

GB1 Fold Stability Tolerance

::

  scripts/backrub_seqtol_2QMT.py ${BENCHMARK_PATH}/input/pdbs/2QMT/2QMT.pdb 1
  scripts/backrub_seqtol_2QMT.py ${BENCHMARK_PATH}/input/pdbs/2QMT/2QMT.pdb 2
  ...

PDZ Domain Interface Tolerance

::

  scripts/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb 1
  scripts/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb 2
  ...

  scripts/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_%02i.pdb 1 ${BENCHMARK_PATH}/input/pdbs/1N7T_V83K/1N7T_V83K
  scripts/backrub_seqtol.py ${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_%02i.pdb 2 ${BENCHMARK_PATH}/input/pdbs/1N7T_V83K/1N7T_V83K
  ...

hGH/hGHR Interface Tolerance

::

  scripts/backrub_seqtol_1A22.py ${BENCHMARK_PATH}/input/pdbs/1A22_1/1A22_1.pdb 1
  scripts/backrub_seqtol_1A22.py ${BENCHMARK_PATH}/input/pdbs/1A22_1/1A22_1.pdb 2
  ...


