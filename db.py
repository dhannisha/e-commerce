from dotenv import load_dotenv
import os
from supabase import create_client

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SECRET_KEY"))
#response=(supabase.table("authentication").insert({'id':1,'username':'admin','password':'admin@123'}).execute())
# print (response.data)

def insert_record_auth(id,username,password):
    response = supabase.table("authentication").insert({"id": id, "username": username, "password": password}).execute()
    return response.data
def insert_record_orders(o_id,u_id,total,status):
    response = supabase.table("orders").insert({"order_id": o_id, "user_id": u_id, "total": total, "status": status}).execute()
    return response.data
def insert_record_products(id,pro_name,pro_description,pro_price,stock,image_url):
    response = supabase.table("products").insert({"id": id, "product_name": pro_name, "description": pro_description, "price": pro_price, "stock": stock, "image_url": image_url}).execute()
    return response.data
def insert_record_ordered_items(id,o_id,p_id,quantity,price):
    response = supabase.table("ordered_items").insert({"id": id, "order_id": o_id, "product_id": p_id, "quantity": quantity, "price": price}).execute()
    return response.data
def insert_record_profile(id,name,mobile_no):
    response = supabase.table("profile").insert({"id": id, "name": name, "mobilenumber": mobile_no}).execute()
    return response.data

def select_records_auth():
    response = supabase.table("authentication").select("*").execute()
    return response.data
def select_records_orders():
    response = supabase.table("orders").select("*").execute()
    return response.data
def select_records_products():
    response = supabase.table("products").select("*").execute()
    return response.data
def select_records_ordered_items():
    response = supabase.table("ordered_items").select("*").execute()
    return response.data
def select_records_profile():
    response = supabase.table("profile").select("*").execute()
    return response.data

def authenticate_user(username, password):
    response = supabase.table("authentication").select("*").eq("username", username).eq("password", password).execute()
    if response.data:
        return True
    else:
        return False

#insert_record_auth("A101", "dhannisha", "12345")

#insert_record_profile("A101", "Dhannisha", 9876543210)

#insert_record_products("P101", "Chocolate Cake", "Fresh chocolate cake", 500, 10, "cake.jpg")

#insert_record_orders("O101", "A101", 500, "Pending")

#insert_record_ordered_items("OI101", "O101", "P101", 2, 1000)

select_records_auth()

def authenticate_user(username, password):
    response = supabase.table("authentication").select("*").eq("username", username).eq("password", password).execute()
    if response.data:
        return response.data[0]
    else:
        return False