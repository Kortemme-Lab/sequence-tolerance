==============================
Sun Grid Engine job submission
==============================

The protocols/backrub_seqtol/backrub_seqtol.py script functions as both a submission script for a workstation and for an SGE
cluster engine. The user is referred to the documentation in protocols/backrub_seqtol/README.rst for a more detailed
explanation of what the script does.

In particular, the *Configuration* section of protocols/backrub_seqtol/README.rst should be followed for the commands below
to work.

----------------------------
Command line options
----------------------------

The backrub_seqtol.py script takes the following options for SGE cluster submission:

- PDB_PATH environment variable, set with the -v qsub option. Required option. This specifies the input PDB structure;
- SGE_TASK_ID environment variable. This is not set explicitly; it is set using the -t qsub option *e.g.* -t 1-20 performs 20 runs of the script and each runs with a separate task ID;
- INPUT_PATH environment variable, set with the -v qsub option. Optional, defaults to the directory containing pdb_path.

The -N qsub option used in the examples below simply names the job on the cluster and is optional.

----------------------------
Paths and extensions
----------------------------

The command lines below use placeholders for paths and extensions. Please change these appropriately *e.g.*:

::

  BENCHMARK_PATH=<path/to/sequence-tolerance>

(where BENCHMARK_PATH should be set to the root directory of this benchmark capture) or use the create_qsub_commands.py
script (see below). Edit protocols/backrub_seqtol/settings.json to set the output path and the path to the Rosetta installation.

Note that the extension will change depending on what options were used to build Rosetta and on the architecture of the
machine used for the build.

-----------------------------
How to run the full benchmark
-----------------------------

These commands create data for the different benchmark cases. For test runs, add the argument "test_mode" to each line.

~~~~~~~~~~~~~~~~~~~~~~~
create_qsub_commands.py
~~~~~~~~~~~~~~~~~~~~~~~

To help with using the command lines below, we have included a helper script to generate the full command lines based on
a value for BENCHMARK_PATH. This can be used as follows *e.g.*:

::

  python create_qsub_commands.py BENCHMARK_PATH

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GB1 Fold Stability Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/2QMT/2QMT.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/2QMT -t 1-20 -N bs_2QMT ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PDZ Domain Interface Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/2I0L_A_C_V2006 -t 1-200 -N bs_2I0L_A_C_V2006 ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py
  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/2IWP_B_A_V1927/2IWP_B_A_V1927.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/2IWP_B_A_V1927 -t 1-200 -N bs_2IWP_B_A_V1927 ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py
  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/2FNE_A_C_V2048/2FNE_A_C_V2048.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/2FNE_A_C_V2048 -t 1-200 -N bs_2FNE_A_C_V2048 ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py
  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_%02i.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/1N7T -t 1-200 -N bs_1N7T ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py
  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/1N7T/1N7T_%02i.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/1N7T_V83K -t 1-200 -N bs_1N7T_V83K ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hGH/hGHR Interface Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/1A22_1/1A22_1.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/1A22_1 -t 1-100 -N bs_1A22_1 ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py
  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/1A22_2/1A22_2.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/1A22_2 -t 1-100 -N bs_1A22_2 ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py
  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/1A22_3/1A22_3.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/1A22_3 -t 1-100 -N bs_1A22_3 ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py
  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/1A22_4/1A22_4.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/1A22_4 -t 1-100 -N bs_1A22_4 ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py
  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/1A22_5/1A22_5.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/1A22_5 -t 1-100 -N bs_1A22_5 ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py
  qsub -v BENCHMARK_PATH=${BENCHMARK_PATH} -v PDB_PATH=${BENCHMARK_PATH}/input/pdbs/1A22_6/1A22_6.pdb -v INPUT_PATH=${BENCHMARK_PATH}/input/backrub_seqtol/1A22_6 -t 1-100 -N bs_1A22_6 ${BENCHMARK_PATH}/protocols/backrub_seqtol/backrub_seqtol.py

------------------------------
Analyzing the benchmark output
------------------------------

See analysis/README.rst for a full description of the analysis scripts. Briefly, navigate to the directory where the output
was produced and call the analysis e.g.

::

  cd output/sample
  R
  > source("../../analysis/sequence_tolerance.R")
  > process_seqtol()
