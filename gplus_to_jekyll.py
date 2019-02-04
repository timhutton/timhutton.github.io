
import glob
import os
from shutil import copyfile

input_folder  = 'C:/Tim/Takeout/Google+ Stream/Posts/'
output_folder = 'C:/Tim/Takeout/output/'
output_assets_folder = 'C:/Tim/Takeout/output_assets/'

# get the list of asset names
asset_filenames = [f.split('\\')[-1] for f in glob.glob(input_folder+'*')]
assets_used = set()

# write new files
for f in glob.glob(input_folder+'*.html'):
    print('Reading '+f)
    filetitle = f.split('\\')[-1].split('.html')[0]
    date = filetitle[:8]
    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    title = filetitle[11:]
    out_filename = output_folder+str(year)+'-'+str(month)+'-'+str(day)+'-'+title+'.md'
    with open(f, 'r', encoding='utf-8') as in_file:
        lines = in_file.readlines()
        main_content = '\n'.join(lines)
    for asset_filename in asset_filenames:
        if '"'+asset_filename+'"' in main_content:
            main_content = main_content.replace('"'+asset_filename+'"', '"/assets/'+asset_filename+'"')
            assets_used.add(asset_filename)
    print('Writing '+out_filename)
    with open(out_filename,'w', encoding='utf-8') as out_file:
        print(title)
        out_file.write('---\nlayout: post\ntitle: '+title+'\n---\n\n')
        out_file.write(main_content)
        out_file.write('\n\n<i>This post was originally on Google+</i>')

# copy assets used to output folder
print('\nCopying assets that are referenced...')
for asset_filename in assets_used:
    copyfile(input_folder+asset_filename, output_assets_folder+asset_filename)
