import argparse
import os

import toddkaye.models as models
CMS = models.CMS

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', 
                    help='The CMS operation to perform')
    parser.add_argument('slug', nargs='?', default='ALL',
                    help='Which slug to operate on or ALL')
    parser.add_argument('--data', default=os.getcwd(), 
                    help='Path to the data directory')

    return parser.parse_args()
    

def checkout(args):
    slug = args.slug
    print(slug)
    session = models.session
    if slug == 'ALL':
        pages = session.query(CMS).all()
    else:
        pages = session.query(CMS).filter(CMS.slug==slug).all()
    
    for page in pages:
        print(page)

def commit(args):
    pass

def list(args):
    session = models.session
    for page in session.query(CMS).all():
        print(page)


def main():
    args = get_args()
    if args. operation == 'checkout':
        checkout(args)
    elif args.operation == 'commit':
        commit(args)
    elif args.operation in ('show', 'list', 'ls'):
        list(args)

if __name__ == '__main__':
    main()