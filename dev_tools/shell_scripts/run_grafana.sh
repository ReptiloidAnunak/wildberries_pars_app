clear
echo "🔎 Run Grafana & Promtail"
cd monitoring && docker-compose up -d
docker exec -it monitoring_grafana_1 grafana-cli admin reset-admin-password admin
clear
echo -r "\n\nGrafana is running. See your logs here: http://127.0.0.1:3000/login"