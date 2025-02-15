from chalice import Chalice, Response
from chalice import BadRequestError
import uuid
from chalice.app import CORSConfig

# Create a CORS configuration
cors_config = CORSConfig(
    allow_origin='http://localhost:3000',  # Specify the exact client origin
    allow_headers=['Content-Type'],
    max_age=600,
    expose_headers=['X-Special-Header'],
    allow_credentials=True
)

app = Chalice(app_name='lifeos_server')

# In-memory storage for goals for now
goals = []

@app.route('/', methods=['GET'], cors=cors_config)
def index():
    return {'hello': 'world'}

@app.route('/goal', methods=['POST'], cors=cors_config)
def create_goal():
    request_body = app.current_request.json_body
    
    # Validate required fields
    if not request_body.get('title'):
        raise BadRequestError('Goal title is required')
    
    # Generate unique ID
    goal_id = str(uuid.uuid4())
    
    new_goal = {
        'id': goal_id,
        'title': request_body.get('title'),
        'description': request_body.get('description', ''),
        'tags': request_body.get('tags', [])
    }
    
    goals.append(new_goal)
    
    return Response(body=new_goal, status_code=201)

@app.route('/goals', methods=['GET'], cors=cors_config)
def list_goals():
     return Response(body=goals, status_code=200)
