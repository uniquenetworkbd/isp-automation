import routeros_api
import os

# রাউটারের তথ্য (আপনার রাউটারের আইপি ও পাসওয়ার্ড দিন)
ROUTER_HOST = 'YOUR_ROUTER_IP' # এখানে আপনার পাবলিক আইপি বা ডিএনএস দিন
ROUTER_USER = 'admin'
ROUTER_PASS = 'your_password'

def check_mikrotik():
    try:
        # কানেকশন তৈরি
        connection = routeros_api.RouterOsApiPool(
            ROUTER_HOST, 
            username=ROUTER_USER, 
            password=ROUTER_PASS, 
            plaintext_login=True
        )
        api = connection.get_api()
        
        # রাউটারের আইডেন্টিটি বা নাম রিড করা
        resource = api.get_resource('/system/identity')
        identity = resource.get()
        
        print(f"✅ কানেকশন সফল! রাউটারের নাম: {identity[0]['name']}")
        
        # একটি সিম্পল ডাটা রিড করা (Active Users)
        active_users = api.get_resource('/ip/hotspot/active').get()
        print(f"📊 বর্তমানে একটিভ ইউজার আছে: {len(active_users)} জন।")
        
        connection.disconnect()
        
    except Exception as e:
        print(f"❌ কানেকশন ব্যর্থ হয়েছে। কারণ: {e}")

if __name__ == "__main__":
    check_mikrotik()
