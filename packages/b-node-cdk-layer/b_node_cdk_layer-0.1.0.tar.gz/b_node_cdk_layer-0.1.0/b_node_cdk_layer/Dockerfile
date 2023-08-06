FROM node:14.5.0

RUN mkdir -p /asset/bin/
RUN cd /asset/bin && npm init --force --yes
RUN cp -L /usr/local/bin/node /asset/bin/node
RUN npm install --prefix /asset/bin aws-cdk@1.150.0
