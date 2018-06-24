'''
module to query github
'''

import urllib.request
import json
import datetime
from mysite.models import GitHubEvent
from mysite import db

def get_events(user='hmm01i'):
    '''
    get events related to user
    '''
    req = urllib.request
    with req.urlopen('https://api.github.com/users/{}/events'.format(user)) as resp:
        raw_events = resp.read().decode()

    print(json.loads(raw_events))

def parse_events(raw_events):
    '''
    parsing the event data recieved from github

    separate func so i can send data from arbitrary source, ie file
    '''
    events_l = json.loads(raw_events)
    for event in events_l:
        if event['type'] == 'PushEvent':
            print('Pushed {} commits - {}'.format(event['payload']['size'], event['created_at']))
            # we will only want to add "new" events.
            # maybe we want the job to drop the table
            # although probably better to just check if an event has already been added
            # or use a data limiter for adding...
        event_exist = GitHubEvent.query.filter_by(event_id=event['id']).first()
        if not event_exist:
            db.session.add(GitHubEvent(event_type=event['type'],
                                   repo_id=event['repo']['id'],
                                   event_id=event['id'],
                                   event_timestamp=event['created_at']))
    db.session.commit()


if __name__ == "__main__":
    with open('data/raw_events.json') as f:
        parse_events(f.read())
    print(GitHubEvent.query.all())
