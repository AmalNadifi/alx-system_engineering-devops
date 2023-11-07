# Automation of the task : creating a custom HTTP header response with Puppet
# Automation: Creating a custom HTTP header response with Puppet

exec { 'command':
  # Update the package list
  command => 'apt-get -y update &&

  # Install Nginx
  apt-get -y install nginx &&

  # Adding a custom HTTP header 'X-Served-By' with the server's hostname to the Nginx configuration
  sed -i "/listen 80 default_server;/a add_header X-Served-By $::hostname;" /etc/nginx/sites-available/default &&

  # Restarting the Nginx service to apply the changes
  service nginx restart',
  provider => shell,
}
