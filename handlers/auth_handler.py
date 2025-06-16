from aiogram import Router, F, types
from aiogram.filters.command import CommandStart
from keyboards.main_keyboard import (
    regions_keyboard, main_keyboard, get_times_keyboard, get_learn_prayer_keyboard,
)
from locales.uz import (
    select_region_message, region_selected_message, error_message, prayer_times_message, learn_prayer_intro_message, donate_alert_message
)

from aiogram.exceptions import TelegramBadRequest

from helpers.getRegionName import get_region_name_by_id
from helpers.IsNotRegistered import IsNotRegistered
from helpers.getTimes import get_prayer_times

from models.user import User
router = Router(name=__name__)

@router.callback_query(F.data == "select_region")
@router.message(IsNotRegistered())
async def start_command_handler(message):
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text=select_region_message,
        reply_markup=await regions_keyboard()
    )

@router.callback_query(F.data.startswith('region:'))
async def select_region_handler(callback: types.CallbackQuery):
    try:
        region_id = callback.data.split(":")[1]
        User.change_region(callback.from_user.id, region_id)
        region_name = get_region_name_by_id(int(region_id))
        await callback.answer(text=f"✅ Siz *{region_name}* hududini tanladingiz!")
        await callback.message.edit_text(
            text=region_selected_message.format(region_name=region_name),
            reply_markup=await get_times_keyboard()
        )
    except Exception:
        await callback.answer(text=f"Mavjud bo'lmagan region tanladingiz !", show_alert=True)
        await callback.message.edit_text(
            text=error_message,
            reply_markup=await regions_keyboard()
        )

@router.message(CommandStart())
@router.callback_query(F.data == "refresh_prayer_times")
async def send_prayer_times(target: types.Message | types.CallbackQuery, user: User):
    response = await get_prayer_times(user)
    from datetime import datetime
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    text = prayer_times_message.format(
        region_name=response["region"],
        bomdod=response["times"]["tong_saharlik"],
        quyosh=response["times"]["quyosh"],
        peshin=response["times"]["peshin"],
        asr=response["times"]["asr"],
        shom=response["times"]["shom_iftor"],
        xufton=response["times"]["hufton"],
        updated_at=now
    )

    markup = await main_keyboard()

    if isinstance(target, types.CallbackQuery):
        try:
            await target.answer(text="⏱ Namoz vaqtlari yangilandi", show_alert=False)
            await target.message.edit_text(text=text, reply_markup=markup)
        except TelegramBadRequest as e:
            if "message is not modified" not in str(e):
                raise
    else:
        await target.answer(text=text, reply_markup=markup)


@router.callback_query(F.data == "learn_prayer")
async def learn_prayer_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=learn_prayer_intro_message,
        reply_markup=await get_learn_prayer_keyboard()
    )

@router.callback_query(F.data.startswith("learn_"))
async def learn_prayer_detail_handler(callback: types.CallbackQuery):
    from locales.uz import (
        learn_bomdod_text, learn_peshin_text, learn_asr_text, learn_shom_text, learn_xufton_text
    )
    prayer_type = callback.data.split("_")[1]
    prayer_texts = {
        "bomdod": learn_bomdod_text,
        "peshin": learn_peshin_text,
        "asr": learn_asr_text,
        "shom": learn_shom_text,
        "xufton": learn_xufton_text
    }
    
    text = f"**Namoz turi:** {prayer_type.capitalize()}\n\n{prayer_texts.get(prayer_type, 'Namoz turi topilmadi.')}"
    
    await callback.message.edit_text(
        text=text,
        reply_markup=await get_learn_prayer_keyboard()
    )


@router.callback_query(F.data == "donate")
async def donate_callback(callback: types.CallbackQuery):
    await callback.answer(
        text=donate_alert_message,
        show_alert=True
    )