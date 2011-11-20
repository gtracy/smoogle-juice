from google.appengine.ext import db

class Smoogler(db.Model):

   phone       = db.StringProperty()

   auth_token  = db.StringProperty()
   auth_date   = db.DateTimeProperty()
  
   reg_code    = db.StringProperty()
   createDate  = db.DateTimeProperty(auto_now_add=True)

## end Smoogler


class AuditLog(db.Model):

    phone       = db.StringProperty()
    
    request     = db.StringProperty()
    response    = db.StringProperty()
    service     = db.StringProperty()
    
    sid         = db.StringProperty()   # twilio transaction id
    
    date        = db.DateTimeProperty(auto_now_add=True)
    
## end AuditLog

