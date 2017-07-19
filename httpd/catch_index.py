#!/usr/bin/python3
# coding: utf-8


def IndexMiddleware(index='index.html'):
    async def middleware_factory(app, handler):
        async def index_handler(request):
            print(request)
            try:
                filename = request.match_info['filename']
                if not filename:
                    filename = index
                if filename.endswith('/'):
                    filename += index
                request.match_info['filename'] = filename
            except KeyError:
                pass
            return await handler(request)
        return index_handler
    return middleware_factory
