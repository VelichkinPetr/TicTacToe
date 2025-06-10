import sys
import os



def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)



IMAGE_EASY: str = resource_path("images/easy.png")
IMAGE_MEDIUM: str = resource_path("images/medium.png")
IMAGE_HARD: str = resource_path("images/hard.png")
IMAGE_RECYCLE_FULL: str = resource_path("images/full.png")
IMAGE_RECYCLE_EMPTY: str = resource_path("images/empty.png")

THEME_FILE: str = resource_path('theme/config.json')

STATS_FILE: str = resource_path('stats/stats.json')

