"""Public read-only entry into the native sample's own observer session."""
from http.cookies import SimpleCookie


class ObservedSample:
    def __init__(self, app, *, secure=False):
        self.app = app
        self.state = app.state
        self.secure = secure
        self.token = None

    def admitted(self):
        access = self.state.access
        session = access.session(self.token)
        if session is None:
            code = access.issue('demo', owner=True, principal_id='preview-host', display_name='Preview host')
            self.token, _ = access.login(code)
            session = access.observe(self.token, 'demo', 'peter')
        if (not session.get('read_only') or session.get('can_query')
                or (session.get('viewing_as') or {}).get('principal', {}).get('id') != 'peter'):
            raise RuntimeError('Use the native read-only sample observer.')
        return self.token

    async def __call__(self, scope, receive, send):
        if scope['type'] != 'http':
            return await self.app(scope, receive, send)
        from access import COOKIE
        token = self.admitted()
        headers = [(key, value) for key, value in scope.get('headers', []) if key.lower() != b'cookie']
        headers.append((b'cookie', (COOKIE + '=' + token).encode()))
        child = {**scope, 'headers': headers}

        async def observed(message):
            if message['type'] == 'http.response.start':
                cookie = SimpleCookie()
                cookie[COOKIE] = token
                cookie[COOKIE]['path'] = '/'
                cookie[COOKIE]['httponly'] = True
                cookie[COOKIE]['samesite'] = 'Strict'
                cookie[COOKIE]['max-age'] = 86400
                if self.secure:
                    cookie[COOKIE]['secure'] = True
                message = {**message, 'headers': [*message.get('headers', []), (b'set-cookie', cookie.output(header='').strip().encode())]}
            await send(message)

        return await self.app(child, receive, observed)


def public_sample(app, *, prefix='', secure=False, public_origin=''):
    from web_mount import MountedApp
    return MountedApp(ObservedSample(app, secure=secure), prefix=prefix, read_only=True, public_origin=public_origin)
