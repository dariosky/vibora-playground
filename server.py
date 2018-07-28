import os

from vibora import Vibora, Request
from vibora.responses import JsonResponse

app = Vibora()
DEBUG = os.environ.get('DEBUG', True)


@app.route('/')
async def home(request: Request):
    return JsonResponse({'hello': 'world'})


if __name__ == '__main__':
    print("Starting server.", "DEBUG MODE" if DEBUG else "")
    app.run(debug=DEBUG, host='0.0.0.0', port=8000)
