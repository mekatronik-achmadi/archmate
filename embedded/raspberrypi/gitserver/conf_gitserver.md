##### login ssh

~~~
ssh alarm@10.124.4.150
sudo su

exit
exit
~~~

##### apache server

~~~
systemctl enable httpd.service
~~~

##### git server

~~~
mkdir -p /srv/git
chown -R http:http /srv/git/
~~~

##### git apache config

~~~
echo 'LoadModule cgi_module modules/mod_cgi.so' >> /etc/httpd/conf/httpd.conf
#echo 'LoadModule env_module modules/mod_env.so' >> /etc/httpd/conf/httpd.conf
#echo 'LoadModule alias_module modules/mod_alias.so' >> /etc/httpd/conf/httpd.conf

echo '
<Directory "/usr/lib/git-core*">
   Options ExecCGI Indexes
   Order allow,deny
   Allow from all
   Require all granted
</Directory>

<LocationMatch "^/.*/git-receive-pack$">
    Options +ExecCGI
    Require all granted
</LocationMatch>

<LocationMatch "^/.*/git-upload-pack$">
    Options +ExecCGI
    Require all granted
</LocationMatch>

SetEnv GIT_PROJECT_ROOT /srv/git
SetEnv GIT_HTTP_EXPORT_ALL
ScriptAlias /git/ /usr/lib/git-core/git-http-backend/
' >> /etc/httpd/conf/httpd.conf

systemctl restart httpd
~~~

##### git authentication (optional)

~~~
cd /srv/git
htpasswd -c htpasswd-git gitserv

echo '
<Location /git/>
        AuthName "Restricted Git"
        AuthType Basic
        AuthUserFile /srv/git/htpasswd-git
        <If "%{QUERY_STRING} =~ m#service=git-receive-pack# || %{REQUEST_URI} =~ m#/git-receive-pack$#">
                Require valid-user
        </If>
        Satisfy all
</Location>
' >> /etc/httpd/conf/httpd.conf

systemctl restart httpd
~~~

##### gitweb interface

~~~
echo '
Alias /gitweb "/usr/share/gitweb"
<Directory "/usr/share/gitweb">
    DirectoryIndex gitweb.cgi
    Options ExecCGI
    Require all granted
    <Files gitweb.cgi>
    	SetHandler cgi-script
    </Files>
    SetEnv  GITWEB_CONFIG  /etc/gitweb.conf
</Directory>' > /etc/httpd/conf/extra/gitweb.conf

echo 'Include conf/extra/gitweb.conf' >> /etc/httpd/conf/httpd.conf

systemctl restart httpd
~~~

~~~
export IPNUMBER='10.124.5.150'

echo "our \$projectroot = \"/srv/git\";" > /etc/gitweb.conf
echo "\$feature{'blame'}{'default'} = [1];" >> /etc/gitweb.conf
echo "\$feature{'highlight'}{'default'} = [1];" >> /etc/gitweb.conf
~~~

##### create server repository

~~~
cd /srv/git
mkdir -p projectTes.git/
git --bare init projectTes.git/
cd projectTes.git/
echo "GitServer Test" > description
git config --file config http.receivepack true

cd /srv/git
chown -R http:http projectTes.git/
~~~

##### check on gitweb (client)

~~~
firefox http://10.124.4.150/gitweb
~~~

##### git clone-push (client)

~~~
git clone http://10.124.4.150/git/projectTes.git
cd projectTes/

echo "test gitserver" > tes.txt
git add .
git commit -m "initial commit"
git push origin master
~~~

##### git add remote (client)

~~~
git remote add gitlocal http://10.124.4.150/git/projectTes.git
git remote -v

git branch
git push gitlocal master
~~~

##### git set head branch

~~~
echo 'ref: refs/heads/master' > /srv/git/projectTes.git/HEAD
echo 'ref: refs/heads/mybranch' > /srv/git/projectTes.git/HEAD
~~~
