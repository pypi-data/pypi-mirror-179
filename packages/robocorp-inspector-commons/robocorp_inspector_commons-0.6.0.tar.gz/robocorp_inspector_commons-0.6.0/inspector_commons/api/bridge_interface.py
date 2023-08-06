from inspector_commons.bridge.bridge_browser import BrowserBridge
from inspector_commons.config import Config
from inspector_commons.context import Context
from inspector_commons.utils import IS_WINDOWS


class BridgeConnector(BrowserBridge):
    def __init__(self, logger, *args, **kwargs):
        config = Config()
        config.set("remote", None)
        config.set("debug", False)
        context = Context(logger, config)
        super().__init__(context, *args, **kwargs)


if IS_WINDOWS:
    from inspector_commons.bridge.bridge_windows import WindowsBridge

    class WindowsBridgeConnector(WindowsBridge):
        def __init__(self, logger, *args, **kwargs):
            config = Config()
            config.set("remote", None)
            config.set("debug", False)
            context = Context(logger, config)
            super().__init__(context, *args, **kwargs)
