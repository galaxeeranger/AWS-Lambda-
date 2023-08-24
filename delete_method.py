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

def Delete_Table_Data(cur, con):
    query_all = f"DELETE FROM `Dummy-company_db`.Test_table;"
    cur.execute(query_all)
    con.commit()
    return {"msg":"Table Data Deleted Successfully"}

def Delete_Id_Data(cur, con, table_id):
    print("table_id --->", table_id)
    if table_id is not None:
        query_id = f"DELETE FROM `Dummy-company_db`.Test_table WHERE `id` = '{table_id}';"
        cur.execute(query_id)
        con.commit()
        return {"msg": "Id Data Deleted Successfully"}
        

def delete_data(table_id=None):
    if table_id is None:
        try:
            con = dbconnector()
            cur = con.cursor()
            result = Delete_Table_Data(cur, con)
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
            result = Delete_Id_Data(cur, con, table_id)
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