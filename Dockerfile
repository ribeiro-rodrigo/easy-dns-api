FROM mc706/pipenv-3.7

LABEL maintainer="Rodrigo Ribeiro"

ARG dns_server_host
ARG dns_avaliable_zones
ARG dns_connection_timeout
ARG tsig_key
ARG auth_username
ARG auth_password
ARG auth_token_expires_in_minutes
ARG server_port
ARG environment 

COPY . /src/easy-dns-api
WORKDIR /src/easy-dns-api

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt 

EXPOSE 5000

ENV DNS_SERVER_HOST=${dns_server_host}
ENV DNS_AVALIABLE_ZONES=${dns_avaliable_zones}
ENV DNS_CONNECTION_TIMEOUT=${dns_connection_timeout}
ENV TSIG_KEY=${tsig_key}
ENV AUTH_USERNAME=${auth_username}
ENV AUTH_PASSWORD=${auth_password}
ENV AUTH_TOKEN_EXPIRES_IN_MINUTES=${auth_token_expires_in_minutes}
ENV SERVER_PORT=${server_port}
ENV ENVIRONMENT=${environment}

CMD ["python", "app.py"]