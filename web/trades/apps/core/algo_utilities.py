import warnings
import os
from django.conf import settings
import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from sklearn import linear_model, neighbors
from sklearn import preprocessing
from sklearn import pipeline
import tarfile
from six.moves import urllib
import hashlib
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
import matplotlib.image as mpimg
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import cross_val_score
from scipy import stats
import joblib
"""
 to_data_path_ is the place datasets are kept
 chapter_id name of the chapter to store images_
"""

mpl.use('Agg')


class Algo(object):
    def __init__(self, chapter_id, target_field):
        self.CHAPTER_ID = chapter_id
        print('chapter_id')

        warnings.filterwarnings(action="ignore", message="^internal gelsd")
        # to make this notebook's output stable across runs
        self.RANDOM_STATE = 42
        np.random.seed(self.RANDOM_STATE)
        # To plot pretty figures
        mpl.rc('axes', labelsize=14)
        mpl.rc('xtick', labelsize=12)
        mpl.rc('ytick', labelsize=12)

        # Where to save the figures
        # --- Change to this when you start to use Django ---
        self.PROJECT_ROOT_DIR = os.path.join(os.path.dirname(settings.WEB_DIR), "data", self.CHAPTER_ID)
        os.makedirs(self.PROJECT_ROOT_DIR, exist_ok=True)
        self.TO_DATA_PATH = os.path.join(self.PROJECT_ROOT_DIR, "datasets")
        os.makedirs(self.TO_DATA_PATH, exist_ok=True)
        # print(self.TO_DATA_PATH)

        self.IMAGES_PATH = os.path.join(self.PROJECT_ROOT_DIR, "images_")
        os.makedirs(self.IMAGES_PATH, exist_ok=True)
        # print(self.IMAGES_PATH)

        self.MODELS_PATH = os.path.join(self.PROJECT_ROOT_DIR, "models")
        os.makedirs(self.MODELS_PATH, exist_ok=True)
        # print(self.MODELS_PATH)

        self.TARGET_FIELD = target_field
        self.DATA = None
        self.TRAIN = None
        self.TEST = None
        self.TRAIN_TARGET = None
        self.TRAIN_DATA = None
        self.TEST_TARGET = None
        self.TEST_DATA = None
        self.train_data = None
        self.test_data = None
        self.num_attribs = None
        self.extra_attribs = None
        self.model = None
        self.HASH = hashlib.md5
        self.PIPELINE = None

    def save_fig(self, fig_id, tight_layout=True, fig_extension="png", resolution=300):
        path = os.path.join(self.IMAGES_PATH, fig_id + "." + fig_extension)
        if not os.path.isfile(path):
            print("Saving figure", fig_id)
            if tight_layout:
                plt.tight_layout()
            plt.savefig(path, format=fig_extension, dpi=resolution)

    def create_gz_file(self, file_from="dual_single.csv", file_to="dual_single.tar.gz"):
        print(666)
        csv_path = os.path.join(self.TO_DATA_PATH, file_from)
        gz_path = os.path.join(self.TO_DATA_PATH, file_to)
        if not os.path.isfile(gz_path):
            with open(os.path.join(self.TO_DATA_PATH, file_to), 'w') as fp:
                pass
        tar = tarfile.open(gz_path, "w:gz")
        tar.add(csv_path)
        tar.close()

    def fetch_tgz_data(self, from_url, tgz_name, ext="tgz"):
        tgz_path = os.path.join(self.TO_DATA_PATH, tgz_name + "." + ext)
        urllib.request.urlretrieve(from_url, tgz_path)
        tgz = tarfile.open(tgz_path)
        if ext=="tgz":
            tgz.extractall(path=self.TO_DATA_PATH)
        elif  ext=="gz":
            tgz.extractall(path="c:\\")
        tgz.close()
        os.remove(tgz_path)

    def load_csv_data(self, file):
        csv_path = os.path.join(self.TO_DATA_PATH, file + ".csv")  # "housing"
        self.DATA = pd.read_csv(csv_path)
        return self.DATA

    def load_excel_data(self, file):
        excel_path = os.path.join(self.TO_DATA_PATH, file + ".xlsx")
        self.DATA = pd.read_excel(excel_path)
        return self.DATA

    # less recommended
    def split_train_test(self, data=None, test_ratio=0.2):
        if data is None:
            data = self.DATA
        shuffled_indices = np.random.permutation(len(data))
        test_set_size = int(len(data) * test_ratio)
        test_indices = shuffled_indices[:test_set_size]
        train_indices = shuffled_indices[test_set_size:]
        self.TRAIN = data.iloc[train_indices]
        self.TEST = data.iloc[test_indices]
        return self.TRAIN, self.TEST

    # less recommended
    def test_set_check(self, identifier, test_ratio=0.2):
        return bytearray(self.HASH(np.int64(identifier)).digest())[-1] < 256 * test_ratio

    # less recommended
    def split_train_test_by_id(self, data=None, test_ratio=0.2, id_column=""):
        if data is None:
            data = self.DATA
        ids = data[id_column]
        in_test_set = ids.apply(lambda id_: self.test_set_check(id_, test_ratio))
        self.TRAIN = data.loc[~in_test_set]
        self.TEST = data.loc[in_test_set]
        return self.TRAIN, self.TEST

    def train_test_split(self, data=None, test_size=0.2):
        if data is None:
            data = self.DATA
        self.TRAIN, self.TEST = train_test_split(self.DATA, test_size=test_size, random_state=self.RANDOM_STATE)
        self.set_target_data()

    # Recommended method
    def train_test_stratified_split(self, data=None, test_size=0.2, field=None, bins=[], lables=[]):
        if data is None:
            data = self.DATA
        data["temp"] = pd.cut(data[field], bins=bins, labels=lables)
        split_ = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=self.RANDOM_STATE)
        for train_index, test_index in split_.split(data, data["temp"]):
            strat_train_set = data.loc[train_index]
            strat_test_set = data.loc[test_index]
        for set_ in (strat_train_set, strat_test_set):
            set_.drop("temp", axis=1, inplace=True)
        self.TRAIN, self.TEST = strat_train_set, strat_test_set
        self.set_target_data()

    def set_target_data(self):
        self.TRAIN_DATA = self.TRAIN.drop(self.TARGET_FIELD, axis=1)  # drop labels for training set
        self.TRAIN_TARGET = self.TRAIN[self.TARGET_FIELD].copy()
        self.TEST_DATA = self.TEST.drop(self.TARGET_FIELD, axis=1)  # drop labels for test set
        self.TEST_TARGET = self.TEST[self.TARGET_FIELD].copy()

    def plot(self, x=None, y=None, s=None, snf=1, c=None, fig_name=None, img_name=None, img_type="png"):
        if img_name is not None:
            image_path = os.path.join(self.IMAGES_PATH, img_name + '.' + img_type)
            img_ = mpimg.imread(image_path)
            ax = self.TRAIN.plot(kind="scatter", x=x, y=y, alpha=0.4, s=self.TRAIN[s] / snf, label="population",
                                 figsize=(10, 7), c=c, cmap=plt.get_cmap("jet"), colorbar=False, sharex=False)
            plt.imshow(img_, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5, cmap=plt.get_cmap("jet"))
            plt.ylabel("Latitude", fontsize=14)
            plt.xlabel("Longitude", fontsize=14)
            cc = self.TRAIN[c]
            tick_values = np.linspace(cc.min(), cc.max(), 7)
            cbar = plt.colorbar()
            cbar.ax.set_yticklabels(["$%dk" % (round(v / 1000)) for v in tick_values], fontsize=14)
            cbar.set_label(c, fontsize=16)
            plt.legend(fontsize=16)
            self.save_fig(img_name+"_"+fig_name)
            # plt.show()
        else:
            self.TRAIN.plot(kind="scatter", x=x, y=y, alpha=0.4, s=self.TRAIN[s]/snf, label="population", figsize=(10, 7),
                            c=c, cmap=plt.get_cmap("jet"), colorbar=True, sharex=False)
            plt.legend()
            if fig_name is not None:
                self.save_fig(fig_name)
            plt.show()

    def set_pipeline(self, pipeline=None):
        self.PIPELINE = pipeline
        self.train_data = self.PIPELINE.fit_transform(self.TRAIN_DATA)
        # I think this should be only transform
        self.test_data = self.PIPELINE.transform(self.TEST_DATA)

    def run_model(self, model, name=None):
        model.fit(self.train_data, self.TRAIN_TARGET)
        train_predictions = model.predict(self.train_data)
        mse = mean_squared_error(self.TRAIN_TARGET, train_predictions)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(self.TRAIN_TARGET, train_predictions)
        self.save_model(model, name)
        return rmse, mae

    def run_model_cv(self, model=None, cv=10, name=None):
        scores = cross_val_score(model, self.train_data, self.TRAIN_TARGET,
                                 scoring="neg_mean_squared_error", cv=cv)
        scores = np.sqrt(-scores)
        self.save_model(model, name)
        return scores

    def run_model_grid_search_cv(self, grid_search=None, model_name=None, confidence=0.95):
        grid_search.fit(self.train_data, self.TRAIN_TARGET)
        cvres = grid_search.cv_results_
        print('grid_search')
        print('-'*20)
        for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
            print(np.sqrt(-mean_score), params)
        df_grid_search = pd.DataFrame(grid_search.cv_results_)
        print('-'*10)
        print('df_grid_search')
        print('-'*20)
        print(df_grid_search)

        feature_importances = grid_search.best_estimator_.feature_importances_
        print('feature_importance')
        print('-'*20)
        print(feature_importances)
        # cat_encoder = cat_pipeline.named_steps["cat_encoder"] # old solution
        cat_encoder = self.PIPELINE.named_transformers_["cat"]
        cat_one_hot_attribs = list(cat_encoder.categories_[0])

        attributes = self.num_attribs + self.extra_attribs + cat_one_hot_attribs
        sorted_feature_importances = sorted(zip(feature_importances, attributes), reverse=True)
        print('sorted_feature_importance')
        print('-'*20)
        print(sorted_feature_importances)

        self.model = grid_search.best_estimator_
        self.save_model(model=self.model, name=model_name)
        rmse, confidence_interval = self.prediction_and_accuracy(confidence=confidence)
        return df_grid_search, sorted_feature_importances, rmse, confidence_interval

    def prediction_and_accuracy(self, model_name=None, confidence=0.95):
        if model_name:
            self.model = self.load_model(model_name)
        predictions = self.model.predict(self.test_data)
        mse = mean_squared_error(self.TEST_TARGET, predictions)
        rmse = np.sqrt(mse)
        print('prediction of test vs. actual final rmse')
        print('-'*40)
        print(rmse)

        # We can compute a 95% confidence interval for the test RMSE:
        squared_errors = (predictions - self.TEST_TARGET) ** 2
        m = len(squared_errors)
        confidence_interval = np.sqrt(stats.t.interval(confidence, m - 1, loc=np.mean(squared_errors),
                                                       scale=stats.sem(squared_errors)))
        print('\nconfidence Interval')
        print('-'*20)
        print(confidence_interval, '\n', '-'*10)
        # We could compute the interval manually like this:
        # tscore = stats.t.ppf((1 + confidence) / 2, df=m - 1)
        # tmargin = tscore * squared_errors.std(ddof=1) / np.sqrt(m)
        # mean = squared_errors.mean()
        # print(np.sqrt(mean - tmargin), np.sqrt(mean + tmargin))
        return rmse, confidence_interval

    def save_model(self, model, name):
        file_path = os.path.join(self.MODELS_PATH, name + ".pkl")
        joblib.dump(model, file_path)

    def load_model(self, name):
        file_path = os.path.join(self.MODELS_PATH, name + ".pkl")
        if os.path.isfile(file_path):
            model = joblib.load(file_path)
            return model
        else:
            msg = "File not exist"
            print(msg)
            return None

