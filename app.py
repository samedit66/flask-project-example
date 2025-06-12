from flask import Flask

from src.database import Database


app = Flask(
    __name__,
    static_folder="src/static", # Задаем static-папку
    template_folder="src/template", # Задаем папку для шаблонов (hmtl-файлов)
)

# Весь остальной код...
