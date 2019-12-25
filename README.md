# gondree.github.io.git


### Clone repository and work with `source` branch
    git clone git@github.com:gondree/gondree.github.io.git
    cd gondree.github.io.git
    git fetch origin
    git branch gh-pages origin/master

### Setup conda environment
	conda create --name gondree.com python=3
	source activate gondree.com

### Install dependencies
    pip install pelican
    pip install Markdown
    pip install ghp-import
    pip install typogrify   # for render_math extension
    pip install fontawesome-markdown  # for font-awesome icons
    pip install Pillow Piexif # for photos plugin

## Running Pelican for development
    # start local server
    make devserver
    # site is viewable at http://localhost:8000/
    # to stop: make stopserver

## Publish
    # You have some changes to the `source` branch
    #   They should be all committed; check with `git status` and commit if any
    #   Now we are about to re-generate the website in a `gh-pages` branch
    # Prep that by getting it up to date:
    git checkout gh-pages
    git pull origin master

    # now, switch back to the `source` branch
    git checkout source

    # now generate the new `output` and use it to update the `gh-pages` branch
    pelican content -o output -s publishconf.py
    ghp-import output

    # now push the local `gh-pages` branch to the remote `master` branch
    git push origin gh-pages:master

    # if you did this wrong, you'll get some type of merge error when
    #    you push gh-pages to the remote master branch and it will
    #    complain that you shoud have done a pull first
