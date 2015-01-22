-------------------------------------------
backrub_seqtol (Backrub/Sequence Tolerance)
-------------------------------------------

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

____________________
Required input files
____________________
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+============================+===================================================================================================================================================================================+
| <base name>_seqtol.resfile | This resfile specifies which sequence positions to sample, along with the residue positions that should be repacked. This file can be created using the seqtol_resfile.py script. |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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


~~~~~~~~~~~~~~~~~
seqtol_resfile.py
~~~~~~~~~~~~~~~~~

The seqtol_resfile.py takes as input a PDB file and generates a resfile for use with the sequence_tolerance app. It takes
at least two other required arguments. The first is the command used for making residues designable. This is usually
either "ALLAA" for all amino acids, or "PIKAA ..." for a restricted set of amino acids. The next arguments are the residues
which should be designable, with the chain and residue number separated by a colon.

______________________________________
Example seqtol_resfile.py Command Line
______________________________________

::

  scripts/seqtol_resfile.py input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb "PIKAA ADEFGHIKLMNPQRSTVWY" B:2002 B:2003 B:2004 B:2005 B:2006

