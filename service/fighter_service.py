
import numpy as np
import pandas as pd

import category_encoders as ce
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


class FighterService:


    def __init__(self):

        self.__fighters_df = pd.read_csv("csv/fighters.csv")
        self.__sherdog_df = pd.read_csv("csv/ALL UFC FIGHTERS 2_23_2016 SHERDOG.COM - Sheet1.csv")


    def getNickname(fighter):
        """
            @type fighter: str
            @rtype: str
        """

        fighter = self.__sherdog_df[self.__sherdog_df["name"] == fighter]

        if len(fighter) == 0:
            return ""

        return fighter.iloc[0]["nick"]


    def getAllFighters():
        """
            @rtype: List[str]
        """
        return list(self.__fighters_df["fighter"])



fighter_service = FighterService()
