# Visit the blog at: https://timhutton.github.io #

## Notes ##

This is a [Jekyll](https://jekyllrb.com/docs/) blog. After installing everything, run these commands to build the static assets and check everything is working:
```
bundle update
bundle exec jekyll serve
```
Online, github does this automatically when you push to master.

### Importing old Google+ posts ###

After downloading the Takeout data, the python script ```gplus_to_jekyll.py``` attempts to extract usable Jekyll format posts from it. But it only mostly works. There must be a better approach?