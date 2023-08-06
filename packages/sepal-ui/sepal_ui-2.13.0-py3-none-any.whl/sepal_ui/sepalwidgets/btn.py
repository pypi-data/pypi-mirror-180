import warnings
from pathlib import Path

import ipyvuetify as v
from deprecated.sphinx import deprecated
from traitlets import Unicode, observe

from sepal_ui.scripts import utils as su
from sepal_ui.sepalwidgets.sepalwidget import SepalWidget

__all__ = ["Btn", "DownloadBtn"]


class Btn(v.Btn, SepalWidget):
    """
    Custom process Btn filled with the provided text.
    the color will be defaulted to 'primary' and can be changed afterward according to your need

    Args:
        msg (str, optional): the text to display in the btn
        gliph (str, optional): the full name of any mdi/fa icon
        text (str, optional): the text to display in the btn
        icon (str, optional): the full name of any mdi/fa icon
        kwargs (dict, optional): any parameters from v.Btn. if set, 'children' will be overwritten.

    .. deprecated:: 2.13
        ``text`` and ``icon`` will be replaced by ``msg`` and ``gliph`` to avoid duplicating ipyvuetify trait.

    .. deprecated:: 2.14
        Btn is not using a default ``msg`` anymor`.
    """

    v_icon = None
    "v.Icon: the icon in the btn"

    gliph = Unicode("").tag(sync=True)
    "traitlet.Unicode: the name of the icon"

    msg = Unicode("").tag(sync=True)
    "traitlet.Unicode: the text of the btn"

    def __init__(self, msg="", gliph="", **kwargs):

        # deprecation in 2.13 of text and icon
        # as they already exist in the ipyvuetify Btn traits (as booleans)
        if "text" in kwargs:
            if isinstance(kwargs["text"], str):
                msg = kwargs.pop("text")
                warnings.warn(
                    '"text" is deprecated, please use "msg" instead', DeprecationWarning
                )
        if "icon" in kwargs:
            if isinstance(kwargs["icon"], str):
                gliph = kwargs.pop("icon")
                warnings.warn(
                    '"icon" is deprecated, please use "gliph" instead',
                    DeprecationWarning,
                )

        # create the default v_icon
        self.v_icon = v.Icon(children=[""])

        # set the default parameters
        kwargs["color"] = kwargs.pop("color", "primary")
        kwargs["children"] = [self.v_icon, self.msg]

        # call the constructor
        super().__init__(**kwargs)

        self.gliph = gliph
        self.msg = msg

    @observe("gliph")
    def _set_gliph(self, change):
        """
        Set a new icon. If the icon is set to "", then it's hidden
        """
        new_gliph = change["new"]
        self.v_icon.children = [new_gliph]

        # hide the component to avoid the right padding
        if not new_gliph:
            su.hide_component(self.v_icon)
        else:
            su.show_component(self.v_icon)

        return self

    @observe("msg")
    def _set_text(self, change):
        """
        Set the text of the btn
        """

        self.v_icon.left = bool(change["new"])
        self.children = [self.v_icon, change["new"]]

        return self

    @deprecated(version="2.14", reason="Replace by the private _set_gliph")
    def set_icon(self, icon=""):
        """
        set a new icon. If the icon is set to "", then it's hidden.

        Args:
            icon (str, optional): the full name of a mdi/fa icon

        Return:
            self
        """
        self.gliph = icon
        return self

    def toggle_loading(self):
        """
        Jump between two states : disabled and loading - enabled and not loading

        Return:
            self
        """
        self.loading = not self.loading
        self.disabled = self.loading

        return self


class DownloadBtn(v.Btn, SepalWidget):
    """
    Custom download Btn filled with the provided text.
    the download icon is automatically embeded and green.
    The btn only accepts absolute links. if non is provided then the btn stays disabled

    Args:
        text (str): the message inside the btn
        path (str|pathlib.Path, optional): the absoluteor relative path to a downloadable content
        args (dict, optional): any parameter from a v.Btn. if set, 'children' and 'target' will be overwritten.
    """

    def __init__(self, text, path="#", **kwargs):

        # create a download icon
        v_icon = v.Icon(left=True, children=["fa-solid fa-download"])

        # set default parameters
        kwargs["class_"] = kwargs.pop("class_", "ma-2")
        kwargs["xs5"] = kwargs.pop("xs5", True)
        kwargs["color"] = kwargs.pop("color", "success")
        kwargs["children"] = [v_icon, text]
        kwargs["target"] = "_blank"
        kwargs["attributes"] = {"download": None}

        # call the constructor
        super().__init__(**kwargs)

        # create the URL
        self.set_url(path)

    def set_url(self, path="#"):
        """
        Set the URL of the download btn. and unable it.
        If nothing is provided the btn is disabled

        Args:
            path (str|pathlib.Path): the absolute path to a downloadable content

        Return:
            self
        """

        # set the url
        url = su.create_download_link(path)
        self.href = url

        # unable or disable the btn
        self.disabled = str(path) == "#"

        # set the download attribute
        name = None if str(path) == "#" else Path(path).name
        self.attributes = {"download": name}

        return self
