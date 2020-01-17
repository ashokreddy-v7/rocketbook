import ReloadAuthorizationKey as Auth
import requests
import sys
import cx_Oracle
import datetime
import os
import logging
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config


log_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
logging.basicConfig(filename=r'D:\JIVEProject\JiveActivityLoadOracle\runtime'+log_time+'.log',filemode='w', level=logging.DEBUG)

os.environ["NLS_LANG"]="AMERICAN_AMERICA.AL32UTF8"
con_str = config.cyOraConn

try:
    connection = cx_Oracle.connect(con_str)
    cursor = connection.cursor()
except Exception as e:
    print("Cannot connect to Database")
    print(str(e))
    sys.exit(1)

api_url = config.jivePayload
payload = config.jive_data_payload

try:
    jive_res = requests.get(api_url, headers={'Authorization': Auth.Get_NewAutorizationKey()}, params=payload, proxies=Auth.proxies, verify=False)
    jive_data = jive_res.json()
except Exception as e:
    logging.warning("Error in Jive Json Response")
    logging.warning(e)
    logging.warning(jive_res.text)
    sys.exit(1)
# paging_data = jive_data['paging']
next_page = '1'
# if paging_data.has_key('next'):
#    next_page = paging_data['next']
while next_page:
    list_data = jive_data['list']
    for each_item in list_data:

        activity = {}
        if 'name' in each_item:
            activity['ACTIVITYNAME'] = each_item['name']
        if 'timestamp' in each_item:
            activity['TIMESTAMP'] = each_item['timestamp']
        if 'actorID' in each_item:
            activity['ACTORID'] = each_item['actorID']
        if 'actorType' in each_item:
            activity['ACTORTYPE'] = each_item['actorType']
        if 'activityType' in each_item:
            activity['ACTIVITYTYPE'] = each_item['activityType']
        if 'actionObjectId' in each_item:
            activity['ACTIONOBJECTID'] = each_item['actionObjectId']
        if 'actionObjectType' in each_item:
            activity['ACTIONOBJECTTYPE'] = each_item['actionObjectType']
        if 'activity' in each_item:
            if 'actor' in each_item['activity']:
                if 'objectType' in each_item['activity']['actor']:
                    activity['ACTOROBJECTTYPE'] = each_item['activity']['actor']['objectType']

                if 'objectId' in each_item['activity']['actor']:
                    activity['ACTOROBJECTID'] = each_item['activity']['actor']['objectId']

                if 'objectHash' in each_item['activity']['actor']:
                    activity['ACTOROBJECTHASH'] = each_item['activity']['actor']['objectHash']

                if 'username' in each_item['activity']['actor']:
                    activity['ACTOR_USERNAME'] = each_item['activity']['actor']['username']

                if 'name' in each_item['activity']['actor']:
                    activity['ACTOR_NAME'] = each_item['activity']['actor']['name']

                if 'firstName' in each_item['activity']['actor']:
                    activity['ACTOR_FIRSTNAME'] = each_item['activity']['actor']['firstName']

                if 'lastName' in each_item['activity']['actor']:
                    activity['ACTOR_LASTNAME'] = each_item['activity']['actor']['lastName']

                if 'email' in each_item['activity']['actor']:
                    activity['ACTOR_EMAIL'] = each_item['activity']['actor']['email']

                if 'creationDate' in each_item['activity']['actor']:
                    if each_item['activity']['actor']['creationDate'] > 0:
                        activity['ACTOR_CREATIONDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actor']['creationDate'] / 1000))

                if 'modificationDate' in each_item['activity']['actor']:
                    if each_item['activity']['actor']['modificationDate'] > 0:
                        activity['ACTOR_MODIFICATIONDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actor']['modificationDate'] / 1000))

                if 'profile' in each_item['activity']['actor']:
                    if 'country' in each_item['activity']['actor']['profile']:
                        activity['ACTOR_COUNTRY'] = each_item['activity']['actor']['profile']['country']

                    if 'address2' in each_item['activity']['actor']['profile']:
                        activity['ACTOR_ADDRESS2'] = each_item['activity']['actor']['profile']['address2']

                    if 'city' in each_item['activity']['actor']['profile']:
                        activity['ACTOR_CITY'] = each_item['activity']['actor']['profile']['city']

                    if 'address1' in each_item['activity']['actor']['profile']:
                        activity['ACTOR_ADDRESS1'] = each_item['activity']['actor']['profile']['address1']

                    if 'title' in each_item['activity']['actor']['profile']:
                        activity['ACTOR_TITLE'] = each_item['activity']['actor']['profile']['title']

                    if 'phoneNumber' in each_item['activity']['actor']['profile']:
                        activity['ACTOR_PHONENUMBER'] = each_item['activity']['actor']['profile']['phoneNumber']

                    if 'company' in each_item['activity']['actor']['profile']:
                        activity['ACTOR_COMPANY'] = each_item['activity']['actor']['profile']['company']

                    if 'pleasecontactmeregaringproductsupport' in each_item['activity']['actor']['profile']:
                        activity['ACTOR_CONTACTME'] = each_item['activity']['actor']['profile']['pleasecontactmeregardingproductsupport']

                if 'enabled' in each_item['activity']['actor']:
                    activity['ACTOR_ENABLED'] = str(each_item['activity']['actor']['enabled'])

                if 'lastLoggedIn' in each_item['activity']['actor']:
                    if each_item['activity']['actor']['lastLoggedIn'] > 0:
                        activity['ACTOR_LASTLOGGEDIN'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actor']['lastLoggedIn'] / 1000))

                if 'lastProfileUpdate' in each_item['activity']['actor']:
                    if each_item['activity']['actor']['lastProfileUpdate'] > 0:
                        activity['ACTOR_LASTPROFILEUPDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actor']['lastProfileUpdate'] / 1000))

                if 'federated' in each_item['activity']['actor']:
                    activity['ACTOR_FEDERATED'] = str(each_item['activity']['actor']['federated'])

                if 'visible' in each_item['activity']['actor']:
                    activity['ACTOR_VISIBLE'] = str(each_item['activity']['actor']['visible'])

                if 'status' in each_item['activity']['actor']:
                    activity['ACTOR_STATUS'] = str(each_item['activity']['actor']['status'])

                if 'url' in each_item['activity']['actor']:
                    activity['ACTOR_URL'] = each_item['activity']['actor']['url']

            if 'action' in each_item['activity']:
                activity['ACTION'] = each_item['activity']['action']

            if 'actionObject' in each_item['activity']:
                if 'objectType' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_OBJECTTYPE'] = each_item['activity']['actionObject']['objectType']

                if 'objectId' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_OBJECTID'] = each_item['activity']['actionObject']['objectId']

                if 'objectHash' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_OBJECTHASH'] = each_item['activity']['actionObject']['objectHash']

                if 'subject' in each_item['activity']['actionObject']:
                    activity['SUBJECT'] = each_item['activity']['actionObject']['subject']

                if 'creationDate' in each_item['activity']['actionObject']:
                    if each_item['activity']['actionObject']['creationDate'] > 0:
                        activity['ACTOBJ_CREATIONDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actionObject']['creationDate'] / 1000))

                if 'modifiedDate' in each_item['activity']['actionObject']:
                    if each_item['activity']['actionObject']['modifiedDate'] > 0:
                        activity['ACTOBJ_MODIFIEDDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actionObject']['modifiedDate'] / 1000))

                if 'author' in each_item['activity']['actionObject']:
                    if 'objectType' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_OBJECTTYPE'] = each_item['activity']['actionObject']['author']['objectType']

                    if 'objectId' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_OBJECTID'] = each_item['activity']['actionObject']['author']['objectId']

                    if 'username' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_USERNAME'] = each_item['activity']['actionObject']['author']['username']

                    if 'name' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_NAME'] = each_item['activity']['actionObject']['author']['name']

                    if 'firstName' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_FIRSTNAME'] = each_item['activity']['actionObject']['author']['firstName']

                    if 'lastName' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_LASTNAME'] = each_item['activity']['actionObject']['author']['lastName']

                    if 'email' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_EMAIL'] = each_item['activity']['actionObject']['author']['email']

                    if 'creationDate' in each_item['activity']['actionObject']['author']:
                        if each_item['activity']['actionObject']['author']['creationDate'] > 0:
                            activity['AUTHOR_CREATIONDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actionObject']['author']['creationDate']/1000))

                    if 'modificationDate' in each_item['activity']['actionObject']['author']:
                        if each_item['activity']['actionObject']['author']['modificationDate'] > 0:
                            activity['AUTHOR_MODIFICATIONDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actionObject']['author']['modificationDate'] / 1000))

                    if 'profile' in each_item['activity']['actionObject']['author']:
                        if 'country' in each_item['activity']['actionObject']['author']['profile']:
                            activity['AUTHOR_COUNTRY'] = each_item['activity']['actionObject']['author']['profile']['country']

                        if 'address2' in each_item['activity']['actionObject']['author']['profile']:
                            activity['AUTHOR_ADDRESS2'] = each_item['activity']['actionObject']['author']['profile']['address2']

                        if 'address1' in each_item['activity']['actionObject']['author']['profile']:
                            activity['AUTHOR_ADDRESS1'] = each_item['activity']['actionObject']['author']['profile']['address1']

                        if 'city' in each_item['activity']['actionObject']['author']['profile']:
                            activity['AUTHOR_CITY'] = each_item['activity']['actionObject']['author']['profile']['city']

                        if 'title' in each_item['activity']['actionObject']['author']['profile']:
                            activity['AUTHOR_TITLE'] = each_item['activity']['actionObject']['author']['profile']['title']

                        if 'phoneNumber' in each_item['activity']['actionObject']['author']['profile']:
                            activity['AUTHOR_PHONENUMBER'] = each_item['activity']['actionObject']['author']['profile']['phoneNumber']

                        if 'company' in each_item['activity']['actionObject']['author']['profile']:
                            activity['AUTHOR_COMPANY'] = each_item['activity']['actionObject']['author']['profile']['company']

                        if 'pleasecontactmeregardingproductsupport' in each_item['activity']['actionObject']['author']['profile']:
                            activity['AUTHOR_CONTACTME'] = each_item['activity']['actionObject']['author']['profile']['pleasecontactmeregardingproductsupport']

                    if 'enabled' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_ENABLED'] = str(each_item['activity']['actionObject']['author']['enabled'])

                    if 'lastLoggedIn' in each_item['activity']['actionObject']['author']:
                        if each_item['activity']['actionObject']['author']['lastLoggedIn'] > 0:
                            activity['AUTHOR_LASTLOGGEDIN'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actionObject']['author']['lastLoggedIn'] / 1000))

                    if 'lastProfileUpdate' in each_item['activity']['actionObject']['author']:
                        if each_item['activity']['actionObject']['author']['lastProfileUpdate'] > 0:
                            activity['AUTHOR_LASTPROFILEUPDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actionObject']['author']['lastProfileUpdate'] / 1000))

                    if 'federated' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_FEDERATED'] = str(each_item['activity']['actionObject']['author']['federated'])

                    if 'visible' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_VISIBLE'] = str(each_item['activity']['actionObject']['author']['visible'])

                    if 'status' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_STATUS'] = str(each_item['activity']['actionObject']['author']['status'])

                    if 'url' in each_item['activity']['actionObject']['author']:
                        activity['AUTHOR_URL'] = each_item['activity']['actionObject']['author']['url']

                if 'containerId' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_CONTAINERID'] = each_item['activity']['actionObject']['containerId']

                if 'containerType' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_CONTAINERTYPE'] = each_item['activity']['actionObject']['containerType']

                if 'url' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_URL'] = each_item['activity']['actionObject']['url']

                if 'name' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_NAME'] = each_item['activity']['actionObject']['name']

                if 'displayName' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_DISPLAYNAME'] = each_item['activity']['actionObject']['displayName']

                if 'description' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_DESCRIPTION'] = each_item['activity']['actionObject']['description']

                if 'parentId' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_PARENTID'] = each_item['activity']['actionObject']['parentId']

                if 'parentType' in each_item['activity']['actionObject']:
                    activity['ACTOBJ_PARENTTYPE'] = each_item['activity']['actionObject']['parentType']

                if 'isQuestion' in each_item['activity']['actionObject']:
                    activity['IS_QUESTION'] = str(each_item['activity']['actionObject']['isQuestion'])

                if 'questionStatus' in each_item['activity']['actionObject']:
                    activity['QUESTION_STATUS'] = str(each_item['activity']['actionObject']['questionStatus'])

                if 'resolved' in each_item['activity']['actionObject']:
                    activity['RESOLVED'] = str(each_item['activity']['actionObject']['resolved'])

                if 'assumedResolved' in each_item['activity']['actionObject']:
                    activity['ASSUMED_RESOLVED'] = str(each_item['activity']['actionObject']['assumedResolved'])

                if 'open' in each_item['activity']['actionObject']:
                    activity['IS_OPEN'] = str(each_item['activity']['actionObject']['open'])

                if 'questionCreationDate' in each_item['activity']['actionObject']:
                    if each_item['activity']['actionObject']['questionCreationDate'] > 0:
                        activity['QUESTION_CREATIONDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actionObject']['questionCreationDate'] / 1000))

                if 'resolutionDate' in each_item['activity']['actionObject']:
                    if each_item['activity']['actionObject']['resolutionDate'] > 0:
                        activity['RESOLUTIONDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['actionObject']['resolutionDate'] / 1000))

                if 'numHelpfulAnswers' in each_item['activity']['actionObject']:
                    activity['NUM_HELPFUL_ANSWERS'] = each_item['activity']['actionObject']['numHelpfulAnswers']

                if 'numReplies' in each_item['activity']['actionObject']:
                    activity['NUM_REPLIES'] = each_item['activity']['actionObject']['numReplies']

            if 'activityTime' in each_item['activity']:
                if each_item['activity']['activityTime'] > 0:
                    activity['ACTIVITYTIME'] = datetime.datetime.fromtimestamp(int(each_item['activity']['activityTime'] / 1000))

            if 'destination' in each_item['activity']:
                if 'objectType' in each_item['activity']['destination']:
                    activity['DEST_OBJECTTYPE'] = each_item['activity']['destination']['objectType']

                if 'objectId' in each_item['activity']['destination']:
                    activity['DEST_OBJECTID'] = each_item['activity']['destination']['objectId']

                if 'objectHash' in each_item['activity']['destination']:
                    activity['DEST_OBJECTHASH'] = each_item['activity']['destination']['objectHash']

                if 'name' in each_item['activity']['destination']:
                    activity['DEST_NAME'] = each_item['activity']['destination']['name']

                if 'displayName' in each_item['activity']['destination']:
                    activity['DEST_DISPLAYNAME'] = each_item['activity']['destination']['displayName']

                if 'description' in each_item['activity']['destination']:
                    activity['DEST_DESCRIPTION'] = each_item['activity']['destination']['description']

                if 'creationDate' in each_item['activity']['destination']:
                    if each_item['activity']['destination']['creationDate'] > 0:
                        activity['DEST_CREATIONDATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['destination']['creationDate'] / 1000))

                if 'modificationDate' in each_item['activity']['destination']:
                    if each_item['activity']['destination']['modificationDate'] > 0:
                        activity['DEST_MODIFICATION_DATE'] = datetime.datetime.fromtimestamp(int(each_item['activity']['destination']['modificationDate'] / 1000))

                if 'url' in each_item['activity']['destination']:
                    activity['DEST_URL'] = each_item['activity']['destination']['url']

                if 'status' in each_item['activity']['destination']:
                    activity['DEST_STATUS'] = each_item['activity']['destination']['status']

                if 'parentId' in each_item['activity']['destination']:
                    activity['DEST_PARENTID'] = each_item['activity']['destination']['parentId']

                if 'parentType' in each_item['activity']['destination']:
                    activity['DEST_PARENTTYPE'] = each_item['activity']['destination']['parentType']

        if 'containerId' in each_item:
            activity['CONTAINERID'] = each_item['containerId']

        if 'containerType' in each_item:
            activity['CONTAINERTYPE'] = each_item['containerType']

        fields = activity.keys()
        values = activity.values()
        bindvars = ":"+",:".join(fields)
        SQL = "INSERT INTO DW_TEMP.JIVE_ACTIVITY_DATA_TMP (%s) VALUES (%s)" %(",".join(fields), bindvars)

        try:

            cursor.prepare(SQL)
            cursor.execute(None, activity)

        except Exception as e:
            logging.warning(e)
            logging.info(activity)
    paging_data = jive_data['paging']
    connection.commit()
    if 'next' in paging_data:
        next_page = paging_data['next']
        print(next_page)
        try:
            jive_res = requests.get(next_page, headers={'Authorization':Auth.Get_NewAutorizationKey()}, proxies=Auth.proxies, verify=False)
            jive_data = jive_res.json()
        except Exception as e:
            logging.warning("Error in Jive Json Response")
            logging.warning(e)
            logging.warning(jive_res.text)
            logging.info(next_page)
            sys.exit(1)
    else:
        next_page = None
        print(next_page)

cursor.close()
connection.close()

