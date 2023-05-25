from utils.game_data import GameData
import pytesseract
from pyautogui import locate
from PIL import Image
from file_helpers import resource_path


# TODO: equipped


class LightConeStrategy:
    scan_type = 0
    nav_data = {
        "16:9": {
            "inv_tab": (0.38, 0.06),
            "row_start_top": (0.1, 0.185),
            "row_start_bottom": (0.1, 0.77),
            "scroll_start_y": 0.849,
            "scroll_end_y": 0.185,
            "offset_x": 0.075,
            "offset_y": 0.157,
            "rows": 4,
            "cols": 8
        }
    }

    def __init__(self, screenshot):
        self._lock_icon = Image.open(resource_path("./images/lock.png"))
        self._screenshot = screenshot

    def screenshot_stats(self):
        return self._screenshot.screenshot_light_cone_stats()

    async def parse(self, stats_map):
        # Get each cropped img
        name = stats_map["name"]
        level = stats_map["level"]
        superimposition = stats_map["superimposition"]
        lock = stats_map["lock"]
        equipped = stats_map["equipped"]

        # OCR
        name = pytesseract.image_to_string(
            name, config="-c tessedit_char_whitelist=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ \'abcedfghijklmnopqrstuvwxyz-\" --psm 6")
        level = pytesseract.image_to_string(
            level, config='-c tessedit_char_whitelist=0123456789/ --psm 7')
        superimposition = pytesseract.image_to_string(
            superimposition, config='-c tessedit_char_whitelist=12345 --psm 10')
        equipped = pytesseract.image_to_string(
            equipped, config='-c tessedit_char_whitelist=Equipped --psm 7')

        # Clean up
        name = name.strip()
        level = level.strip()
        superimposition = superimposition.strip()
        equipped = equipped.strip()

        # Fix OCR errors
        name, _ = GameData.get_closest_light_cone_name(name)

        # Parse level, ascension, superimposition
        try:
            level, max_level = level.split("/")
            level = int(level)
            max_level = int(max_level)
        except ValueError:
            print("Failed to parse level for ", name, level)
            level = 1
            max_level = 20

        ascension = (max(max_level, 20) - 20) // 10
        superimposition = int(superimposition)

        min_dim = min(lock.size)
        locked = self._lock_icon.resize((min_dim, min_dim))

        # Check if locked by image matching
        if locate(locked, lock, confidence=0.1):
            lock = True
        else:
            lock = False

        location = ""
        if equipped == "Equipped":
            equipped_avatar = stats_map["equipped_avatar"]

            location = GameData.get_equipped_character(
                equipped_avatar, resource_path("./images/avatars/"))

        result = {
            "name": name,
            "level": int(level),
            "ascension": int(ascension),
            "superimposition": int(superimposition),
            "location": location,
            "lock": lock
        }

        print(result)

        return result
