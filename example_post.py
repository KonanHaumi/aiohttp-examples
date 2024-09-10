"""
ОБРАБОТКА POST ЗАПРОСОВ
Теперь мы добавим возможность отправлять данные на сервер с помощью POST-запросов и обрабатывать эти данные. 
(Это нужно, когда вы хотите, чтобы пользователь мог добавлять записи в вашу записную книжку)

Проверить можно командой: 
curl -d '{"note": "My first note"}' http://127.0.0.1:8000/notes
После отправки полученные заметки отобразяться по ссылке /notes
"""

import aiohttp
from aiohttp import web

# создадим пустой список для хранения записей
notes = []

async def index (request):
    return web. Response(text='Hello world!')

# обработчик для добавления новой записи
async def add_note (request) :
    data = await request.json() # Получаем данные из POST-запроса 
    note = data.get('note') # Извлекаем поле "note" из данных
    if note:
        notes.append(note)
        return web. json_response({"message": f"Записка с содержимым: '{note}' добавлена!"}) # Возвращаем подтверждение
    return web. json_response({"error": "Ошибка! Пустая записка"}, status=400) # Ошибка, если запись не предоставлена

# обработчик для получения всех записей
async def get_notes(request):
    return web.json_response(notes)

# создаем приложение aiohttp
app = web. Application()

# Добавляем маршрут, указываем, что за корневой маршрут отвечает функция handle и так далее
app.add_routes([
    web.get('/', index),
    web.get('/notes', get_notes),
    web.post('/notes', add_note)
])

# Запускаем веб сервер
if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8000)