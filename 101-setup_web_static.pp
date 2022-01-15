# Configuring web server using puppet

# Ngninx
$config = "server {
        root        /etc/nginx/html;
        add_header X-Served-By ${HOSTNAME};
        index       index.html index.htm;
        listen      80 default_server;
        listen      [::]:80 default_server;
        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }
        error_page 404 /404.html;
        location /404 {
            root /etc/nginx/html;
            internal;
        }
}"
package { 'nginx':
    ensure   => 'present',
    provider => 'apt'
} ->

file { ['/data/', '/data/web_static/', '/data/web_static/releases/',
        '/data/web_static/releases/test/', '/data/web_static/shared']:
    ensure => 'directory',
} ->

file {'/data/web_static/releases/test/index.html':
    ensure  => 'present',
    content => 'Holberton School\n',
} ->

file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test/',
    force  => yes,
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
    path => '/usr/bin/:/usr/local/bin/:/bin/'

}
file { '/etc/nginx/sites-available/default':
    ensure  => 'present',
    content => $config,
} ->

service { 'nginx restart':
    require => 'etc/init.d'
}
