import azure.functions as func
import logging
import Service.queue_samples_hello_world as colas
from azure.identity import DefaultAzureCredential

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    default_queue_name = "slrosalesqueue"

    name = req.params.get('name')
    cola = req.params.get('cola')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = None

        if req_body:
            name = req_body.get('name')
            if not cola:
                cola = req_body.get('cola')

    sample = colas.QueueHelloWorldSamples()
    queue_name = cola if cola else default_queue_name
    sample.create_client_with_connection_string()
    sample.queue_and_messages_example(queue_name)

    if name:
        return func.HttpResponse(f"Hello, {name}. With queue management executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.function_name(name="DeletedQueue")
@app.route(route="queue/delete", auth_level=func.AuthLevel.ANONYMOUS, methods=['POST'])
def delete_queue(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    default_queue_name = "slrosalesqueue"
    
    name = req.params.get('name')
    cola = req.params.get('cola')
    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = None
        
        if req_body:
            name = req_body.get('name')
            if not cola:
                cola = req_body.get('cola')
    
    queue_name = cola if cola else default_queue_name
    
    sample = colas.QueueHelloWorldSamples()
    sample.create_client_with_connection_string()
    sample.delete_queue_do(queue_name)

    if name:
        return func.HttpResponse(f"Hello, {name}. With queue management executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )