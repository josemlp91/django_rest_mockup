import json
from recadvisor.apps.mockup.mockup import Mockup
from django.http import JsonResponse
from recadvisor.settings import DEBUG, ENABLE_MOCKUP_VIEWS, BASE_DIR


def mockup_view(view_name):
    def _mockup_view(func):
        def inner(*args, **kwargs):
            if DEBUG and ENABLE_MOCKUP_VIEWS:
                m = Mockup()
                current_mockup_view = m.get_mockup(view_name)
                if current_mockup_view:
                    mock_result = current_mockup_view.content
                    return JsonResponse(mock_result, safe=False)
            return func(*args, **kwargs)
        return inner
    return _mockup_view