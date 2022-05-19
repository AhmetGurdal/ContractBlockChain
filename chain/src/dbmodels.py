import uuid

class DocStatus:
    status = {  1:"User_Verify", 
                2:"Notary_Verify",
                3:"Waiting",
                4:"Verified",
                5:"Rejected"
             }

class Strings:
    notification_messages = {
        1 : ""
    }

class DBUser:
    def __init__(self, id : int, type: int, ss_no : int,
                notary_id : int, firstname : str, lastname : str,
                phone : str, email : str, password: str,
                private_key : str, public_key : str, last_login_at: int,
                created_at : int
                ) -> None:
        self.id = id
        self.type = type
        self.ss_no = ss_no,
        self.notary_id = notary_id
        self.firstname = firstname
        self.lastname = lastname,
        self.phone = phone,
        self.email = email
        self.password = password
        self.private_key = private_key
        self.public_key = public_key
        self.last_login_at = last_login_at
        self.created_at = created_at
        self.uuid = str(uuid.uuid4())

class DBBlock:

    def __init__(self, index :int, timestamp : int,
                 data : str, proof : int, prev_hash : str
                ) -> None:
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.proof = proof
        self.prev_hash = prev_hash

class DBDocUser:

    def __init__(self, id : int, doc_id : int, user_id : int, is_verified : bool):
        self.id = id
        self.doc_id = doc_id
        self.user_id = user_id
        self.is_verified = is_verified

class DBDocNotary:
    
    def __init__(self, id : int, doc_id : int, user_id : int) -> None:
        self.id = id
        self.doc_id = doc_id
        self.user_id = user_id

class DBDoc:
   
    def __init__( self, id: int, title: str,
                  origin_hash : str, storage_hash : str,
                  status : int, invalid_message : str, user_ids : list,
                  created_by : int, created_at : int,
                  last_update_at : int
                ) -> None:
        self.id = id
        self.title = title
        self.origin_hash = origin_hash
        self.storage_hash = storage_hash
        self.status = status
        self.invalid_message = invalid_message
        self.user_ids = user_ids
        self.created_by = created_by
        self.created_at = created_at
        self.last_update_at = last_update_at

class DBNotification:

    def __init__( self, id : int, user_id : int,
                  doc_id : int, is_seen : bool, message_id: int
                ) -> None:
        self.id = id
        self.user_id = user_id
        self.doc_id = doc_id
        self.is_seen = is_seen
        self.message_id = message_id
