  
import requests
import hmac
import hashlib
import base64
import json
import urllib
from datetime import datetime
class Invoice(object):
    MID=''
    MODE=''
    APIKEY=''
    SECRETKEY=''
    totalAmount=0
    URI="https://api.kashier.io/paymentRequest"
    URI_TEST="https://test-api.kashier.io/paymentRequest"
    items=[]
    def __init__(self, MID, APIKEY, MODE,SECRETKEY):

        self.MID = MID
        self.MODE = MODE
        self.APIKEY = APIKEY
        self.SECRETKEY = SECRETKEY
  
   
    def init_item(self,description,quantity,unitPrice,itemName,subTotal):
        self.totalAmount+=subTotal
        item=   {
            "description": description,
            "quantity": quantity,
            "itemName": itemName,
            "unitPrice": unitPrice,
            "subTotal": subTotal
            }
        dict_copy = item.copy() # 👈️ 

        self.items.append( dict_copy)
       
        return self.items

    
    def create_invoice(self,items, totalAmount,invoiceReferenceId="",currency="EGP",tax=0,dueDate=datetime.today().strftime('%Y-%m-%d'),customerName=" ",description=" " ):
     
        if self.MODE=='live' :
          url= self.URI 
        else:
           url= self.URI_TEST  
        
        r = requests.post( f'{url}?currency={currency}', json={
        
        "paymentType": "professional",
        "merchantId":  self.MID,
        "totalAmount": totalAmount ,
        "customerName": customerName,
        "description": description,
        "dueDate": dueDate,
        "invoiceReferenceId": invoiceReferenceId,
        "invoiceItems":items,
        
        "state": "submitted",
        "tax": tax
        },
        headers={"Authorization":  self.SECRETKEY}
            )
        return r
    def share_invoiceBySMS(self,phone ,invoiceReferenceId,storeName="test ",customerName=" test"):
        if self.MODE=='live' :
          url= self.URI 
        else:
           url= self.URI_TEST  
        share= {
            "subDomainUrl": "http://merchant.kashier.io/en/prepay",
            "urlIdentifier": invoiceReferenceId,
            "customerName": customerName,
            "storeName": storeName,
            "customerPhoneNumber": phone,
            "language": "en",
            "operation": "phone"
            }
        r = requests.post( f'{url}/sendInvoiceBy?operation=share_payment_Request&currency=EGP', json=share,
         headers={"Authorization":  self.SECRETKEY}
            )
        print(share)
    
        return r
    def share_invoiceByEmail(self,email ,invoiceReferenceId,storeName=" ",customerName=" ",currency="EGP"):
        if self.MODE=='live' :
          url= self.URI 
        else:
           url= self.URI_TEST  
        share= {
            "subDomainUrl": "http://merchant.kashier.io/en/prepay",
            "urlIdentifier": invoiceReferenceId,
            "customerName": customerName,
            "storeName": storeName,
            "customerEmail": email,
            "language": "en",
            "operation": "email"
            }
        r = requests.post( f'{url}/sendInvoiceBy?operation=share_payment_Request&currency={currency}', json=share,
         headers={"Authorization":  self.SECRETKEY}
            )
        
    
    def get_invoice(self ,invoiceReferenceId):
        if self.MODE=='live' :
          url= self.URI 
        else:
           url= self.URI_TEST  
       
        r = requests.get( f'{url}/{invoiceReferenceId}', 
         headers={"Authorization":  self.SECRETKEY}
            )
        
    
        return r

    def get_list_invoices(self,current=1,pageSize=15,currency="EGP"):

        if self.MODE=='live' :
          url= self.URI 
        else:
           url= self.URI_TEST  
        #return f'{url}/{self.MID}?current={current}&pageSize={pageSize}?currency=EGP'
        r = requests.get( f'{url}s/{self.MID}?current={current} &pageSize={pageSize}&currency={currency}', 
         headers={"Authorization":  self.SECRETKEY}
            )
        
    
        return r
    def verify_webhook(self,request, hmac_header=''):
           payload = request.body
    #
           data=json.loads(payload)
           hmac_header = request.headers.get('x-kashier-signature')
         
           queryString = {}
           for key in data['data']['signatureKeys']:
                # return key
              queryString[key] = str(data['data'][key])
              # queryString[key] = ('%20').join( str(data['data'][key]).split(' '))
           
          
           secret = bytes(self.APIKEY, 'utf-8')
           queryString  = self.http_build_query( queryString).encode()
           
           signature = hmac.new(secret, queryString, hashlib.sha256).hexdigest()
           
           return signature == hmac_header
    
    def http_build_query(self,data):
      
      
       return urllib.parse.urlencode(data,quote_via=urllib.parse.quote)