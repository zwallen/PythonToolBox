import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pycodebox.plotting import (
    stratified_barplot,
    stratified_violin_boxplot,
    stratified_coef_w_ci,
    stratified_volcano,
)


def test_stratified_barplot_required_params():
    np.random.seed(1234)
    df = pd.DataFrame(
        {
            'gender': pd.Categorical(
                np.random.choice(['Male', 'Female'], size=100, replace=True)
            ),
            'treatment': pd.Categorical(
                np.random.choice(['Treatment', 'Control'], size=100, replace=True)
            ),
            'case_id': np.arange(1, 100 + 1),
        }
    )
    p = stratified_barplot(df, 'gender', 'treatment', 'case_id')
    plt.close()
    assert p is not None


def test_stratified_barplot_full_params():
    np.random.seed(1234)
    df = pd.concat(
        [
            pd.DataFrame(
                {
                    'gender': pd.Categorical(
                        np.random.choice(
                            ['Male', 'Female'], size=100, replace=True, p=[0.3, 0.7]
                        )
                    ),
                    'treatment': pd.Categorical(['Treatment'] * 100),
                    'case_id': np.arange(1, 100 + 1),
                }
            ),
            pd.DataFrame(
                {
                    'gender': pd.Categorical(
                        np.random.choice(
                            ['Male', 'Female'], size=100, replace=True, p=[0.5, 0.5]
                        )
                    ),
                    'treatment': pd.Categorical(['Control'] * 100),
                    'case_id': np.arange(100 + 1, 200 + 1),
                }
            ),
        ]
    )
    p = stratified_barplot(
        df,
        'gender',
        'treatment',
        'case_id',
        fill_color=['grey', 'black'],
        xlab='Treatment group',
        alpha=0.05,
    )
    plt.close()
    assert p is not None


def test_stratified_violin_boxplot_required_params():
    np.random.seed(1234)
    df = pd.DataFrame(
        {
            'score': pd.concat(
                [
                    pd.Series(np.random.normal(5, 5, size=100)),
                    pd.Series(np.random.normal(10, 5, size=100)),
                    pd.Series(np.random.normal(20, 10, size=100)),
                    pd.Series(np.random.normal(15, 7, size=100)),
                    pd.Series(np.random.normal(12, 20, size=100)),
                ]
            ),
            'treatment': pd.Categorical(
                ['Control'] * 100
                + ['TreatmentA'] * 100
                + ['TreatmentB'] * 100
                + ['TreatmentC'] * 100
                + ['TreatmentD'] * 100
            ),
        }
    )
    p = stratified_violin_boxplot(df, 'score', 'treatment')
    plt.close()
    assert p is not None


def test_stratified_violin_boxplot_full_params():
    np.random.seed(1234)
    df = pd.DataFrame(
        {
            'survival': pd.concat(
                [
                    pd.Series(np.random.normal(100, 30, size=100)),
                    pd.Series(np.random.normal(50, 20, size=100)),
                    pd.Series(np.random.normal(20, 5, size=100)),
                ]
            ),
            'treatment': pd.Categorical(
                ['TreatmentA'] * 100 + ['TreatmentB'] * 100 + ['Control'] * 100
            ),
        }
    )
    p = stratified_violin_boxplot(
        df,
        'survival',
        'treatment',
        ylab='Survival (months)',
        xlab='Treatment group',
        alpha=0.05,
    )
    plt.close()
    assert p is not None


def test_stratified_coef_w_ci_required_params():
    df = pd.DataFrame(
        {
            'genes': pd.Categorical(
                ['Gene1'] * 2
                + ['Gene2'] * 2
                + ['Gene3'] * 2
                + ['Gene4'] * 2
                + ['Gene5'] * 2
            ),
            'treatment': pd.Categorical(['Treatment', 'Control'] * 5),
            'coef': [0.5, -0.3, 0.2, -0.1, 0.4, -0.2, 0.3, -0.4, 0.1, -0.5],
            'lower': [0.2, -0.5, 0.1, -0.3, 0.1, -0.4, 0.2, -0.6, 0.05, -0.7],
            'upper': [0.8, -0.1, 0.3, 0.1, 0.7, 0.0, 0.4, -0.2, 0.15, -0.3],
            'pvalue': [0.01, 0.05, 0.03, 0.07, 0.02, 0.04, 0.0012, 0.08, 0.09, 0.10],
        }
    )
    p = stratified_coef_w_ci(df, 'genes', 'treatment', 'coef', 'lower', 'upper')
    plt.close()
    assert p is not None


def test_stratified_coef_w_ci_full_params():
    df = pd.DataFrame(
        {
            'genes': pd.Categorical(
                ['Gene1'] * 2
                + ['Gene2'] * 2
                + ['Gene3'] * 2
                + ['Gene4'] * 2
                + ['Gene5'] * 2
            ),
            'treatment': pd.Categorical(['Treatment', 'Control'] * 5),
            'coef': [0.5, -0.3, 0.2, -0.1, 0.4, -0.2, 0.3, -0.4, 0.1, -0.5],
            'lower': [0.2, -0.5, 0.1, -0.3, 0.1, -0.4, 0.2, -0.6, 0.05, -0.7],
            'upper': [0.8, -0.1, 0.3, 0.1, 0.7, 0.0, 0.4, -0.2, 0.15, -0.3],
            'pvalue': [0.01, 0.05, 0.03, 0.07, 0.02, 0.04, 0.0012, 0.08, 0.09, 0.10],
        }
    )
    p = stratified_coef_w_ci(
        df,
        'genes',
        'treatment',
        'coef',
        'lower',
        'upper',
        pvalue='pvalue',
        fill_color=['grey', 'black'],
        xlab='Effect Size',
    )
    plt.close()
    assert p is not None


def test_stratified_volcano_required_params():
    np.random.seed(1234)
    df = pd.DataFrame(
        {
            'genes': pd.Categorical([f'Gene{i}' for i in np.arange(1, 301)]),
            'treatment': pd.Categorical(['TreatmentA', 'TreatmentB', 'Control'] * 100),
            'coef': np.random.normal(
                0, 1.5, 300
            ),  # Coefficients centered around 0 with some spread
            'pvalue': np.random.beta(
                0.5, 2, 300
            ),  # P-values skewed toward smaller values (more realistic)
        }
    )

    # Add some clearly significant results for testing
    # Make some genes highly significant in different treatments
    df.loc[df.index < 10, 'pvalue'] = np.random.uniform(
        0.001, 0.01, 10
    )  # Very significant
    df.loc[(df.index >= 10) & (df.index < 20), 'pvalue'] = np.random.uniform(
        0.01, 0.05, 10
    )  # Significant
    df.loc[df.index < 10, 'coef'] = np.random.uniform(
        2, 4, 10
    )  # Strong positive effects
    df.loc[(df.index >= 10) & (df.index < 20), 'coef'] = np.random.uniform(
        -3, -1, 10
    )  # Strong negative effects

    p = stratified_volcano(df, 'genes', 'treatment', 'coef', 'pvalue')
    plt.close()
    assert p is not None


def test_stratified_volcano_full_params():
    np.random.seed(42)
    df = pd.DataFrame(
        {
            'genes': pd.Categorical([f'Gene{i}' for i in np.arange(1, 301)]),
            'treatment': pd.Categorical(['TreatmentA', 'TreatmentB', 'Control'] * 100),
            'coef': np.random.normal(
                0, 1.5, 300
            ),  # Coefficients centered around 0 with some spread
            'pvalue': np.random.beta(
                0.5, 2, 300
            ),  # P-values skewed toward smaller values (more realistic)
        }
    )

    # Add some clearly significant results for testing
    # Make some genes highly significant in different treatments
    df.loc[df.index < 10, 'pvalue'] = np.random.uniform(
        0.001, 0.01, 10
    )  # Very significant
    df.loc[(df.index >= 10) & (df.index < 20), 'pvalue'] = np.random.uniform(
        0.01, 0.05, 10
    )  # Significant
    df.loc[df.index < 10, 'coef'] = np.random.uniform(
        2, 4, 10
    )  # Strong positive effects
    df.loc[(df.index >= 10) & (df.index < 20), 'coef'] = np.random.uniform(
        -3, -1, 10
    )  # Strong negative effects

    p = stratified_volcano(
        df,
        'genes',
        'treatment',
        'coef',
        'pvalue',
        pthresh=0.05,
        top_n=5,
        fill_color=['grey', 'blue', 'red'],
        xlab='Mean expression change',
    )
    plt.close()
    assert p is not None
