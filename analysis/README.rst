====================================
Metrics
====================================

This benchmark uses four different metrics:

- Average absolute distance (AAD);
- Area under the receiver operator characteristic (ROC) curve (AUC);
- Frobenius distance; and
- Rank top.

For more complete explanations of the metrics, the reader is referred to the 2010 publication from Smith and Kortemme [1]_. Much
of the text below paraphrases explanations from that paper. In that paper, the authors mention that the combination of all of
the metrics helped to guide and improve performance of their method.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Average absolute distance (AAD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The average absolute difference is used to present the average amino acid frequency error when comparing the predictions
with phage display results. A prediction is considered to be perfect if the AAD is 0%, good if the AAD is <6%, and worst
if the AAD is 10%.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Area under the receiver operator characteristic curve (AUC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The most populated amino acids are defined as those with phage display frequency ≥ 10%. The AUC metric depends solely on
the relative ranking of amino acids, indicating how well the prediction ranks the most populated amino acids. An AUC score
of 0.5 represents random predictive power, 0.75 represents a good score/prediction, and 1.0 represents a perfect score.

~~~~~~~~~~~~~~~~~~
Frobenius distance
~~~~~~~~~~~~~~~~~~

The Frobenius distance/norm (or Euclidean norm) is also considered. The best score is 0 and the worst is 2\ :sup:`1/2`. On its own,
this metric appears to be biased towards rewarding flat profiles rather than profiles with more information content / specificity \[\ 1_\].

~~~~~~~~
Rank top
~~~~~~~~

The predicted rank of the most frequent experimentally observed amino acid. When the prediction has a tie situation, the
maximum rank should be used \[\ 1_\].


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Correlations between the metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Figure 5 in the 2010 paper suggests that the AAD and Frobenius distance metrics are highly correlated (an expected result)
for the dataset in that paper, as are the Rank top and AUC metrics which both consider the most frequently predicted amino
acids.

================
Running analysis
================

~~~~~~~~~~~~~~
Required tools
~~~~~~~~~~~~~~

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


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Changes in the output format since the 2010 paper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output of the sequence tolerance application changed in Rosetta version 36344 (2010). The versions of the analysis scripts contained
herein expect output in the original format. The analysis/convert_new_seqtol_to_old.py script changes the output from newer revisions
into the older format so that the analysis scripts will continue to work.

~~~~~~~~~~~~~~~
Troubleshooting
~~~~~~~~~~~~~~~

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


==========
References
==========

.. [1] Smith, CA, Kortemme, T. Structure-Based Prediction of the Peptide Sequence Space Recognized by Natural and Synthetic PDZ Domains. 2010. J Mol Biol 402(2):460-74. `doi: 10.1016/j.jmb.2010.07.032 <http://dx.doi.org/10.1016/j.jmb.2010.07.032>`_.
