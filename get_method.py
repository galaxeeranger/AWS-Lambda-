import pymysql
import json

def dbconnector():
    msqlcon = pymysql.connect(host='iesl-dev-db-syd.cdiah0tmq8hx.ap-southeast-2.rds.amazonaws.com',
                              user='shivmurat',
                              password='aIsZAAYV#6vfzpko',
                              db='Dummy-company_db',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor,
                              port=int(('3306')),
                              )
    return msqlcon

def All_Table_Data(cur):
    query = "SELECT * FROM Test_table"
    cur.execute(query)
    return cur.fetchall()

def All_Data_id(cur, table_id):
    print("table_id --->",table_id)
    if table_id is not None:
        query = "SELECT * FROM Test_table WHERE id=" + table_id
        cur.execute(query)
        return cur.fetchall()


def getdata(table_id=None):
    if table_id is None:
        try:
            con = dbconnector()
            cur = con.cursor()
            result = All_Table_Data(cur)
            con.close()

            return {'statusCode': 200, 'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'},
                    'body': json.dumps({"response": result}, default=str)}

        except Exception as e:
            return {'statusCode': 404, 'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'},
                'body': json.dumps({"Error": str(e)}, default=str)}
    else:
        try:
            con = dbconnector()
            cur = con.cursor()
            result = All_Data_id(cur, table_id)
            con.close()

            return {'statusCode': 200, 'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'},
                    'body': json.dumps({"response": result}, default=str)}

        except Exception as e:
            return {'statusCode': 404, 'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'},
                'body': json.dumps({"Error": str(e)}, default=str)}