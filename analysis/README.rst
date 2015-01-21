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

-------------------------------
Average absolute distance (AAD)
-------------------------------

The average absolute difference is used to present the average amino acid frequency error when comparing the predictions
with phage display results. A prediction is considered to be perfect if the AAD is 0%, good if the AAD is <6%, and worst
if the AAD is 10%.

-----------------------------------------------------------
Area under the receiver operator characteristic curve (AUC)
-----------------------------------------------------------

The most populated amino acids are defined as those with phage display frequency ≥ 10%. The AUC metric depends solely on
the relative ranking of amino acids, indicating how well the prediction ranks the most populated amino acids. An AUC score
of 0.5 represents random predictive power, 0.75 represents a good score/prediction, and 1.0 represents a perfect score.

------------------
Frobenius distance
------------------

The Frobenius distance/norm (or Euclidean norm) is also considered. The best score is 0 and the worst is 2\ :sup:`1/2`. On its own,
this metric appears to be biased towards rewarding flat profiles rather than profiles with more information content / specificity \[\ 1_\].

--------
Rank top
--------

The predicted rank of the most frequent experimentally observed amino acid. When the prediction has a tie situation, the
maximum rank should be used \[\ 1_\].


--------------------------------
Correlations between the metrics
--------------------------------

Figure 5 in the 2010 paper suggests that the AAD and Frobenius distance metrics are highly correlated (an expected result)
for the dataset in that paper, as are the Rank top and AUC metrics which both consider the most frequently predicted amino
acids.

~~~~~~~~~~
References
~~~~~~~~~~

.. [1] Smith, CA, Kortemme, T. Structure-Based Prediction of the Peptide Sequence Space Recognized by Natural and Synthetic PDZ Domains. 2010. J Mol Biol 402(2):460-74. `doi: 10.1016/j.jmb.2010.07.032 <http://dx.doi.org/10.1016/j.jmb.2010.07.032>`_.
