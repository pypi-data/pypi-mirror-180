#%%
import os
import pandas as pd
import pooch
from abdu.ot import url_dc, path_target


class Load_db:
    def __init__(self, url=url_dc, target_name=path_target):
        path, fname = os.path.split(path_target)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df():
        df_bikes = pd.read_csv(
            path_target,
            na_values="",
            low_memory=False,
            converters={"data": str, "heure": str},
        )
        return df_bikes

# %%
df = Load_db().save_as_df()