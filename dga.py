import locky
import locky
import datetime
import elasticsearch
from elasticsearch import helpers

def main():
    es = elasticsearch.Elasticsearch()
    base = datetime.date.today()
    numdays = 100
    dateRange = [base + datetime.timedelta(days=x) for x in range(0, numdays)]
    j = 0
    for d in dateRange:
        actions = []
        #generate locky domains - 120000 per day
        for seed in range(0,10000):
            date = d.strftime('%Y-%m-%d')
            obj = locky.dga(seed, d)
            for domain in obj.getDomains():
                head = {
                    '_index':'dga',
                    '_type':'domain',
                }
                head['_source'] = {
                    'date':date,
                    'seed':seed,
                    'domain':domain,
                    'ThreatFamily':'Locky'
                }
                actions.append(head)
        #generate necurs domains - 10000 per 4 days
        for seed in (5,7,9,11)
            date = d.strftime('%Y-%m-%d')
            obj = necurs.dga(seed, d)
            for domain in obj.getDomains():
                head = {
                    '_index':'dga',
                    '_type':'domain',
                }
                head['_source'] = {
                    'date':date,
                    'seed':seed,
                    'domain':domain,
                    'ThreatFamily':'Necurs'
                }
                actions.append(head)
        helpers.bulk(es, actions)
if __name__ == '__main__':
    main()
