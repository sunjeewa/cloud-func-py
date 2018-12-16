def pubsubpy(data, context):
    """  Background Cloud Function to be triggered by Pub/Sub. """

    import base64

    if 'data' in data:
        name = base64.b64decode(data['data']).decode('utf-8')
    else:
        name = 'World'

    print('Hello {}!'.format(name))

