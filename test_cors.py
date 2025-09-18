from app import create_app

app = create_app()

with app.test_client() as client:
    # send an Origin header as browsers do to see CORS response headers
    resp = client.get('/users/', headers={'Origin': 'https://example.vercel.app'})
    print('Status:', resp.status_code)
    for k, v in resp.headers.items():
        if 'Access-Control' in k or 'access-control' in k.lower():
            print(k+':', v)
    # print all headers for debugging
    print('\nAll headers:')
    for k, v in resp.headers.items():
        print(k+':', v)
