# import json
import os
import types


def main(response, request):
    # response.data = json.dumps(dict(request.headers))

    request.environ["apig_wsgi.context"] = types.SimpleNamespace()
    request.environ["apig_wsgi.context"].get_remaining_time_in_millis = time_remaining

    response.data = str(request.environ["apig_wsgi.context"].get_remaining_time_in_millis())
    response.data = str(request.start_time)
    response.data = os.environ["var1"]

    response.headers["Cache-Control"] = "max-age=0"
    return response


def time_remaining():
    return 123
