from setuptools import setup

APP = ['main.py'] # если ваш файл запускается не как main.py — поменяйте имя здесь DATA_FILES = ['settings.json', 'downloads'] # если у вас нет downloads — уберите 'downloads' OPTIONS = { 'argv_emulation': False, 'packages': ['telethon', 'PIL', 'requests', 'cloudinary', 'woocommerce'], 'includes': ['tkinter'], }

setup( app=APP, data_files=DATA_FILES, options={'py2app': OPTIONS}, setup_requires=['py2app'], )
