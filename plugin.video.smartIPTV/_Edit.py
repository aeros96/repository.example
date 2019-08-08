import xbmcaddon
import base64

Decode = base64.decodestring
MainBase = base64.b64decode ('aHR0cHM6Ly9hZXJvczk2LjAwMHdlYmhvc3RhcHAuY29tL2J1aWxkL3VwbG9hZHovc21hcnRuZW1haW4ueG1s')
addon = xbmcaddon.Addon('plugin.video.smartIPTV')