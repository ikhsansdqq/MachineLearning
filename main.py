import pandas as pd


def read_csv(path):
    data = pd.read_csv(path, delimiter=';', na_values='?')
    return pd.DataFrame(data)


def normalization_process(all_data, column_target):
    for column in column_target:
        all_data[column] = (all_data[column] - all_data[column].min()) / (
                all_data[column].max() - all_data[column].min())
    return all_data


testStartID = data_train.index.stop
all_data = normalization_process(data_train,
                                 ['age', 'sex', 'height', 'weight', 'qrs_duration', 'qrs', 'QRST', 'heart_rate'])
normTrain, normTest = all_data.iloc[:testStartID], all_data.iloc[testStartID:]

data_train = read_csv('../docs/data_arrhythmia.csv')
