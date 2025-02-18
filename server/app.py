import os
import uuid
import boto3
from dotenv import load_dotenv
from chalice import Chalice, Response
from chalice import BadRequestError
from chalice.app import CORSConfig
from botocore.exceptions import ClientError
from pinecone import Pinecone, ServerlessSpec

load_dotenv()
pinecone_api_key=os.environ.get('PINECONE_API_KEY')

pc = Pinecone(pinecone_api_key)

# Create a CORS configuration
cors_config = CORSConfig(
    allow_origin='http://localhost:3000',
    allow_headers=['Content-Type'],
    max_age=600,
    expose_headers=['X-Special-Header'],
    allow_credentials=True
)

app = Chalice(app_name='lifeos_server')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Goals')

@app.route('/goals', methods=['GET'], cors=cors_config)
def list_goals():
    try:
        response = table.scan()
        return Response(body=response.get('Items', []), status_code=200)
    except ClientError as e:
        return Response(body={'error': str(e)}, status_code=500)

@app.route('/goal', methods=['POST'], cors=cors_config)
def create_goal():
    request_body = app.current_request.json_body
    
    if not request_body.get('title'):
        raise BadRequestError('Goal title is required')
    
    goal_id = str(uuid.uuid4())
    
    new_goal = {
        'goalId': goal_id,
        'title': request_body.get('title'),
        'description': request_body.get('description', ''),
        'tags': request_body.get('tags', [])
    }
    
    try:
        table.put_item(Item=new_goal)
        return Response(body=new_goal, status_code=201)
    except ClientError as e:
        return Response(body={'error': str(e)}, status_code=500)
