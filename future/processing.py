import os
import sys
import csv
import time
import concurrent.futures


NATION_LIST = ('Singapore Germany Israel Italy Canada France Spain Mexico').split()
TARGET_CSV = '/Users/an/workspaces/python-advance/future/nations.csv'
DEST_DIR = '/Users/an/workspaces/python-advance/future/csvs'
HEADER = ['Region','Country','Item Type','Sales Channel','Order Priority','Order Date','Order ID','Ship Date','Units Sold','Unit Price','Unit Cost','Total Revenue','Total Cost','Total Profit']


def save_csv(data, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=HEADER)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def get_sales_data(nt):
    data = []
    with open(TARGET_CSV, 'r', newline='') as fp:
        reader = csv.DictReader(fp, fieldnames=HEADER)
        for r in reader:
            if r['Country'] == nt:
                data.append(r)
    return data

def show(text):
    print(text, end=" ")
    sys.stdout.flush()

def separate_nt(nt):
    data = get_sales_data(nt)
    show(nt)
    save_csv(data, nt.lower() + '.csv')
    return nt         

def main(separate_nt):
    start = time.time()
    end_jobs = []
    worker = min(20, len(NATION_LIST))
    with concurrent.futures.ProcessPoolExecutor(worker) as executor:
        future_workers = []
        for nt in NATION_LIST:
            future_workers.append(executor.submit(
                separate_nt, 
                nt)
                )
        for executor in concurrent.futures.as_completed(future_workers):
            end_jobs.append(executor.result())
    end = time.time()
    msg = f"\n {len(end_jobs)} csv separated in {end-start:.2f}s"
    print(msg)

if __name__ == '__main__':
    main(separate_nt)