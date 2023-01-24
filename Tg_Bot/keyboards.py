from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config as cfg
from DB import SessionDb, FlowDb, ProductDb

class Keyboards:
    butt_on_page = 20
    products = [i[0] for i in SessionDb.query(ProductDb.product_name)]
    flows =  [i[0] for i in SessionDb.query(FlowDb.flow_exp)]
    def __init__(self):
        self.btn_back_to_menu = InlineKeyboardButton(
            text='↩️Главное меню',
            callback_data='back_to_menu'
        )

    def single_back(self):
        markup = InlineKeyboardMarkup(row_width=1)
        markup.insert(self.btn_back_to_menu)
        return markup

    def main_menu(self, ):
        markup = InlineKeyboardMarkup(row_width=1)
        markup.insert(InlineKeyboardButton(text='Приход',callback_data='coming'))
        markup.insert(InlineKeyboardButton(text='Расход',callback_data='expenditure'))
        return markup

    def all_products(self, page=0):
        markup = InlineKeyboardMarkup(row_width=3)
        start = page * 20
        end = start+self.butt_on_page
        select_products = self.products[start:end]
        next_page = self.products[end:end+self.butt_on_page]
        for product in select_products:
            markup.insert(InlineKeyboardButton(text=product, callback_data=f'select_product_{product}'))
        markup.row(InlineKeyboardButton(
            text='------------------------------------------', callback_data='.....'))
        footer = []
        if page != 0:
            footer.append(InlineKeyboardButton(
                text='⬅️Предыдущая страница', callback_data=f'replace_page_{page-1}'))
        footer.append(InlineKeyboardButton(
            text=f'Стр. №{page+1}', callback_data=f'{page}'))
        if len(next_page) > 0:
            footer.append(InlineKeyboardButton(
                text='➡️Следующая страница', callback_data=f'replace_page_{page+1}'))
        markup.row(*footer)
        markup.row(self.btn_back_to_menu)
        return markup

    def all_flows(self, product:str, page=0):
        markup = InlineKeyboardMarkup(row_width=3)
        start = page * 20
        end = start+self.butt_on_page
        flows = self.flows
        select_flows = flows[start:end]
        next_page = flows[end:end+self.butt_on_page]
        for flow in select_flows:
            markup.insert(InlineKeyboardButton(text=flow, callback_data=f'select_flow_{flow}'))
        markup.row(InlineKeyboardButton(
            text='------------------------------------------', callback_data='.....'))
        footer = []
        if page != 0:
            footer.append(InlineKeyboardButton(
                text='⬅️Предыдущая страница', callback_data=f'replace_page_{page-1}'))
        footer.append(InlineKeyboardButton(
            text=f'Стр. №{page+1}', callback_data=f'{page}'))
        if len(next_page) > 0:
            footer.append(InlineKeyboardButton(
                text='➡️Следующая страница', callback_data=f'replace_page_{page+1}'))
        markup.row(*footer)
        markup.row(self.btn_back_to_menu)
        return markup


kbd = Keyboards()