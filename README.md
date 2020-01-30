# ufc-fight-prediction
[Link to the app](https://ufcpredict.stromsy.com/predict)

### Which Fighter Would Win?

In the UFC, the Vegas Odds for a given fight show who is the favorite and who is the underdog. Those who have insights on the fighters stand to make a lot of money on bets.

Besides for the bets, it's inherently interesting for MMA enthusiasts to think about which fighter would win a given fight.

The purpose of this project was to use data analysis to determine who would win. Note that we allow for fighters from different eras and different weight classes to be compared. Long-retired fighters are imagined to be in their primes, and any two fighters being compared are imagined to be fighting at the same weight.


### Insights
For full methodology, consult [this notebook](https://github.com/ekoly/ufc-fight-prediction/blob/master/ipynb/ufc-predictions.ipynb).

Each fight was divided into two rows- one focusing on the red fighter and another focusing on the blue fighter. The target was a column called "is_winner", which is True if the fighter won or False if the fighter lost or if the fight ended in a tie. The baseline accuracy by choosing the majority class ("lose or tie") every time was 50.81%.

We proceeded to test a Logistic Regression, a Random Forest Classifier, and an XGBClassifier to try to predict the outcome of UFC fights. The accuracy of the Logistic Regression was originally 64.81%. Interestingly it did not converge, even with the number of iterations jacked up to 333. The accuracy of the Random Forest Classifier was originally 64.97%, which was very similar to the Logistic Regression. The accuracy of the XGBClassifier with it's parameters optimized with a RandomizedSearchCV was originally 65.75%, about a percentage point higher than the others.

The models were further optimized with Permutation Importance. This increased the efficiency of the models by reducing the size of the inputs, but it made no significant difference in accuracy.

While the XGB Classifier yielded the highest accuracy, its reported confidence was in the high 90s for many predictions. This level of confidence is highly dubious for a UFC fight prediction. We decided to use the Random Forest Classifier for the app, because of its more realistic confidence.

Oddly, the model often outputs different results depending on which fighter is on the left and which is on the right. This was mitigated by making two predictions for each fight, one in each fighter configuration, and going with whichever prediction has the higher confidence level.


### Positive Features

This graphic shows features that were highly predictive of the winner.
The green bars are the best estimate of predictiveness and the thin bars
are the margin of error.
                
Here are some notes to help you interpret it:
* Features **not** ending in "\_opponent" are features of the red fighter. 
* Features that **do** end in "\_opponent" are features of the blue fighter.
* Features ending in "\_ratio" are the feature of the red fighter over the feature of the blue fighter.
* Features containing "\_opp\_" represent the average of that action that the fighter **receives** during fights.
* "att" usually means attempts
* "td" usually means takedowns

![positive features](https://github.com/ekoly/ufc-fight-prediction/blob/master/img/positive-features.png?raw=true)

### Negative Features

This graphic shows features that caused predictions to become worse when included in the analysis.

![negative features](https://github.com/ekoly/ufc-fight-prediction/blob/master/img/negative-features.png?raw=true)

### Isolated Partial Dependance Plots

The following plots show the likelyhood of a win based on individual features. Higher y-values represent higher likelyhood of winning the fight.

![age ratio](https://github.com/ekoly/ufc-fight-prediction/blob/master/img/age-ratio.png?raw=true)
![reach ratio](https://github.com/ekoly/ufc-fight-prediction/blob/master/img/reach-ratio.png?raw=true)
![current win streak](https://github.com/ekoly/ufc-fight-prediction/blob/master/img/current-win-streak.png?raw=true)
