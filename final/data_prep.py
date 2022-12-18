import pickle

import numpy as np
import pandas as pd
from category_encoders import CatBoostEncoder

class DataPrep:
    def __init__(self):
        pass

    def fit(self, df, cat_cols):
        df = self._fill_na(df)
        df = self._fe(df)

        self.cat_cols = cat_cols + ['st_code_snd__st_code_rsv']
        self.enc = CatBoostEncoder(self.cat_cols).fit(df[self.cat_cols], df['y'])

    def transform(self, df, transform_y=False, method='4'):
        df = self._fill_na(df)
        df = self._fe(df)
        df[self.cat_cols] = self.enc.transform(df[self.cat_cols])

        if transform_y:
            df['y'] = self.transform_y(df['y'], method=method)

        return df

    def fit_transform(self, df, cat_cols, transform_y=False, method='4'):
        self.fit(df, cat_cols)
        return self.transform(df, transform_y, method)

    def _fill_na(self, df):
        df['distance'] = df['distance'].fillna(0)
        df['vidsobst'] = df['vidsobst'].fillna(pd.Series.mode(df['vidsobst'])[0]).astype(int)
        df['common_ch'] = df['common_ch'].fillna(0).astype(int)
        df['route_type'] = df['route_type'].fillna(0).astype(int)
        df['fr_id'] = df['fr_id'].fillna(2261).astype(int)
        return df

    def _fe(self, df):
        df = df[df['date_depart_year'] >= 2020]
        df['date_depart_month_sin'] = np.sin(2 * np.pi * df['date_depart_month'] / 12)
        df['date_depart_month_cos'] = np.cos(2 * np.pi * df['date_depart_month'] / 12)
        df['date_depart_week_sin'] = np.sin(2 * np.pi * df['date_depart_week'] / 52)
        df['date_depart_week_cos'] = np.cos(2 * np.pi * df['date_depart_week'] / 52)
        df['date_depart_day_sin'] = np.sin(2 * np.pi * df['date_depart_day'] / 31)
        df['date_depart_day_cos'] = np.cos(2 * np.pi * df['date_depart_day'] / 31)
        df['date_depart_hour_sin'] = np.sin(2 * np.pi * df['date_depart_hour'] / 24)
        df['date_depart_hour_cos'] = np.cos(2 * np.pi * df['date_depart_hour'] / 24)
        df['date_depart_year'] = df['date_depart_year'] - 2020

        df = df.drop(['date_depart_month', 'date_depart_week', 'date_depart_day', 'date_depart_hour'], axis=1)

        df['is_eq_rsv_snd_roadid'] = (df['rsv_roadid'] == df['snd_roadid']).astype(int)
        df['is_eq_rsv_snd_dp_id'] = (df['rsv_dp_id'] == df['snd_dp_id']).astype(int)

        df['distance_sqrt'] = np.sqrt(df['distance'])
        df['distance_cos'] = np.cos(df['distance'])
        df['distance_x_route_type'] = df['distance'] * df['route_type']
        df['st_code_snd__st_code_rsv'] = df['st_code_snd'] + "__" + df['st_code_rsv']
        return df

    def transform_y(self, y, method='4'):
        if method == '4':
            return y ** 0.25
        elif method == '2':
            return y ** 0.5
        elif method == 'log':
            return np.log1p(y)
        else:
            return y

