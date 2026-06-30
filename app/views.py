from django.shortcuts import render, redirect
from .models import *
import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)
group_id = -1004461894992

def home_page(request):

    brands = BrandLogo.objects.all()
    events = Event.objects.all()
    team = Team.objects.all()
    categories = GamesCategory.objects.all()
    game = Games.objects.all()
    game_photos = Game_photo.objects.all()
    context = {'brands':brands, 'events':events, 'team':team, 'categories':categories, 'game':game, 'game_photos':game_photos}
    return render(request, 'home.html', context)



def new_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company = request.POST.get('company')
        phone_number = request.POST.get('phone_number')
        comment = request.POST.get('comment')
        text = (f'Новый клиент! \n\n'
                f'Имя: {name} \n'
                f'Название компании: {company} \n'
                f'Номер клиента: {phone_number} \n'
                f'Коментарий: {comment}')
        bot.send_message(group_id, text)
    return redirect('/')


