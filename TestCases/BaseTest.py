import pytest


@pytest.mark.usefixtures("log_on_failure", "get_browser")       #"handleConsentPopup",
class BaseTest:
    pass
