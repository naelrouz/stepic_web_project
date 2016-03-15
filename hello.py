def simplest_wsgi_app(environ, start_response):
     start_response('200 OK', [('Content-Type', 'text/plain')])
     yield 'Hello, world!'
