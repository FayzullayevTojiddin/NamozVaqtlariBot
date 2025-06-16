import json
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pathlib import Path

async def regions_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    json_path = Path("models/regions.json")

    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)
        regions: list[str] = data.get("regions", [])

    for index, name in enumerate(regions, start=1):
        keyboard.button(text=name, callback_data=f"region:{index}")

    keyboard.adjust(2)
    return keyboard.as_markup()

async def main_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="🔁 Namoz vaqtlarini yangilash", callback_data="refresh_prayer_times")
    keyboard.button(text="📖 Namoz o‘qishni o‘rganish", callback_data="learn_prayer")
    keyboard.button(text="🌍 Hududni o‘zgartirish", callback_data="select_region")
    keyboard.button(text="💝 Donat qilish", callback_data="donate")
    keyboard.adjust(1)
    return keyboard.as_markup()

async def get_times_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="🔁 Namoz vaqtlarini ko'rish", callback_data="refresh_prayer_times")
    keyboard.button(text="📖 Namoz o‘qishni o‘rganish", callback_data="learn_prayer")
    keyboard.button(text="💝 Donat qilish", callback_data="donate")
    keyboard.adjust(1)
    return keyboard.as_markup()

async def get_learn_prayer_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    buttons = {
        "learn_bomdod": "📿 Bomdod",
        "learn_peshin": "☀️ Peshin",
        "learn_asr": "🌇 Asr",
        "learn_shom": "🌙 Shom",
        "learn_xufton": "🕯 Xufton",
        "refresh_prayer_times": "⬅️ Asosiy menyu"
    }
    for callback_data, text in buttons.items():
        keyboard.button(text=text, callback_data=callback_data)
    keyboard.adjust(1)
    return keyboard.as_markup()