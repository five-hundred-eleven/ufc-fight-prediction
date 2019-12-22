
import numpy as np
import pandas as pd

import category_encoders as ce
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

import pickle

import re


class FighterService:


    def __init__(self):

        self.__fighters_df = pd.read_csv("csv/fighters.csv")
        self.__sherdog_df = pd.read_csv("csv/ALL UFC FIGHTERS 2_23_2016 SHERDOG.COM - Sheet1.csv")

        with open("pickles/pipeline.pickle", "rb") as f:
            self.__pipeline = pickle.load(f)

        with open("pickles/features.pickle", "rb") as f:
            self.__features = pickle.load(f)

        prefix_re = re.compile(r".*(_opponent)|(_ratio)$")

        fighters_individual_df = self.__fighters_df[[col for col in self.__fighters_df.columns.drop(["is_winner"]) if not prefix_re.match(col)]]
        self.__latest_fights = fighters_individual_df.sort_values(by="date").groupby("fighter").tail(1)


    def getNickname(fighter):
        """
            Returns the nickname of the fighter, or an empty string if none found.

            @type fighter: str
            @rtype: str
        """

        fighter = self.__sherdog_df[self.__sherdog_df["name"] == fighter]

        if len(fighter) == 0:
            return ""

        return fighter.iloc[0]["nick"]


    def getAllFighters(self):
        """
            Returns a list of the names of all fighters.

            @rtype: List[str]
        """
        return list(self.__fighters_df["fighter"])


    def doPrediction(self, red_fighter, blue_fighter):
        """
            Given the names of two fighters, predicts which fighter would win.

            @type red_fighter: str
            @type blue_fighter: str

            @returns: a tuple containing a float representing the confidence in the prediction,
                and a string of the name of the winner.
        """
        bout = makeBoutDf(red_fighter, blue_fighter)
        probas = scoreBout(bout)

        red_fighter_prob = (probas.iloc[0]["True"] + probas.iloc[1]["False"])/2
        blue_fighter_prob = (probas.iloc[0]["False"] + probas.iloc[1]["True"])/2

        print(red_fighter_prob, "+", blue_fighter_prob, "=", red_fighter_prob+blue_fighter_prob)

        if red_fighter_prob > blue_fighter_prob:
            return red_fighter_prob, red_fighter

        else:
            return blue_fighter_prob, blue_fighter


    def __getByFighter(self, fighter_name):
        return self.__latest_fights[self.__latest_fights["fighter"] == fighter_name].copy()


    def __makeBoutDf(self, fighter1, fighter2):

        fighter1_df = getByFighter(fighter1)
        fighter2_df = getByFighter(fighter2)

        fighter1_df["temp_id_"] = fighter2_df["temp_id_"] = np.random.randint(2**31)
        fighter1_df, fighter2_df = (
            pd.merge(fighter1_df, fighter2_df, on="temp_id_", suffixes=("", "_opponent")),
            pd.merge(fighter2_df, fighter1_df, on="temp_id_", suffixes=("", "_opponent")),
        )

        fight_df = pd.concat([fighter1_df, fighter2_df])

        for col in [col for col in fight_df.select_dtypes(include="number").columns if col.endswith("_opponent")]:

            col2 = col
            col1 = col[:-9]

            fight_df[col1 + "_ratio"] = (fight_df[col1] + 1) / (fight_df[col2] + 1)

        fight_df["stance_config"] = fight_df["Stance"] + "-" + fight_df["Stance_opponent"]

        return fight_df.drop(columns=["temp_id_"])


    def __scoreBout(self, bout):
        return pd.DataFrame(data=pipeline.predict_proba(bout[self.__features]), columns=[str(x) for x in pipeline.classes_])



fighter_service = FighterService()
