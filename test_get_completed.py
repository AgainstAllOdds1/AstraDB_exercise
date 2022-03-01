from connection import session

print('========================================')

try:
    result = session.execute("""select * from todoitems where user_id = 'john' and completed = True ALLOW FILTERING;""")

    for row in result:
        print(str(row))
except Exception as e:
    print(e)
    print('Failure')
else:
    print('Success')
print('========================================')