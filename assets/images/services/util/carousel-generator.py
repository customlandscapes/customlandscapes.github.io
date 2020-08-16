#!/usr/bin/env python
#
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('service')
parser.add_argument('one', type=int)
parser.add_argument('two', type=int)
parser.add_argument('three', type=int)
parser.add_argument('four', type=int)
args = parser.parse_args()

service = args.service
full_path = "images/services/{}/".format(service)

# List files and build
list_of_files = [
    {
        'full': full_path + x.split('/')[-1], 
        'file': x.split('.')[0]
    } 
    for x in os.listdir('../{}/'.format(service)) if not x.startswith('.')
]
list_of_files = sorted(list_of_files, key=lambda x: x['file'])
#print('\n'.join([x['full'] for x in list_of_files]))
#print('')

# 3 for carousel
print("""
<div class="carousel-inner">
    <div class="item active carousel-crop" style="background-image:url('{}')">
    </div>
    <div class="item carousel-crop" style="background-image:url('{}')">
    </div>
    <div class="item carousel-crop" style="background-image:url('{}')">
    </div>
</div>
""".format(
    list_of_files[args.one]['full'],
    list_of_files[args.two]['full'],
    list_of_files[args.three]['full'],
))
print('')

print("""<div class="col-sm-3 col-xs-6 blueimp-links">
    <a href="{0}" title="{1}" data-gallery>
        <div class="extra-crop img-responsive img-hover img-related" style="background-image:url('{0}')"></div>
    </a>
</div>

<div class="col-sm-3 col-xs-6 blueimp-links">
    <a href="{2}" title="{3}" data-gallery>
        <div class="extra-crop img-responsive img-hover img-related" style="background-image:url('{2}')"></div>
    </a>
</div>

<div class="col-sm-3 col-xs-6 blueimp-links">
    <a href="{4}" title="{5}" data-gallery>
        <div class="extra-crop img-responsive img-hover img-related" style="background-image:url('{4}')"></div>
    </a>
</div>
""".format(
    list_of_files[args.one]['full'],
    list_of_files[args.one]['file'],
    list_of_files[args.two]['full'],
    list_of_files[args.two]['file'],
    list_of_files[args.three]['full'],
    list_of_files[args.three]['file'],
))

print("""<div class="col-sm-3 col-xs-6 blueimp-links">
    <a href="{0}" title="{1}" data-gallery>
        <div class="extra-crop img-responsive img-hover img-related" style="background-image:url('{0}')">
            <div class="overlay-text-services">
                <span class="overlay-span">More</span>
            </div>
        </div>
    </a>""".format(
    list_of_files[args.four]['full'],
    list_of_files[args.four]['file'],
))

idx = 0
s = {args.one, args.two, args.three, args.four}
for f in list_of_files:
    if idx in s:
        idx += 1
        continue

    print("""   <a href="{}" title="{}" data-gallery></a>""".format(
        f['full'], f['file']
    ))
    idx += 1

print("""</div>""")
