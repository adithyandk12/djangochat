import os

from django.core.asgi import get_asgi_application
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')
django.setup()

import room.routing
application = ProtocolTypeRouter({    
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
})


# your_project/asgi.py
# import os
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.core.asgi import get_asgi_application
# import djangochat.routing  # adjust this import

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             djangochat.routing.websocket_urlpatterns
#         )
#     ),
# })
