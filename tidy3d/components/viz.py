""" utilities for plotting """

import matplotlib.pylab as plt


def make_ax():
    """makes an empty `ax`"""
    _, ax = plt.subplots(1, 1, tight_layout=True)
    return ax


def add_ax_if_none(plot):
    """decorates `plot(ax=None)` function,
    if ax=None, creates ax and feeds it to `plot`.
    """

    def _plot(*args, **kwargs):
        """new `plot()` function with `ax=ax`"""
        if kwargs.get("ax") is None:
            ax = make_ax()
            kwargs["ax"] = ax
        return plot(*args, **kwargs)

    return _plot


def make_aspect_equal(plot):
    """decorates `ax = plot()` function,
    sets equal aspect ratio for return ax
    """

    def _plot(*args, **kwargs):
        """calls `ax = plot()` and sets apect ratio of `ax` to "equal"`"""
        ax = plot(*args, **kwargs)
        ax.set_aspect("equal")
        return ax

    return _plot


class VizParams:
    """contains general settings for plots"""

    # colormaps: https://matplotlib.org/stable/tutorials/colors/colormaps.html
    qualatative_cmap = plt.cm.Set2  # qualatative colormap