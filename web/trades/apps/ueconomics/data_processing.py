from django.conf import settings
import pandas as pd
import numpy as np
import math
from openpyxl.utils.dataframe import dataframe_to_rows
import csv
import pickle
from openpyxl import Workbook, load_workbook
from ..core.algo_utilities import Algo
from .models import Source, Product, YearData


class AlgoUE(Algo):
    def __init__(self):
        super().__init__(chapter_id="ueconomics", target_field=None)

    def upload_data_to_database(self):
        df_exports = self.load_excel_data('exports')
        df_imports = self.load_excel_data('imports')
        # print(df_imports)
        print('exports')

        source_exports, created = Source.objects.get_or_create(type='exports')
        print(created)
        print(source_exports)
        if created:
            for index, row in df_exports.iterrows():
                description_ = row['Description']
                sitc2_ = row['SITC2']
                print(description_, sitc2_)
                product, created = Product.objects.get_or_create(sitc2=sitc2_, description=description_)
                for ny in range(2015, 2020):
                    y = 'Y' + str(ny)
                    v = row[y]
                    yd, created = YearData.objects.get_or_create(source=source_exports, product=product, year=ny, value=v)

        source_imports, created = Source.objects.get_or_create(type='imports')
        if created:
            for index, row in df_imports.iterrows():
                description_ = row['Description']
                sitc2_ = row['SITC2']
                product, created = Product.objects.get_or_create(sitc2=sitc2_, description=description_)
                for ny in range(2015, 2020):
                    y = 'Y' + str(ny)
                    v = row[y]
                    yd, created = YearData.objects.get_or_create(source=source_imports, product=product, year=ny, value=v)

    def get_data(self):
        qs = YearData.objects.all()
        q = qs.values('source', 'product', 'year', 'value')
        pd_ = pd.DataFrame.from_records(q)
        source = Source.objects.all()
        product = Product.objects.all()
        return pd_, product, source



