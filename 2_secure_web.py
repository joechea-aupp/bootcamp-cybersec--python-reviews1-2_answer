# write a script to convert the following unsecure url to a secure url
# http://facebook.com:80 to https://facebook.com:443
url = 'http://facebook.com:80'
url = url.replace('http', 'https').replace(':80', ':443')
