FROM node:18-alpine

WORKDIR /usr/src/frontend

COPY package.json .
COPY package-lock.json .
RUN npm install

EXPOSE 3000

CMD [ "npm", "start" ]
