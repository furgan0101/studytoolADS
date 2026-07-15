FROM nginx:alpine

# nginx config: serve the trainer as the default page
COPY default.conf /etc/nginx/conf.d/default.conf

# the app + its exam page images
COPY algorithms-study-app.html /usr/share/nginx/html/
COPY img/ /usr/share/nginx/html/img/

EXPOSE 80
