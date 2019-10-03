#In wp-settings.php there is a misspell in lIne 137
exec { 'change the error':
  command => '/usr/bin/sudo /bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php'
    }
