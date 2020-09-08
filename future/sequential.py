import os 
import sys
import csv
import time 

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

def separate_many(nt_list):
    for nt in nt_list:
        data = get_sales_data(nt)
        show(nt)
        save_csv(data, nt.lower() + '.csv')
    return len(nt_list)

def main(separate_many):
    start = time.time()
    result_cnt = separate_many(NATION_LIST)
    end = time.time()
    msg = f"\n{result_cnt} csv separated in {end-start:.2f}s"
    print(msg)

if __name__ == '__main__':
    main(separate_many)