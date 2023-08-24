import pymysql
import json

def dbconnector():
    msqlcon = pymysql.connect(host='***************************************',
                              user='************',
                              password='***********',
                              db='***********',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor,
                              port=int(('3306')),
                              )
    return msqlcon

def Insert_Data(con, cur,table_id, body_data):
    if body_data.get('NAME') is None:
        query_set = f"UPDATE `Dummy-company_db`.`Test_table` SET `EMAIL` = '{body_data.get('EMAIL')}', `PHONE` = '{body_data.get('PHONE')}' WHERE (`id` = '{table_id}');"
    elif body_data.get('EMAIL') is None:
        query_set = f"UPDATE `Dummy-company_db`.`Test_table` SET `NAME` = '{body_data.get('NAME')}', `PHONE` = '{body_data.get('PHONE')}' WHERE (`id` = '{table_id}');"
    elif body_data.get('PHONE') is None:
        query_set = f"UPDATE `Dummy-company_db`.`Test_table` SET `NAME` = '{body_data.get('NAME')}', `EMAIL` = '{body_data.get('EMAIL')}' WHERE (`id` = '{table_id}');"
    else:
        query_set = f"UPDATE `Dummy-company_db`.`Test_table` SET `NAME` = '{body_data.get('NAME')}', `EMAIL` = '{body_data.get('EMAIL')}', `PHONE` = '{body_data.get('PHONE')}' WHERE (`id` = '{table_id}');"
    cur.execute(query_set)
    con.commit()
    return {"msg": "Data Updated Successfully"}
    

def patch_data(table_id=None, body_data=None):
    if table_id is not None:
        try:
            con = dbconnector()
            cur = con.cursor()
            result = Insert_Data(con, cur,table_id, body_data)
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
 
 
 
