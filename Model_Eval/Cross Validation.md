In train-test split, we have three options:

  Simply split into train and test: But that way tuning a hyperparameter makes the model 'see' the test data (i.e. knowledge of test data leaks into the model)
  Split into train, validation, test sets: Then the validation data would eat into the training set
  Cross-validation: Split into train and test, and train multiple models by sampling the train set. Finally, just test once on the test set.
  
So, Cross Val is used to avoid cheating by looking at the test during tuning of the Hyperparameters. Thus, making the model mroe robust and future-proof.

<img width="727" alt="Screenshot 2021-11-08 at 11 39 34 AM" src="https://user-images.githubusercontent.com/61674750/140693052-b6fde009-faf8-41f8-a726-cdb54ea327bb.png">

 *The various types of cross-validation are - :
    *K-fold cross-validation
    *Leave one out(LOO)
    *Leave P-out(LPO)
    *Stratified K-Fold 
     
1. jjj
   1. uuu

For more information on the above methods, please go through the documentation at sklearn.
