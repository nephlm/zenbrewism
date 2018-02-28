REPO=~/Src/web/toddkaye.com
DST=/var/www/toddkaye.com
SERVER=webserver

rsync -avz $REPO/react/build $SERVER:$DST/react/
rsync -avz $REPO/edit/build $SERVER:$DST/edit/
rsync -avz --exclude .htpasswd --exclude config.py $REPO/flask $SERVER:$DST/
rsync -avz $REPO/etc $SERVER:/tmp/
scp $REPO/*.sh $SERVER:$DST/