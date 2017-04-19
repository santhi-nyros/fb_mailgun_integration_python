Flaskapp  folder is script for getting new leads from facebook page and add lead to mail-gun mail list and sent a mail to lead.
------------------------------------------------------------------------------------
@@Enviroment Setup process@@

First we need to create a virtual enviroment for installing requirment.txt
In python we use following commands for cretaing virtual enviroment
$virtualenv <env_name>

activate the env with following command
$ source <env_name>/bin/activate

Then we need to install all packages on requirment.txt file

$pip install -r requirement.txt

or install one by one

$pip install Flask

$pip install facebookads

so on

---------------------------------------------------------------------------

@@ Key changes in method @@

I have added my sample account keys of facebook and mail-gun for run the script,
Because I don't have permisiions to add webhook to your facebook page.

You need to change those keys with your account keys

Here is the guidelines
-----------------------
flaskapp/hello.py


	def get_webhook_lead():
	    # Facebook app keys
	    my_app_id = <YOUR_FB_APP_ID>
	    my_app_secret = <YOUR_FB_APP_SECRET>
	    my_access_token = <YOUR_FB_APP_ACCESS_TOKEN>



flaskapp/hello.py
	def add_list_member(email,name):
		#Mail-gun api keys
		key = <YOUR_MAILGUN_API_KEY>
		domain = <YOUR_MAILGUN_DOMAIN> if it is sandbox domain, It will not sent mail to another mail ids, It's sends only authorized mail ids only.


Change mailList_url

	mailList_url = "https://api.mailgun.net/v3/lists/LIST@YOUR_DOMAIN_NAME/members"

Here we need to set your mail list domain name at LIST@YOUR_DOMAIN_NAME

	Refer https://documentation.mailgun.com/user_manual.html#mailing-lists

Server setup:
     Enviroment settings and keys settings are completed,
     Now you need to add and run these files on your server(ex: AWS, heroku etc)and **you will get url for this app**.


    I have added in heroku for testing purpose.
    My heroku url for this app : https://getfbleadsapp.herokuapp.com

-----------------------------------------------------------------------------

Once you done the setup and run the app successfully

I have given that url  while cretation of webhook on my sample page like


	Callback URL
	https://getfbleadsapp.herokuapp.com

	Verify Token
	abc123

Verify Token: abc123

Note: You don't need to setup any php files.Its pure python.
-----------------------------------------------------------------------------

For creating webhook on facebook page refer the following urls,

https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving/v2.8

Follow the video in this url or
Run the follow using curl or graph-api explorer "https://developers.facebook.com/tools/explorer/198409723950483?method=GET&path=&version=v2.8"

curl \
-F "object=page" \
-F "callback_url=https://www.yourcallbackurl.com" \
-F "fields=leadgen" \
-F "verify_token=abc123" \
-F "access_token=<APP_ACCESS_TOKEN>" \
"https://graph.facebook.com/<API_VERSION>/<APP_ID>/subscriptions"


Thankyou.
