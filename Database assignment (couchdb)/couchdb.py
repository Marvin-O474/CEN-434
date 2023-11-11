import couchdb
server = couchdb.Server('http://admin_user:admin_password@localhost:5984/')  # Replace the URL with your CouchDB server URL , REPLACE admin_user YOUR USERNAME AND admin_password with PASSWORD
#CREATE A DATABASE
db_name = 'assigment'
try:
    db = server.create('marvin')
except couchdb.http.PreconditionFailed as e:
    db = server[db_name]  # If the database already exists, use it
#WRITE DATA
data = {
    'firstname': 'nanami',
    'email': 'net@a.com'
}

doc_id, doc_rev = db.save(data)
#READ DATA
doc = db.get(doc_id)
print(doc)

#UPDATE DATA
doc = db.get(doc_id)
doc['firstname'] = 'micasa'
db.save(doc)

#MODIFY DATA
def modify_data(doc_id, new_data):
    doc = db.get(doc_id)
    doc.update(new_data)
    db.save(doc)

new_data = {'level': '200level'}
modify_data(doc_id, new_data)

#DELETE A DOCUMENT
doc = db.get(doc_id)
db.delete(doc)


