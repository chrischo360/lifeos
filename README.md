# LifeOS

Software to quickly create, categorize, and break down vague ideas into actionable clear goals. Takes advantage of a combination of AI, psychology, and two way communication.  

# Technologies

Framework: Next.js
Styling Framework: Mantine UI
Backend Language: Python
Cloud Service: AWS

# Get Started
## Client
1. `cd` to `client`
2. Run `yarn install`
3. Run `yarn run dev`

## Server
1. Set AWS credentials at `~/.aws/credentials`
```
[default]
aws_access_key_id=[AWS_ACCESS_KEY_ID]
aws_secret_access_key=[AWS_SECRET_ACCESS_KEY]
```
2. Set AWS config at `~/.aws/config` with 
```
[default]
region = us-east-1
output = json
```
3. Ensure you have pipenv installed
4. Run `pipenv shell`
5. Run `pipenv install`
6. Run `chalice local` or `chalice deploy` 
