#!/bin/bash


echo "instaling python3 and pip"
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv

if ! command -v nginx > /dev/null; then
  echo "installing nginx and certbot"
  sudo apt-get install -y nginx certbot python3-certbot-nginx
fi


WWW_ROOT="/var/www_rhflow"
tenants=("org1" "org2")


echo "deleting old files"
sudo rm -rf $WWW_ROOT

echo "create app folder"
sudo mkdir -p $WWW_ROOT


for tenant in "${tenants[@]}"; do
    cd /home/ubuntu
    echo copying files to "${tenant}"
    sudo mkdir -p  $WWW_ROOT/$tenant
    sudo cp -r *  $WWW_ROOT/$tenant
    cd $WWW_ROOT/$tenant

    echo "creating virtual environment for ${tenant}"
    sudo chown -R ubuntu:ubuntu $WWW_ROOT/$tenant
    python3 -m venv venv
    source venv/bin/activate

    echo "installing dependencies"
    pip install -r requirements.txt


    echo "creating nginx site for ${tenant}"
    sudo bash -c "cat > /etc/nginx/sites-available/$tenant << EOF
server {
    listen 80;
    server_name $tenant.lorenzi.net.br;

    location / {
        include proxy_params;
        proxy_pass http://unix:$WWW_ROOT/$tenant/app.sock;
        proxy_redirect off;
    }
    
    location /staticfiles {
        alias $WWW_ROOT/$tenant/static;
    }
}

EOF"

    sudo ln -s /etc/nginx/sites-available/$tenant /etc/nginx/sites-enabled/

    echo "configuring environment variables for ${tenant}"
    sudo mv dotenv .env
    sudo sed -i "s/DB_NAME=.*/DB_NAME=${tenant}/g" .env

    echo "starting gunicorn for ${tenant}"
    cd $WWW_ROOT/$tenant
    gunicorn --workers 3 --bind unix:$WWW_ROOT/$tenant/app.sock rhflow.wsgi:application --user ubuntu --group ubuntu --log-file $WWW_ROOT/$tenant/gunicorn.log --timeout 90 --daemon
    echo "${tenant} deployed successfully"
done

if sudo [ ! -d /etc/letsencrypt/live/lorenzi.net.br ]; then
    echo "certificate lorenzi.net.br not found. "
    echo "deleting old certificates, if exists..."
    sudo certbot delete -n --cert-name lorenzi.net.br
    echo "creating new certificate"
    sudo certbot certonly --nginx \
        -d lorenzi.net.br \
        -d *.lorenzi.net.br \
        -m danilo.lorenzi@gmail.com \
        -n --agree-tos
else
    echo "certificate lorenzi.net.br found. "
fi

echo "installing lorenzi.net.br certificate "
sudo certbot install  --cert-name lorenzi.net.br


echo "restarting nginx"
sudo fuser -k 80/tcp
sudo fuser -k 443/tcp
sudo systemctl restart nginx