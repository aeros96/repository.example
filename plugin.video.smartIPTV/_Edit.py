import xbmcaddon
import base64

Decode = base64.decodestring
MainBase = base64.b64decode ('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2Flcm9zOTYvc21hcnRpcHR2L21hc3Rlci9zbWFydG5lbWFpbi54bWw=')
addon = xbmcaddon.Addon('plugin.video.smartIPTV')
