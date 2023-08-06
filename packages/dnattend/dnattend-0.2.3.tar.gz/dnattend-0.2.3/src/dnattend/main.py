#!/usr/bin/env python3

import os
import sys
import json
import joblib
import hashlib
import logging
import tempfile
import numpy as np
import pandas as pd
from . import utils, simulate, test, train


logger = logging.getLogger(__name__)


def train_cli(config: str):
    """ Train a model """
    config = utils.Config(config).config
    # Set global seed
    np.random.seed(config['seed'])
    # Read data and map DNA target label to 1
    data = pd.read_csv(config['input'])
    assert len(data[config['target']].unique()) == 2
    assert config['DNAclass'] in data[config['target']].unique()
    data[config['target']] = data[config['target']].apply(
        lambda x: 1 if x == config['DNAclass'] else 0)
    data = train.splitData(data, **config)
    # Train model
    models = train.trainModel(data, **config)
    # Write trained logistic and catboost models and parameter definitions
    for name, model in models.items():
        model_out = f'{config["out"]}/{name}-trained.pkl'
        params_out = f'{config["out"]}/{name}-params.json'
        print(f'Writing trained {name} model to: {model_out}', file=sys.stderr)
        joblib.dump(model['model'], model_out)
        print(f'Writing tuned {name} parameters '
              f'to: {params_out}', file=sys.stderr)
        with open(params_out, 'w') as fh:
            json.dump(model['params'], fh)
    # Write split data
    for name, df in data.items():
        df.to_pickle(f'{config["out"]}/{name}.pkl')


def test_cli(config: str):
    """ Test a pre-trained model. """
    config = utils.Config(config).config
    np.random.seed(config['seed']) # Set global seed
    data = _readData(config)
    models = {'catboost': {}, 'logistic': {}}
    for name in models:
        models[name]['model'] = joblib.load(
            f'{config["out"]}/{name}-trained.pkl')
        with open(f'{config["out"]}/{name}-params.json') as fh:
            models[name]['params'] = json.load(fh)

    importance_out = f'{config["out"]}/featureImportances.png'
    featureImportances = test.getFeatureImportance(models['catboost']['model'])
    print(f'Writing feature importances to: {importance_out}', file=sys.stderr)
    fig = featureImportances.plot.barh()
    fig.figure.savefig(importance_out, dpi=300)

    roc_out = f'{config["out"]}/ROCcurve.png'
    print(f'Writing ROC curve to: {roc_out}', file=sys.stderr)
    fig, ax = test.plotROC(models, data)
    fig.figure.savefig(roc_out, dpi=300)

    pr_out = f'{config["out"]}/PRcurve.png'
    print(f'Writing PR curve to: {pr_out}', file=sys.stderr)
    fig, ax = test.plotPrecisionRecall(models, data)
    fig.figure.savefig(pr_out, dpi=300)

    calibation_out = f'{config["out"]}/CalibrationCurve.png'
    print(f'Writing Calibration curve to: {calibation_out}', file=sys.stderr)
    fig, ax = test.plotCalibrationCurve(models, data, strategy='quantile')
    fig.figure.savefig(calibation_out, dpi=300)

    for name in models:
        report = test.evaluate(models[name]['model'], data)
        report_out = f'{config["out"]}/{name}-report.json'
        print(f'Writing {name} model report to: {report_out}', file=sys.stderr)
        with open(report_out, 'w') as fh:
            json.dump(report, fh)


def retrain_cli(config: str):
    """ Re-train model on full dataset """
    config = utils.Config(config).config
    np.random.seed(config['seed']) # Set global seed
    data = _readData(config)
    modelType = config['finalModel']
    if modelType not in ['catboost', 'logistic']:
        if modelType:
            logging.error(
                f'Invalid configuration for "finalModel" - {finalModel}')
        logging.error(
            'Please set "finalModel" to either "catboost" or "logistic"')
    model = joblib.load(
        f'{config["out"]}/{modelType}-trained.pkl')
    model = train.refitData(model, data)
    final_out = f'{config["out"]}/{modelType}-final.pkl'
    print(f'Writing fully trained {modelType} model '
          f'to: {final_out}', file=sys.stderr)
    joblib.dump(model, final_out)


def predict_cli(
        data, model, verify: bool = False, sep: str = ',', out=sys.stdout):
    data = pd.read_csv(data, sep=sep)
    model = joblib.load(model)
    data[['Attend_prob', 'DNA_prob', 'Prediction']] = (
        test.predict(model, data))
    data['Prediction'] = data['Prediction'].map({1: 'DNA', 0: 'Attend'})
    if out is not None:
        data.to_csv(out)
    if verify:
        if verifyHash(data):
            print('Success: output matches expected hash.', file=sys.stderr)
            return 0
        else:
            print('Error: output does NOT match expected hash', file=sys.stderr)
            return 1


def verifyHash(df: str, readSize: int = 4096):
    tf = tempfile.NamedTemporaryFile(delete=False)
    df.to_csv(tf.name, float_format='%.3f')
    sha256Hash = hashlib.sha256()
    with open(tf.name, 'rb') as f:
        data = f.read(readSize)
        while data:
            sha256Hash.update(data)
            data = f.read(readSize)
    hash = sha256Hash.hexdigest()
    return hash == ('801cb98641256aaf8c3a57c7af87da80'
                    'bd2f92088a8c9dcd4609c06e03395484')


def simulate_cli(
        out: str, config: str, size: int = 50_000,
        noise: float = 0.2, seed: int = 42):
    """ Randomly generate some example data """
    assert seed > 0
    assert size > 0
    assert noise >= 0
    # Randomly generate some artificial attendance data
    df = simulate.generateData(size, seed, noise)
    print(f'Writing simulated data to: {out}', file=sys.stderr)
    df.to_csv(out, index=False)
    print(f'Writing example configuration to: {config}', file=sys.stderr)
    simulate.writeConfig(config)


def _readData(config):
    """ Read pre-split data """
    data = {}
    for name in ['X_train', 'y_train', 'X_test', 'y_test', 'X_val', 'y_val']:
        data[name] = pd.read_pickle(f'{config["out"]}/{name}.pkl')
    return data
