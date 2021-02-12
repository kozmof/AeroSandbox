from aerosandbox.modeling.fitting import fit_model
import pytest
import aerosandbox.numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def test_fit_model_weighting():
    x = np.linspace(0, 10)
    y = np.sin(x)

    fm = fit_model(
        model=lambda x, p: p["m"] * x + p["b"],
        x_data=x,
        y_data=y,
        parameter_guesses={
            "m": 0,
            "b": 0,
        },
        weights=None
    )  # Fit a model with no weighting

    assert fm(10) != pytest.approx(5, abs=1) # Doesn't give a high value at x = 10

    fm = fit_model(
        model=lambda x, p: p["m"] * x + p["b"],
        x_data=x,
        y_data=y,
        parameter_guesses={
            "m": 0,
            "b": 0,
        },
        weights=(x > 0) & (x < 2)
    )  # Fit a model with weighting

    assert fm(10) == pytest.approx(5, abs=1) # Gives a high value at x = 10

    fm.plot_fit()


if __name__ == '__main__':
    test_fit_model_weighting()
