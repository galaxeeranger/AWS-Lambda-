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

def Insert_Data(con, cur, body_data):
    query_set = f"INSERT INTO `Dummy-company_db`.`Test_table` (`NAME`, `EMAIL`, `PHONE`) VALUES ('{body_data.get('NAME')}', '{body_data.get('EMAIL')}', '{body_data.get('PHONE')}');"
    cur.execute(query_set)
    con.commit()
    return {"msg": "Data Created Successfully"}
    

def create_data(body_data=None):
    if body_data is not None:
        try:
            con = dbconnector()
            cur = con.cursor()
            result = Insert_Data(con, cur, body_data)
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
 
 
 
