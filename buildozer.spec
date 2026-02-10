[app]

title = 射击游戏
package.name = shootergame
package.domain = org.test

source.dir = .
source.include_ext.dirs = 

version = 1.0.0
version.regex = __version__ = ['"](.+)['"]
version.filename = %(source.dir)s/main.py

requirements = python3,kivy

orientation = portrait

fullscreen = 0

presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png

[buildozer]

log_level = 2

warn_on_root = 1

[app]

android.permissions = CAMERA

android.api = 33
android.ndk = 25b
android.sdk = 33
android.minapi = 21

[android]

android.archs = arm64-v8a,armeabi-v7a

android.accept_sdk_license_terms = True

[android]

debug = True

[ios]

[buildozer]

[buildozer]
