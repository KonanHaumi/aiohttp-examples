"""
Функция счетчика посещений страницы (проверить можно через обновление страницы)
"""

import aiohttp
from aiohttp import web

visits = 0

# создаем базовый обработчик для корневого маршрута "/"
async def handle (request) :
    global visits
    print( 'visits') # плюемся в терминал на каждое посещение
    visits += 1
    return web. Response(text = f"Visits: {visits}")

# создаем приложение aiohttp
app = web. Application ()

# Добавляем маршрут, указываем, что за корневой маршрут отвечает функция handle и так далее
app.add_routes ([
    web. get ('/', handle),
])
# Запускаем веб сервер
if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8000)