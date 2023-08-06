def showDatabases():
    return '''sudo mysql -u root -e 'show databases';'''


def exportDatabase(dbName, dbPath):
    return f'''sudo mysqldump -u root {dbName} > '{dbPath}' --skip-dump-date --extended-insert=FALSE;'''
    # return f'''sudo mysqldump -u root {dbName} > '{dbPath}' --skip-dump-date --extended-insert | sed 's/),(/),\n(/g' > '{dbPath}' ;'''


def showDatabasesDocker(containerName, passwordFilePath):
    return f'''
    PASSWORD_PATH='{passwordFilePath}'
    PASSWORD=`cat $PASSWORD_PATH`
    docker exec {containerName} mysql -u root --password=$PASSWORD -e "SHOW DATABASES";
    '''


def exportDatabaseDocker(containerName, passwordFilePath, databaseName, outputPath):
    return f'''
    PASSWORD_PATH='{passwordFilePath}'
    PASSWORD=`cat $PASSWORD_PATH`
    docker exec {containerName} /usr/bin/mysqldump -u root --password=$PASSWORD {databaseName} > {outputPath} --skip-dump-date --extended-insert=FALSE;
    '''
