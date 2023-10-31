# The following script is a Puppet manifest to install and configure Nginx with a 301 redirect

# Installing the Nginx package
package { 'nginx':
  ensure =>installed,
}

# Add a 301 redirect rule to the Nginx configuration
file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/AmalNadifi permanent;',
}

# Creating a default HTML page with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
}

# Defining the Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Package['nginx'],
}
