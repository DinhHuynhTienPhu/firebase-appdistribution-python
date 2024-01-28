import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta,timezone    
import requests
import time

#functions

def get_newest_release(project_number, app_id, api_key):
    base_url = "https://firebaseappdistribution.googleapis.com/v1/"
    parent = f"projects/{project_number}/apps/{app_id}/releases"
    url = f"{base_url}{parent}"

    # Set up the headers with the API key for authorization
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON
        response_json = response.json()

        # Check if there are releases in the response
        if "releases" in response_json and response_json["releases"]:
            # Get the newest release (assuming releases are sorted by createTime)
            newest_release = response_json["releases"][0]

            return newest_release
        else:
            print("No releases found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

    return None













#main code



now =int(datetime.now(tz=timezone.utc).timestamp() )
# #exp in 30 minutes
exp = int((datetime.now(tz=timezone.utc) + timedelta(minutes=30)).timestamp() )

print("************* Code started at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "*************")
print("************* UTC time *************")
print("************* now:", now, "*************")
print("************* ************* *************\n\n")


#the valuse is from the service account key json file downloaded from google 
#read more at: https://developers.google.com/identity/protocols/oauth2/service-account#httprest
# when create service accout, rember to give it access to the project, best to give it the role "owner", or at least  give it the role that can access the app distribution. DO NOT LET THE ROLE OPTION EMPTY
values={
  "type": "service_account",
  "project_id": "tic-tac-toe-something",
  "private_key_id": "2f606f19c42ac03637786fbdb9c819180834a8something",
  "private_key": "-----BEGIN PRIVATE KEY-----\somethingkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDPtqNo9jWKDWE4\n46Omev4jCneIqBOvT8xhJtUQZRYo5Bq+icFUSw0bdqJN67tRaU0UDHqsBEbljXa1\nWUUYpRtH7p5XCKsbbjs61RzpzpFNUo3rYuGmmXSJrDMUGDbzVSq8eteALBaIAge2\noxm6bsIcirk7E4I2WpKlTAT7yNXujzEXmSQoggUfj5OtQEC6ZBkzt7uZ90vainvI\n20ohMIXByxuqArvN6c3fi5uLLSpox78y6cJV1upxIplUH2P5aImee5ZLq4K5UZn9\nUvog2pEnaBG18s0kaRzyT0UzSinQwMekVKi9pTiEG8ARzludDR1HNo1KM9kpF3sW\nSwYHsZG7AgMBAAECggEAHbO8t0gpzMVwBx4KK0bAK4uWHz0Fn5aWH7hZVGBYJF3F\n80QomKCozaoPuHvCi/g2VO0Z55ou9ylc9b6/si/98DHPg5uSODhxkM6jtU1cGsX4\n1FWN9fBQqVUt8qwpw28EzvHz+fiT+jvsFXJKPg4ThNhTd36pKpOWD7wIpGaKLPQb\n+b3hI36dF2HoBEU07yDW4f7VL3qmGwxRhZZCJfG4VXWq0pNC68f66PeENPX42FMX\nnWTiVO9c1k8OEInm7TQx6Dg1Jcx6qtNOyYjX2zMe+C7wwsqbFb5n7fumFcQiSU3L\nJB+XtjdMbq1i21UlLe3/x0G9sfp5sxoqxTHpt7RU6QKBgQDou2gglBp0BcW2As3h\n92g03xnlMzqE0TCRu2z66mU+tgvlMhR039RtpU0onkMpBdDJMLz6LR39mCz4eiqZ\npdwGiNHKWLQwU5bKn4nlS6gUA4hH11r3xU0zkjrmibU8ZtnuAzGDrw5+PpJVC+Qv\nQVfQQRIGIp9KI6sn1hEELHcN8wKBgQDkeuZKvls7G3t0oKzEnfnNR5Sc9Yb2AKOj\n/L8NOYCEb4WRBGtK9UVB00ZoNEZF/5nvXvFqiRPJjKccBUScdV0kPihKggjjNZyb\nr+j6D6RsP//VL55aGDjV38UmJWqxr+KokhRNc0BLAr0EyKSYzdxKPo0uH3nn/XbD\ng2hMTiY3GQKBgQC9MeSjX2Ll4O9qWHtAcF1BZgDqJ6wx3tFKF4Cvti8aPOoMp5qj\nrHZHsHK6S3YzeivR8pIeGuFfj/82/DF3eLMWiNFrWpMZGkria7GxOsDnjDuUk4i7\nFaT+AKlrUpWIBeCyMdxlvcDddkaFZsZYeBlIDi312N1/auGv38EzkGY0awKBgFZ7\n6sXqDhBuk6mO1DbMcWzxpmBPU9m0XjzJg+vWkz4OFKnS2WYTNzb2aRUyjFMcsED6\nWDlyT6of8nVZzSHIDwyT9p5VYFXYykHoMTDOUPektgsVLkR+HK1gOXj5+svtfsc+\nHC9A69o43CF+bUdlzPfRe5E02ukkeRsCl60ie7apAoGBALbTDU/VsYsm+DVE7tNn\nfl7gKrFU08QoBTQ1UJEeFw4Vz9d3BWoG3+CGan6I+bQ2Bh63uTHtqnxiYYlnpdRF\nb7UOJsky6RFqiyaOqspa5T28y6OveBK4QVEF8kTLZ7xfXHPxIHcrBTtBTlAwSJkU\nEn4bhsbqMkevdbZIPWivhgFA\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-i4e3g@tic-tac-toesomething.iam.gserviceaccount.com",
  "client_id": "111728777103085something4",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-i4e3g%40tic-tac-tsomething.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

#you must change the values below to your own values
project_number = "43555901something"
app_id = "1:435559015716:android:4685417c5470cc7dfesomething"
path = "D:/NotImportantProjects/tic tac toe/test.apk"
uploadFileName = "test.apk"
testerConfig ={
  "testerEmails": [
    "ff10111011@gmail.com"
  ],
  "groupAliases": [
    "testers"
  ]
}

print("************* Values *************")
print("*************json file from google: ",values)
print("************* project number", project_number, " app id: ", app_id, "*************\n\n")
print("************* Path: ", path, "*************")
print("************* upload file name: ", uploadFileName, "*************")
print("************* tester config: ", testerConfig, "*************")
print("************* ************* *************\n\n")




# now = int(time.time()) 
# exp = now + 3500

# Your claim set and header remain the same...
claim_set = {
    "iss": values['client_email'],
    "sub": values['client_email'],
    "scope": "https://www.googleapis.com/auth/cloud-platform",
    "aud": "https://www.googleapis.com/oauth2/v4/token",
    "iat": now,
    "exp": exp,
}

header = {"alg": "RS256", "typ": "JWT"}
private_key = values['private_key']

# Load private key using cryptography library...
private_key_obj = serialization.load_pem_private_key(
    private_key.encode(), password=None, backend=default_backend()
)

# Encode JWT...
jwt_token = jwt.encode(claim_set, private_key_obj, algorithm="RS256", headers=header)

print("************* Generated JWT Token *************")
print(jwt_token)
print("************* ******************* *************\n\n")

# stop the screen to read the output

token_endpoint = "https://oauth2.googleapis.com/token"

# Prepare the data for the POST request
data = {
    'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
    'assertion': jwt_token
}

# Make the HTTPS POST request
response = requests.post(token_endpoint, data=data)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse and print the response JSON
    response_json = response.json()
    #print(response_json)
    access_token = response_json.get('access_token')
    expires_in = response_json.get('expires_in')
    token_type = response_json.get('token_type')

    print("************** Access Token **************")
    print(f"Access Token: {access_token}")
    print("\n")
    print(f"Expires In: {expires_in} seconds")

    # 3 line empty space
    # print("\n\n\n")
    # print("Access Token: " + access_token)
    print("*************** **************** ***************\n\n")

else:
    # Print the error message if the request was not successful
    print(f"Error {response.status_code}: {response.text}")


#then push the apk file 

urlfirebase = "https://firebaseappdistribution.googleapis.com/upload/v1/projects/projectid here/apps/app id here/releases:upload" #change this, sorry i forgot to code it

headers = {
    "Authorization": "Bearer " + access_token,
    "X-Goog-Upload-File-Name": uploadFileName,
    "X-Goog-Upload-Protocol": "raw",
}
#path = D:\NotImportantProjects\tic tac toe\test.apk

body = open(path, "rb").read()
print("************** trying to upload file form path: ", path, "**************")

response = requests.post(urlfirebase, headers=headers, data=body)
print("************** Response after upload**************")
print(response.text)
print("************** **************** **************")
# press enter to continue

# if response.text inclue ""name": "projects/435559015716/apps"
# start to add tester

if response.text.find("name") != -1:
    print("************* getting infor about release ************")
    # add tester

    #the result text will be like this: "name": "projects/projectidhere/apps/appidhere/releases/-/operations/6f8d5b22d6db3c3594dab1432c2958d3a4563f922ce4f0305c874ef57168275e"
   #url =POST https://firebaseappdistribution.googleapis.com/v1/{name=projects/*/apps/*/releases/*}:distribute

    result_code = response.text;
    
    #get newest release id
    newest_release = get_newest_release(project_number, app_id, access_token)
    print("************** newest release **************")
    print("", newest_release)
    print("************** **************** **************\n\n")
    release_name = newest_release["name"]
    #name has this format: projects/{projectNumber}/apps/{appId}/releases/{releaseId}
    #split the name to get the release id
    release_id = release_name.split("/")[-1]

    # Constructing the URL: https://firebaseappdistribution.googleapis.com/v1/{name=projects/*/apps/*/releases/*}:distribute
    url = f"https://firebaseappdistribution.googleapis.com/v1/{release_name}:distribute"
    urlfirebase = url
    

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    body = testerConfig
    print ("************** trying to add tester **************")

    response = requests.post(urlfirebase, headers=headers, json=body)
    print("************** Response after add tester**************")
    print(response.text)
    print("************** Finish **************")

print("************* Code finish at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "*************")
print("************* UTC time *************")
print("************* now:", int(datetime.now(tz=timezone.utc).timestamp() )  , "*************")
print("************* ************* *************\n\n")
    # press enter to exit
input()








