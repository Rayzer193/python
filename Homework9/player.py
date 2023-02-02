from aiogram import types
import game
import bot
import text


async def player_turn(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f'{name}, твой ход! Сколько конфет возьмешь?')


async def player_game(message: types.Message, take: str, name: str):
    if take.isdigit():
        take = int(take)
        if (game.get_total() - take) < 0:
            await message.answer(f'{name}, хочет взять - {take} {text.declension_sweets(take)[0]},'
                                 f' но на столе всего {game.get_total()}.\n'
                                 f' необходимо взять от 1 до {game.get_total()} конфет')
        elif take <= 0 or take > 28:
            await message.answer(f'{name}, необходимо взять от 1 до 28 кофет')
        elif 1 <= take <= 28:
            game.take_sweets(take)
            if await game.check_win(message, 'player', take):
                return
            else:
                await message.answer(f'{name} берет {take} {text.declension_sweets(take)[0]}.'
                                     f'\nОсталось {game.get_total()} '
                                     f'{text.declension_sweets(game.get_total())[1]}. Ход бота')
                await bot.bot_turn(message)
    else:
        await message.answer(f'Вводи число')
