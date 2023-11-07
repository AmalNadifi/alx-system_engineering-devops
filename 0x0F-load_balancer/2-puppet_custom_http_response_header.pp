# Automating the task of updating the package list using Puppet

# Updating the package list
exec { 'update':
  command   => 'sudo apt-get -y update',
  provider  => shell,
}

# Installing Nginx
exec { 'install':
  command   => 'sudo apt-get -y install nginx',
  provider  => shell,
}

# Adding a custom HTTP header 'X-Served-By' with the server's hostname to the Nginx configuration
exec { 'replace':
  command   => 'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default',
  provider  => shell,
}

# Restarting the Nginx service to apply the changes
exec { 'restart':
  command   => 'sudo service nginx restart',
  provider  => shell,
}
