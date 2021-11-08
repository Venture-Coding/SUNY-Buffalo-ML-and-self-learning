## Understanding the Parameters for Information Gain ##

The decision tree whenever splits, needs a basis for finalising which 'split' to place where, viz. identifying the root node and progressive nodes until reaching the leaf node. The *Information Gain* is considered as the basis of choosing the right split.

Entropy calculation and Gini Impurity calculation are two of the leading methods to finalize what kind of split is to be performed from the root node, towards leaf node.

### Entropy ###

Formula:

      *H(Y) = - ∑ (p(yj) * log2(p(yj)))

Here ‘p(yj)’ is simply the frequentist probability of an element/class ‘j’ in our output(y) data.

<img width="495" alt="Screenshot 2021-11-08 at 8 33 23 PM" src="https://user-images.githubusercontent.com/61674750/140765808-af94bb5d-8ae9-43d3-aba7-b0c658fc9bd5.png">

Entropy is lowest at the extremes, when the curve either contains no positive instances or only positive instances. That is, when the curve is pure the disorder is 0. Entropy is highest in the middle when the curve is evenly split between positive and negative instances. Extreme disorder , because there is no majority.

Information Gain using Entropy: 

   *IG(S, a) = H(S) – H(S | a)
   
Where IG(S, a) is the information for the dataset S for the variable a for a random variable, H(S) is the entropy for the dataset before any change (described above) and H(S | a) is the conditional entropy for the dataset given the variable a.

The conditional entropy can be calculated by splitting the dataset into groups for each observed value of a and calculating the sum of the ratio of examples in each group out of the entire dataset multiplied by the entropy of each group.

   *H(S | a) = sum v in a Sa(v)/S * H(Sa(v))
   
Where Sa(v)/S is the ratio of the number of examples in the dataset with variable a has the value v, and H(Sa(v)) is the entropy of group of samples where variable a has the value v.


### Gini Impurity ###

