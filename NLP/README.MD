# This sub repo is dedicated for NLP Lecture
### Inside this repo
> Word embedding (word2vec)
>> **CBOW**: get rid of word order, takes the the vector embedding n words before the target  and after the target and adds them.
examples: removing the middle word from a sentence and guessing the middle word
<Br> one hot encoding is used in CBOW, which takes input as vector that has 10 nodes for example as 0 and only one node is 1, then it's passed to the hidden layer, and at the output it decides which node should be highlighted thus giving us the missing word

>>**Skip-Gram**: starts with a word and try to predict surrounding words.
