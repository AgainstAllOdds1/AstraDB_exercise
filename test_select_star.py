#!/usr/bin/env python3
from connection import session

print('========================================')
print('Start exercise by dropping and creating table')
try:
    result = session.execute("""select * from todoitems;""")

    for row in result:
        print(str(row))
except Exception as e:
    print(e)
    print('Failure')
else:
    print('Success')
print('========================================')

# curl -i -X POST -H "Content-Type: application/json" -d '{"completed":"False","title":"another one"}' "http://127.0.0.1:8080/api/v1/john/todos"
# One more thing, there was a tiny issue. If you have "False" in the json payload, the created record is actually completed=true, because "False" is a string and it is truthy. Heres the right request:

# curl -i -X POST -H "Content-Type: application/json" -d '{"completed":false,"title":"another one"}' "http://127.0.0.1:8080/api/v1/john/todos"

#ssh -R 80:localhost:8080 nokey@localhost.run - this command exposes the local server

#https://flask-cors.readthedocs.io/en/latest/api.html#using-the-cors-extension
