# change-os-configuration-for-holberton-user

# This manuscript enables the user holberton to login and open files without error

# Increase hard file limit for user holberton
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for user holberton
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# # This Puppet script increases the maximum number of open files for the 'holberton' user.

# exec { 'change-os-configuration-for-holberton-user':
#   # Execute the 'ulimit -n 4096' command to increase the file descriptor limit
#   command => 'ulimit -n 4096',
#   # Specify the search path for the command
#   path    => '/bin:/usr/bin:/sbin:/usr/sbin',
#   # Ensure the command returns a successful exit status (0)
#   returns => 0,
# }
