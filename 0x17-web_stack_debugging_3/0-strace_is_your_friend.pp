# Apache is returning a 500 error. Find the issue,
# fix it and then automate it using Puppet (instead of using Bash)

# A puppet manuscript to replace a line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

# replace line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => '/usr/local/bin/:/bin/' # ['/bin','/usr/bin']
}
