import traceback

from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Zaid import CMD_HELP, app
from Zaid.helper.data import Data
from Zaid.helper.inline import cb_wrapper, paginate_help
from Zaid import ids as users


# ==========================
# CALLBACK HANDLER (FIXED)
# ==========================
@app.on_callback_query()
async def _callbacks(_, callback_query: CallbackQuery):
    query = callback_query.data.lower()

    if query == "helper":
        buttons = paginate_help(0, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            Data.text_help_menu,
            reply_markup=InlineKeyboardMarkup(buttons),
        )

    elif query == "close":
        await app.edit_inline_text(
            callback_query.inline_message_id,
            "**— CLOSED**"
        )

    elif query == "close_help":
        if callback_query.from_user.id not in users:
            return
        await app.edit_inline_text(
            callback_query.inline_message_id,
            "**— CLOSED MENU HELP**",
            reply_markup=InlineKeyboardMarkup(Data.reopen),
        )

    elif query == "closed":
        try:
            await callback_query.message.delete()
        except Exception:
            pass
        try:
            await callback_query.message.reply_to_message.delete()
        except Exception:
            pass

    elif query == "make_basic_button":
        try:
            bttn = paginate_help(0, CMD_HELP, "helpme")
            await app.edit_inline_text(
                callback_query.inline_message_id,
                Data.text_help_menu,
                reply_markup=InlineKeyboardMarkup(bttn),
            )
        except Exception:
            print(traceback.format_exc())


# ==========================
# MODULE HELP CALLBACKS
# ==========================
@app.on_callback_query(filters.regex("ub_modul_(.*)"))
@cb_wrapper
async def on_plug_in_cb(_, callback_query: CallbackQuery):
    modul_name = callback_query.matches[0].group(1)
    commands: dict = CMD_HELP[modul_name]

    text = f"──「 **Help For {modul_name.upper()}** 」──\n\n"
    for cmd in commands:
        text += f"  • **Command:** `.{cmd}`\n  • **Function:** `{commands[cmd]}`\n\n"

    text += "© @TheSupportChat"

    buttons = [[InlineKeyboardButton("Return", callback_data="reopen")]]

    await app.edit_inline_text(
        callback_query.inline_message_id,
        text,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("reopen"))
@cb_wrapper
async def reopen_in_cb(_, callback_query: CallbackQuery):
    buttons = paginate_help(0, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("helpme_prev\((.+?)\)"))
@cb_wrapper
async def on_plug_prev_in_cb(_, callback_query: CallbackQuery):
    page = int(callback_query.matches[0].group(1))
    buttons = paginate_help(page - 1, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("helpme_next\((.+?)\)"))
@cb_wrapper
async def on_plug_next_in_cb(_, callback_query: CallbackQuery):
    page = int(callback_query.matches[0].group(1))
    buttons = paginate_help(page + 1, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
