# Customized buildozer.spec for MP3 LED Player
[app]
title = MP3 LED Player
package.name = mp3ledplayer
package.domain = com.nxtech

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,ogg,mp3,json,atlas
version = 0.1

requirements = python3,kivy==2.3.0,kivymd,pygame,pillow

orientation = portrait
fullscreen = 1

#icon.filename = assets/icon.png
#presplash.filename = assets/presplash.png

android.api = 34
android.minapi = 24
android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_AUDIO
android.allow_backup = True

android.release_artifact = apk
android.debug_artifact = apk
android.logcat_filters = *:S python:D

#android.features = android.hardware.usb.host

osx.kivy_version = 2.3.0
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2
ios.codesign.allowed = false

[buildozer]
log_level = 2
warn_on_root = 1

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# # The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.

# The remaining Buildozer options use their default values.
