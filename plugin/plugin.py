from __future__ import absolute_import

from Components.SystemInfo import SystemInfo
from Plugins.Plugin import PluginDescriptor


def autostart(reason, **kwargs):
	if SystemInfo.get("UseServiceHisilicon", False):
		from . import servicehisilicon


def Plugins(**kwargs):
	return [
		PluginDescriptor(where=PluginDescriptor.WHERE_AUTOSTART, needsRestart=True, fnc=autostart)
	]