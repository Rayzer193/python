
from aiogram import types
import game
import random
import player
import time
import text



async def bot_turn(message: types.Message):
    await message.answer('Бот думает')
    time.sleep(1)
    total = game.get_total()
    if game.level == 'сильный':
        if total <= 28:
            take = total
        elif total % 29:
            take = total % 29
        else:
            take = random.randint(1, 28)
    else:
        if total <= 28:
            take = total
        else:
            take = random.randint(1, 28)
    await message.answer(f'Бот берет {take} {text.declension_sweets(take)[0]}. '
                         f'Осталось {game.take_sweets(take)} '
                         f'{text.declension_sweets(game.get_total())[1]}.')

    if await game.check_win(message, 'bot', take):
        return
    await player.player_turn(message)
