FROM node:16.13.1
ENV NODE_ENV=production
WORKDIR /frontend/
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install 
COPY . /frontend/