#!/usr/bin/env python
#
# arg should be "images/services/swimming-pools/"
import os

arg = "../0001/"
preamble = "images/portfolio"
full_path = preamble + arg.split('..')[-1]

inner = ""
# wrapper = """<div class="carousel-inner">{}
# </div>
# """
# first = """
#     <div class="item active">
#         <img class="img-responsive" src="{}" alt="">
#     </div>"""
# rest = """
#     <div class="item">
#         <img class="img-responsive" src="{}" alt="">
#     </div>"""
wrapper = "{}"
first = """<div class="col-sm-3 col-xs-6 blueimp-links" style="margin-bottom: 20px;">
    <a href="{}" title="{}" data-gallery>
        <div class="extra-crop img-responsive img-hover img-related"
             style="background-image:url('{}')"></div>
    </a>
</div>
"""
rest = first

# List files and build
list_of_files = [x for x in os.listdir(arg) if not x.startswith('.')]

first_flag = True
for i in list_of_files:
    if '.mov' in i:
        continue

    if first_flag:
        first_flag = False
        inner += first.format(full_path + i.split('/')[-1], i.split('.')[0], full_path + i.split('/')[-1])
    else:
        inner += rest.format(full_path + i.split('/')[-1], i.split('.')[0], full_path + i.split('/')[-1])

print(wrapper.format(inner))
