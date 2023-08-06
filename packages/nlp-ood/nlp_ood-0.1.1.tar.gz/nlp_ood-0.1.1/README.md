# Meta Domain Classification

## Introduction

Domain classification is the task of predicting a  out of domain or in domain label given an input text. In this tutorial, we focus on sentence-level domain classification, which consists of assigning a category label to individual sentences in a data set.

To approach this task, we have researched and experimented on different methods such as Out-of-Domain Contrastive, Out-of-Domain Bayesian, Out-of-Domain Energy.

***

## OOD-Contrastive

We develop an unsupervised OOD detection method, in which only the in-distribution (ID) data are used in training. We propose to fine-tune the Transformers with a contrastive loss, which improves the compactness of representations, such that OOD instances can be better differentiated from ID ones. These OOD instances can then be accurately detected using the Mahalanobis distance in the model's penultimate layer. We experiment with comprehensive settings and achieve near-perfect OOD detection performance, outperforming baselines drastically. We further investigate the rationales behind the improvement, finding that more compact representations through margin-based contrastive learning bring the improvement ([paper](https://arxiv.org/abs/2104.08812))

[Detail...](https://gitlab.ftech.ai/nlp/research/meta-domain-classification/-/tree/develop/ood-contrastive)

***

## OOD-Bayesian

We analyze overconfident OOD comes from distribution uncertainty due to the mismatch between the training and test distributions, which makes the model can’t confidently make predictions thus probably causing abnormal softmax scores. We propose a Bayesian OOD detection framework to calibrate distribution uncertainty using MonteCarlo Dropout.([paper](https://arxiv.org/pdf/2209.06612v1.pdf))

[Detail...](https://gitlab.ftech.ai/nlp/research/meta-domain-classification/-/tree/develop/ood-bayesian)

***

## OOD-Energy
We propose a unified framework for OOD detection that uses an energy score. We show that energy scores better distinguish in- and out-of-distribution samples than the traditional approach using the softmax scores. Unlike softmax confidence scores, energy scores are theoretically aligned with the probability density of the inputs and are less susceptible to the overconfidence issue ([paper](https://arxiv.org/abs/2010.03759))

[Detail...](https://gitlab.ftech.ai/nlp/research/meta-domain-classification/-/tree/develop/ood-energy)

***

## API
We have researched and tested the studied solution. After testing, we built an api that quickly deploys the application on other environments.

[API-docs](http://103.119.132.170:5053/docs)

[Detail...](https://gitlab.ftech.ai/nlp/research/meta-domain-classification/-/tree/develop/api)

***

## Demo
For the convenience of testing the solution, we quickly developed a web demo of out-of-domain data detection on a pre-built api.

[App](http://103.119.132.170:3039/)

[Detail...](https://gitlab.ftech.ai/nlp/research/meta-domain-classification/-/tree/develop/demo)

***

## License
For open source projects, say how it is licensed.
