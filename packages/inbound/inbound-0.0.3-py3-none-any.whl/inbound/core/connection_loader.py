import importlib
from typing import List


class PluginInterface:
    """Represents a plugin interface. A plugin must provide a register function."""

    @staticmethod
    def register() -> None:
        """Register the plugin."""


def import_module(name: str) -> PluginInterface:
    """Imports a module given a name."""
    return importlib.import_module(name, package=__name__)  # type: ignore


def load_plugins(plugins: List[str]) -> None:
    """Loads the plugins defined in the plugins list."""
    loadedPlugins: List[str] = []
    for plugin_name in plugins:
        if not plugin_name in loadedPlugins:
            plugin = import_module(f"...plugins.connections.{plugin_name}")
            plugin.register()
            loadedPlugins.append(plugin_name)
