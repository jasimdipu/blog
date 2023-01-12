#!/bin/bash

mysql -u root --password="$DB_PASSWORD"  << EOF
USE ${DB_NAME};
GRANT ALL PRIVILEGES ON  test_${DB_NAME}.* TO '${DB_USER}';
EOF
