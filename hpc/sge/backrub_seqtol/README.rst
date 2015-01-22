========================
Sun Grid Engine qsub lines
========================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GB1 Fold Stability Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  qsub -v PDB_PATH=input_files/2QMT/2QMT.pdb -t 1-20 -N bs_2QMT scripts/backrub_seqtol.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PDZ Domain Interface Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  qsub -v PDB_PATH=input_files/2I0L_A_C_V2006/2I0L_A_C_V2006.pdb -t 1-200 -N bs_2I0L_A_C_V2006 scripts/backrub_seqtol.py
  qsub -v PDB_PATH=input_files/2IWP_B_A_V1927/2IWP_B_A_V1927.pdb -t 1-200 -N bs_2IWP_B_A_V1927 scripts/backrub_seqtol.py
  qsub -v PDB_PATH=input_files/2FNE_A_C_V2048/2FNE_A_C_V2048.pdb -t 1-200 -N bs_2FNE_A_C_V2048 scripts/backrub_seqtol.py
  qsub -v PDB_PATH=input_files/1N7T/1N7T_%02i.pdb -v INPUT_PATH=input_files/1N7T/1N7T -t 1-200 -N bs_1N7T scripts/backrub_seqtol.py
  qsub -v PDB_PATH=input_files/1N7T/1N7T_%02i.pdb -v INPUT_PATH=input_files/1N7T_V83K/1N7T_V83K -t 1-200 -N bs_1N7T_V83K scripts/backrub_seqtol.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hGH/hGHR Interface Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  qsub -v PDB_PATH=input_files/1A22_1/1A22_1.pdb -t 1-100 -N bs_1A22_1 scripts/backrub_seqtol.py
  qsub -v PDB_PATH=input_files/1A22_2/1A22_2.pdb -t 1-100 -N bs_1A22_2 scripts/backrub_seqtol.py
  qsub -v PDB_PATH=input_files/1A22_3/1A22_3.pdb -t 1-100 -N bs_1A22_3 scripts/backrub_seqtol.py
  qsub -v PDB_PATH=input_files/1A22_4/1A22_4.pdb -t 1-100 -N bs_1A22_4 scripts/backrub_seqtol.py
  qsub -v PDB_PATH=input_files/1A22_5/1A22_5.pdb -t 1-100 -N bs_1A22_5 scripts/backrub_seqtol.py
  qsub -v PDB_PATH=input_files/1A22_6/1A22_6.pdb -t 1-100 -N bs_1A22_6 scripts/backrub_seqtol.py
