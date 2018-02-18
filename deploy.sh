REPO=~/Src/web/toddkaye.com
DST=/var/www/toddkaye.com
SERVER=webserver

rsync -avz $REPO/react/build $SERVER:$DST/react/
rsync -avz $REPO/flask $SERVER:$DST/
rsync -avz $REPO/etc $SERVER:/tmp/
rcp $REPO/*.sh $SERVER:$DST/