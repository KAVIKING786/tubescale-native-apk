[app]
title = TubeScale AI
package.name = tubescale
package.domain = com.tubescale.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,yt-dlp,requests,urllib3,certifi
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
