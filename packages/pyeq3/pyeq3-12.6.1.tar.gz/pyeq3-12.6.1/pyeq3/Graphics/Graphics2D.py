import pyeq3
import numpy as np
from scipy import stats


def ModelScatterConfidenceGraph(model, axes):
    model.CalculateModelErrors(
        model.solvedCoefficients, model.dataCache.allDataCacheDictionary
    )
    model.CalculateCoefficientAndFitStatistics()
    y_data = model.dataCache.allDataCacheDictionary["DependentData"]
    x_data = model.dataCache.allDataCacheDictionary["IndependentData"][0]

    # first the raw data as a scatter plot
    axes.plot(x_data, y_data, "D")

    # create data for the fitted model plot
    xModel = np.linspace(min(x_data), max(x_data), 1001)

    tempcache = model.dataCache  # store the data cache
    model.dataCache = pyeq3.dataCache()
    model.dataCache.allDataCacheDictionary["IndependentData"] = np.array(
        [xModel, xModel]
    )
    model.dataCache.FindOrCreateAllDataCache(model)
    yModel = model.CalculateModelPredictions(
        model.solvedCoefficients, model.dataCache.allDataCacheDictionary
    )
    model.dataCache = tempcache  # restore the original data cache

    # now the model as a line plot
    axes.plot(xModel, yModel)

    # now calculate confidence intervals
    # http://support.sas.com/documentation/cdl/en/statug/63347/HTML/default/viewer.htm#statug_nlin_sect026.htm
    # http://www.staff.ncl.ac.uk/tom.holderness/software/pythonlinearfit
    mean_x = np.mean(x_data)
    n = model.nobs

    # (1.0 - (a/2)) is used for two-sided t-test critical value, here a = 0.05
    t_value = stats.t.ppf(0.975, model.df_e)

    confs = t_value * np.sqrt(
        (model.sumOfSquaredErrors / model.df_e)
        * (
            1.0 / n
            + (
                np.power((xModel - mean_x), 2.0)
                / ((np.sum(np.power(x_data, 2.0))) - n * (np.power(mean_x, 2.0)))
            )
        )
    )

    # get lower and upper confidence limits based on predicted y
    # and confidence intervals
    upper = yModel + abs(confs)
    lower = yModel - abs(confs)

    # mask off any numbers outside the existing plot limits
    booleanMask = yModel > axes.get_ylim()[0]
    booleanMask &= yModel < axes.get_ylim()[1]

    # color scheme improves visibility on black background lines or points
    axes.plot(xModel[booleanMask], lower[booleanMask], linestyle="solid", color="white")
    axes.plot(xModel[booleanMask], upper[booleanMask], linestyle="solid", color="white")
    axes.plot(xModel[booleanMask], lower[booleanMask], linestyle="dashed", color="blue")
    axes.plot(xModel[booleanMask], upper[booleanMask], linestyle="dashed", color="blue")

    axes.set_title("Model With 95% Confidence Intervals")  # add a title
    axes.set_xlabel("X Data")  # X axis data label
    axes.set_ylabel("Y Data")  # Y axis data label
