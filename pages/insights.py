import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objects as go

from app import app

import numpy as np

column00 = dbc.Col(
    [
        dcc.Markdown(
            """
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
            """
        ),
    ],
    md=4,
)
column01 = html.Img(id="pos-features", src="/img/positive-features.png")

column10 = dbc.Col(
    [
        dcc.Markdown(
            """
                ### Negative Features

                This graphic shows features that caused predictions to become worse when included in the analysis.
            """
        ),
    ],
    md=4,
)
column11 = html.Img(id="neg-features", src="/img/negative-features.png")

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Markdown("""
                # Insights

                For full methodology, consult [this notebook](https://github.com/ekoly/ufc-fight-prediction/blob/master/ipynb/ufc-predictions.ipynb).

                Each fight was divided into two rows- one focusing on the red fighter and another focusing on the blue fighter. The target was a column called "is_winner",
                which is True if the fighter won or False if the fighter lost or if the fight ended in a tie. The baseline accuracy by choosing the majority class ("lose or tie") every time was 50.81%.

                We proceeded to test a Logistic Regression, a Random Forest Classifier, and an XGBClassifier to try to predict the outcome of UFC fights. The accuracy of the Logistic Regression was originally 64.81%. Interestingly
                it did not converge, even with the number of iterations jacked up to 333. The accuracy of the Random Forest Classifier was originally 64.97%, which was very similar to the Logistic Regression. The accuracy
                of the XGBClassifier with it's parameters optimized with a RandomizedSearchCV was originally 65.75%, about a percentage point higher than the others.

                The models were further optimized with Permutation Importance. This increased the efficiency of the models by reducing the size of the inputs, but it made no significant difference in accuracy.

                While the XGB Classifier yielded the highest accuracy, its reported confidence was in the high 90s for many predictions. This level of confidence is highly dubious for a UFC fight prediction. We decided to use
                the Random Forest Classifier for the app, because of its more realistic confidence.

                Oddly, the model often outputs different results depending on which fighter is on the left and which is on the right. This was mitigated by making two predictions for each fight, one in each fighter configuration,
                and going with whichever prediction has the higher confidence level.

                ### Isolated Partial Dependance Plots

                The following plots show the likelyhood of a win based on individual features. Higher y-values represent higher likelyhood of winning the fight.

            """),
            html.Img(id="age-ratio", src="/img/age-ratio.png"),
            html.Img(id="reach-ratio", src="/img/reach-ratio.png"),
            html.Img(id="win-streak", src="/img/current-win-streak.png"),
        ])
    ]),
    dbc.Row([column00, column01]),
    dbc.Row([column10, column11]),
])
