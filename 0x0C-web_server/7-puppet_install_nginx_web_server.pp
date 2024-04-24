# install and configure an Nginx server using Puppet instead of Bash
# include resources in your manifest to perform a 301 redirect when querying `/redirect_me`

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get install -y nginx',
  provider => shell,

}

exec {'Hello':
  command  => 'echo "Hello World!" > /var/www/html/index.nginx-debian.html',
  provider => shell,
}

exec {'sudo sed -i "/listen 80 default_server/a return 301 https://github.com/OluTshegz;" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
