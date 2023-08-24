from get_method import getdata
from post_method import create_data
from update_method import update_data
from patch_method import patch_data
from delete_method import delete_data
import json

def lambda_handler(event, context=None):
    http_method = event['httpMethod']
    event_path = event['path']
    
    body = event['body']
    if body is not None:
        body_data = json.loads(body)
    else:
        body_data = None  
            
    table_params = event['pathParameters']
    if table_params is not None:
        table_id = table_params.get('id')
    else:
        table_id = None
    
    if http_method == 'GET':
        if '/test' == event_path:
            return getdata()
        
        elif f'/test/{table_id}' == event_path:
            return getdata(table_id)
        
        else:
            return "Invalid Url"
        
    if http_method == 'POST':
        if '/test' == event_path:
            return create_data(body_data)
        else:
            return "Invalid Url"
        
    if http_method == 'PUT':
        if f'/test/{table_id}' == event_path:
            return update_data(table_id, body_data)
        else:
            return "Invalid Url"
        
    if http_method == 'PATCH':
        if f'/test/{table_id}' == event_path:
            return patch_data(table_id, body_data)
        else:
            return "Invalid Url"
    
    if http_method == 'DELETE':
        if '/test' == event_path:
            return delete_data()
        
        elif f'/test/{table_id}' == event_path:
            return delete_data(table_id)
        
        else:
            return "Invalid Url"