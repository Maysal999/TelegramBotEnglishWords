# from aiogram import Router, types,Bot
# from aiogram.filters import Command

# from filters.chat_type import ChatTypeFilter

# user_group_router = Router()


# @user_group_router.message.filter(ChatTypeFilter(["group", "supergroup"] ) )

# @user_group_router.message(Command("admin"))
# async def get_admins(message: types.Message, bot: Bot):
#     chat_id = message.chat.id
#     admins_list = await bot.get_chat_administrators(chat_id)
#     #просмотреть все данные и свойства полученных объектов
#     print(admins_list)
#     # Код ниже это генератор списка, как и этот x = [i for i in range(10)]
#     admins_list = [
#         member.user.id
#         for member in admins_list
#         if member.status == "creator" or member.status == "administrator"
#     ]
#     bot.my_admins_list = admins_list
#     if message.from_user.id in admins_list:
#         await message.delete()
#     #print(admins_list)