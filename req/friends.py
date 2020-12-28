import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

token = '2d9042cd2d9042cd2d9042cd902de5ed8922d902d9042cd7279571ce3ff108b2608b688'

def requests_retry_session(
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def response_processing(resp):
    id = ''

    try:
        id = resp['response'][0]['id']
    except KeyError as err:
        return 'Bad response'

    return id

def get_user_id(uid):
    url = f'https://api.vk.com/method/users.get?v=5.71&access_token={token}&user_ids={uid}'

    s = requests.session()
    resp = requests_retry_session(session=s).get(url=url)

    resp = resp.json()

    return response_processing(resp)


def get_friends(id):
    pass


def get_age_of_friends(uid):
    id = get_user_id(uid)

    if not id.isalnum():
        return id

    friends_of_user = get_friends(id)

def calc_age(uid):
    age_of_friends = get_age_of_friends(uid)




if __name__ == '__main__':
    res = calc_age('tt349119')
    print(res)
