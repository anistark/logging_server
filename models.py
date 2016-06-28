import config
import MySQLdb
import time


def insert_log(data):
    db = MySQLdb.connect(config.db['host'], config.db['credentials']['username'], config.db['credentials']['password'], config.db['db_name'])
    cursor = db.cursor()
    sql = "INSERT INTO CENTRALLOGS(CLIENT, LOG_LEVEL,MESSAGE,CREATED_AT) \
             VALUES ('%s', '%s', '%s' , '%s')" % \
        (data[0], data[1], data[2], time.strftime('%Y-%m-%d %H:%M:%S'))
    print(sql)
    try:
        cursor.execute(sql)
        print('Executed')
        db.commit()
    except Exception as e:
        print('Some Error')
        print e
        db.rollback()
    db.close()


def read_logs():
    response = []
    db = MySQLdb.connect(config.db['host'], config.db['credentials']['username'], config.db['credentials']['password'], config.db['db_name'])
    cursor = db.cursor()
    sql = "SELECT * FROM CENTRALLOGS"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            client = row[0]
            log_level = row[1]
            message = row[2]
            response_single = dict(
                    client=client,
                    log_level=log_level,
                    message=message
            )
            response.append(response_single)
    except Exception as e:
        print "Error: unable to fecth data"
        print e
    db.close()
    return response


def get_stats():
    return 'Something'
