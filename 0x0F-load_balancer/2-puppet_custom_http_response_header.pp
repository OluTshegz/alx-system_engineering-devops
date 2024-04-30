# Using Puppet to automate the task of creating a custom HTTP header response
# configures a brand new Ubuntu machine to the requirements asked in this task

exec { 'update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin/',
}

package { 'nginx':
  ensure  => 'present',
  require => Exec['update'],
}

file_line { 'http_header':
  path    => '/etc/nginx/nginx.conf',
  match   => 'http {',
  line    => "    add_header X-Served-By \"${hostname}\";",
  require => Package['nginx'],
}

exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
  require => File_line['http_header'],
}
