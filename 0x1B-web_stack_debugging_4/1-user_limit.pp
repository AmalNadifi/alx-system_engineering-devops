# The following Puppet script adjusts user permissions for the holberton user to enable login and file operations without errors.

# Increasing the hard file limit for the Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
# Modifying the hard file limit in /etc/security/limits.conf for holberton user to 50000

# Increasing the soft file limit for the Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
# Modifying the soft file limit in /etc/security/limits.conf for holberton user to 50000
