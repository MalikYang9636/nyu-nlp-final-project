# nyu-nlp-final-project
NYU NLP Final Project: Build a semantic role labeling system utilizing SOTA machine learning models

## Authors

- [Ziyang Zeng](https://github.com/dizys): Maxent Baseline, DistilBERT related experiments
- [Jiahao Chen](https://github.com/jc10347): Random Forest
- [Peiwen Tang](https://github.com/ppppppw): RoBERTA, Feature engineering, Word2Vec and downstream experiments
- [Zeyu Yang](https://github.com/MalikYang9636): BERT base model

## Experiments

- Baseline: [Maxent](https://github.com/dizys/nyu-nlp-homework-6)
- Word2Vec: [Feature Extraction](./feature_extraction/word2vec.py) and [Classification](./feature_extraction/hf_transformer_word2vec.ipynb)
- Random Forest: [Notebook](./src/RandomForest.ipynb)
- BERT (base): [Notebook](./src/bert_based.ipynb)
- DistilBERT: [Notebook](./src/hf_transformer.ipynb)
- RoBERTA: [Notebook](./src/hf_transformer_roberta.ipynb)
- DistilBERT (POS+BIO): [Notebook](./src/hf_transformer_enhanced.ipynb)
- DistilBERT (QA): [Notebook](./src/hf_transformer_qa.ipynb)
- DistilBERT (ONE ARG1): [Notebook](./src/hf_transformer_one_arg.ipynb)

## Results

On %-test:

| Model                     | Precision | Recall |    F1     | Output                                              |
| :------------------------ | :-------: | :----: | :-------: | :-------------------------------------------------- |
| Maxent                    |   71.88   | 61.33  |   66.19   | [txt](./out/%-out/test-out-maxent.txt)              |
| RandomForest              |   64.53   | 74.00  |   68.94   | [txt](./out/%-out/test-out-rf.txt)                  |
| BERT                      |   91.33   | 91.33  |   91.33   | [txt](./out/%-out/test-out-bert.txt)                |
| DistilBERT                |   93.75   | 90.00  |   91.84   | [txt](./out/%-out/test-out-distilbert.txt)          |
| RoBERTA                   |   91.50   | 93.33  |   92.41   | [txt](./out/%-out/test-out-RoBERTA.txt)             |
| DistilBERT (POS+BIO)      |   93.19   | 91.33  |   92.25   | [txt](./out/%-out/test-out-distilbert-enhanced.txt) |
| DistilBERT (QA)           |   92.00   | 92.00  |   92.00   | [txt](./out/%-out/test-out-distilbert-qa.txt)       |
| **DistilBERT (ONE ARG1)** |   92.67   | 92.67  | **92.67** | [txt](./out/%-out/test-out-distilbert-one-arg1.txt) |

On total-test:

| Model      | Precision | Recall |  F1   | Output                                         |
| :--------- | :-------: | :----: | :---: | :--------------------------------------------- |
| Maxent     |   55.33   | 36.02  | 43.64 | [txt](./out/total-out/test-out-maxent.txt)     |
| DistilBERT |   80.49   | 78.43  | 79.45 | [txt](./out/total-out/test-out-distilbert.txt) |
