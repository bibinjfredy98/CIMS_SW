#!/bin/bash
# wait-for-mysql.sh

set -e

host="$1"
shift
cmd="$@"

until mysql -h "$host" -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" -e 'SELECT 1' > /dev/null 2>&1; do
  echo "MySQL is unavailable - sleeping"
  sleep 3
done

echo "MySQL is up - executing command"
exec $cmd
