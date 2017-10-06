#!/usr/bin/env python

import argparse
import datetime
import dateutil.parser
import json
import requests

parser = argparse.ArgumentParser(description="Fetch data from The-Grid and convert to Agent-Stats format")
parser.add_argument("key", help="The-Grid API key")
parser.add_argument("-u", "--url", help="The-Grid API URL", default="https://the-grid.org/r/export/?key=")
parser.add_argument("-a", "--after", help="Only entries after date [YYYY-MM-DD]")
parser.add_argument("-b", "--before", help="Only entries before date [YYYY-MM-DD]")
args = parser.parse_args()

sourceData = []

if args.after:
    afterDt = dateutil.parser.parse(args.after)
else:
    afterDt = datetime.datetime.min

if args.before:
    beforeDt = dateutil.parser.parse(args.before)
else:
    beforeDt = datetime.datetime.max

url = args.url + args.key
resp = requests.get(url=url)
sourceData = json.loads(resp.text)

for i in sourceData:
    dt = datetime.datetime.fromtimestamp(i['timestamp'])

    if dt < afterDt or dt > beforeDt:
        continue
    
    print dt.strftime("%Y-%m-%d"),                  # Date
    print dt.strftime("%H:%M:%S"),                  # Time
    print i['stats']['ap'],                         # AP
    print i['stats']['portals_visited'],            # Explorer
    print i['stats']['portals_discovered'],         # Seer
    print i['stats']['xm_collected'],               # Collector
    print i['stats']['opr_agreements'],             # Recon
    print i['stats']['distance_walked'],            # Trekker
    print i['stats']['resonators_deployed'],        # Builder
    print i['stats']['links_created'],              # Connector
    print i['stats']['fields_created'],             # Mind-controller
    print i['stats']['mu_captured'],                # Illuminator
    print i['stats']['longest_link'],               # Binder
    print i['stats']['largest_field'],              # Country-master
    print i['stats']['xm_recharged'],               # Recharger
    print i['stats']['portals_captured'],           # Liberator
    print i['stats']['unique_portals_captured'],    # Pioneer
    print i['stats']['mods_deployed'],              # Engineer
    print i['stats']['resonators_destroyed'],       # Purifier
    print i['stats']['portals_neutralized'],        # Neutralizer
    print i['stats']['links_destroyed'],            # Disruptor
    print i['stats']['fields_destroyed'],           # Salvator
    print i['stats']['max_time_portal_held'],       # Guardian
    print i['stats']['link_maintained_max_days'],   # Smuggler
    print i['stats']['link_length_x_days_max'],     # Link-master
    print i['stats']['field_held_max_days'],        # Controller
    print i['stats']['largest_field_x_days_max'],   # Field-master
    print i['stats']['unique_missions_completed'],  # Specops
    print i['stats']['mission_days_attended'],      # Missionday
    print i['stats']['hacks'],                      # hacker
    print i['stats']['glyph_points'],               # translator
    print i['stats']['hacking_streak_max_days'],    # sojourner
    print i['stats']['agents_recruited'],           # Recruiter
    print '0',      # Exo5-controller. Not exposed via The-Grid
    print '""'      # Comment. Not exposed via The-Grid
